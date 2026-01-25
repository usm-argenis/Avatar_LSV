class SkeletonViewer {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        this.clock = new THREE.Clock();
        this.bones = [];
        this.joints = [];
        this.lines = [];
        this.frames = [];
        this.frameIndex = 0;
        this.fps = 30;
        this.isPlaying = true;
        this.interpolationEnabled = true; // Suavizar entre frames

        // Setup renderer con mejor calidad
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.setClearColor(0x1a1a2e);
        this.renderer.shadowMap.enabled = true;
        this.container.appendChild(this.renderer.domElement);

        // Setup camera
        this.camera.position.set(0, 1.5, 3);
        this.camera.lookAt(0, 1, 0);

        // Setup controls mejorados
        this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.08; // Más suave
        this.controls.minDistance = 0.5;
        this.controls.maxDistance = 15;
        this.controls.target.set(0, 1, 0);
        this.controls.rotateSpeed = 0.5;
        this.controls.zoomSpeed = 0.8;

        // Add lights mejoradas
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        this.scene.add(ambientLight);
        
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.6);
        directionalLight.position.set(5, 10, 5);
        directionalLight.castShadow = true;
        this.scene.add(directionalLight);
        
        const fillLight = new THREE.DirectionalLight(0x4fc3f7, 0.3);
        fillLight.position.set(-5, 5, -5);
        this.scene.add(fillLight);

        // Add grid and axes
        const gridHelper = new THREE.GridHelper(10, 10);
        this.scene.add(gridHelper);
        const axesHelper = new THREE.AxesHelper(5);
        this.scene.add(axesHelper);

        // Handle window resize
        window.addEventListener('resize', () => {
            this.camera.aspect = window.innerWidth / window.innerHeight;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(window.innerWidth, window.innerHeight);
        });
    }

    loadSkeleton(url) {
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log("Loaded skeleton data: bones=", (data.bones||[]).length,
                    " frames=", (data.frames||[]).length, " fps=", data.fps);
                this.bones = data.bones || [];
                this.frames = data.frames || [];
                this.fps = data.fps || 30;
                this.createSkeletonMesh();
                // Apply first pose immediately so user sees the avatar
                if (this.frames.length > 0) {
                    console.log('Applying initial pose from first frame');
                    this.updateSkeletonPose(this.frames[0]);
                    // Auto-fit camera to skeleton bounds
                    this.autoFitCamera();
                } else {
                    console.log('No frames available yet');
                }
                // Start animation loop
                this.animate();
            })
            .catch(error => console.error('Error loading skeleton:', error));
    }

    // Compute bounding box for the skeleton across a sample of frames and adjust camera
    autoFitCamera(sampleFrames = 20) {
        if (!this.frames || this.frames.length === 0) return;
        const count = Math.min(sampleFrames, this.frames.length);
        const mins = [Number.POSITIVE_INFINITY, Number.POSITIVE_INFINITY, Number.POSITIVE_INFINITY];
        const maxs = [Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY, Number.NEGATIVE_INFINITY];
        for (let fi = 0; fi < count; fi++) {
            const frame = this.frames[fi];
            if (!frame || !frame.positions) continue;
            for (let p of frame.positions) {
                if (!p || p.length < 3) continue;
                for (let i = 0; i < 3; i++) {
                    if (p[i] < mins[i]) mins[i] = p[i];
                    if (p[i] > maxs[i]) maxs[i] = p[i];
                }
            }
        }

        // Compute center and size
        const center = [(mins[0] + maxs[0]) / 2, (mins[1] + maxs[1]) / 2, (mins[2] + maxs[2]) / 2];
        const size = [maxs[0] - mins[0], maxs[1] - mins[1], maxs[2] - mins[2]];
        const maxSize = Math.max(size[0], size[1], size[2], 0.1);

        // Place camera so the whole bbox fits in view. Use perspective fov to compute distance.
        const fov = this.camera.fov * (Math.PI / 180);
        const distance = (maxSize / 2) / Math.tan(fov / 2);
        // add some margin
        const margin = 1.5;
        const camPos = [center[0], center[1] + maxSize * 0.3, center[2] + distance * margin];

        this.camera.position.set(camPos[0], camPos[1], camPos[2]);
        this.controls.target.set(center[0], center[1], center[2]);
        this.controls.update();
        console.log('autoFitCamera: center=', center, 'size=', size, 'camera pos=', camPos);
    }

    createSkeletonMesh() {
        // Clear existing meshes
        this.joints.forEach(joint => this.scene.remove(joint));
        this.lines.forEach(line => this.scene.remove(line));
        this.joints = [];
        this.lines = [];

        // Create joints con colores por categoría
        for (let i = 0; i < this.bones.length; i++) {
            const bone = this.bones[i];
            let size = 0.02;
            let color = 0x00ff00; // Verde para pose por defecto
            let emissiveIntensity = 0.3;

            // Determinar color y tamaño según tipo de hueso
            if (bone.name.includes('left_hand')) {
                color = 0xff4444; // Rojo para mano izquierda
                size = 0.015;
            } else if (bone.name.includes('right_hand')) {
                color = 0x4444ff; // Azul para mano derecha
                size = 0.015;
            } else if (bone.name.includes('face')) {
                color = 0xffff00; // Amarillo para rostro
                size = 0.01;
            } else if (bone.name.includes('wrist') || bone.name.includes('elbow') || 
                       bone.name.includes('shoulder') || bone.name.includes('hip') ||
                       bone.name.includes('knee') || bone.name.includes('ankle')) {
                size = 0.03; // Joints principales más grandes
                emissiveIntensity = 0.5;
            }

            // Crear esfera con material mejorado
            const jointGeometry = new THREE.SphereGeometry(size, 12, 12);
            const jointMaterial = new THREE.MeshPhongMaterial({ 
                color: color,
                emissive: color,
                emissiveIntensity: emissiveIntensity,
                shininess: 30
            });
            const joint = new THREE.Mesh(jointGeometry, jointMaterial);
            joint.castShadow = true;
            this.scene.add(joint);
            this.joints.push(joint);

            // Create lines to parent con color matching
            if (bone.parent !== undefined && bone.parent !== null) {
                const parentIndex = this.bones.findIndex(b => b.name === bone.parent);
                if (parentIndex >= 0) {
                    const lineMaterial = new THREE.LineBasicMaterial({ 
                        color: color,
                        linewidth: 2,
                        opacity: 0.7,
                        transparent: true
                    });
                    const lineGeometry = new THREE.BufferGeometry();
                    const positions = new Float32Array(6);
                    lineGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
                    const line = new THREE.Line(lineGeometry, lineMaterial);
                    line.userData.parentIndex = parentIndex;
                    line.userData.childIndex = i;
                    this.scene.add(line);
                    this.lines.push(line);
                } else {
                    this.lines.push(null);
                }
            } else {
                this.lines.push(null);
            }
        }
    }

    updateSkeletonPose(frame, nextFrame = null, t = 0) {
        const positions = frame.positions;
        
        for (let i = 0; i < Math.min(positions.length, this.joints.length); i++) {
            const pos = positions[i];
            const joint = this.joints[i];
            if (!joint || !pos) continue;
            
            // Interpolación suave entre frames si está habilitada
            if (this.interpolationEnabled && nextFrame && nextFrame.positions[i] && t > 0 && t < 1) {
                const nextPos = nextFrame.positions[i];
                const x = pos[0] + (nextPos[0] - pos[0]) * t;
                const y = pos[1] + (nextPos[1] - pos[1]) * t;
                const z = pos[2] + (nextPos[2] - pos[2]) * t;
                joint.position.set(x, y, z);
            } else {
                joint.position.set(pos[0], pos[1], pos[2]);
            }
        }
        
        // Update lines con mejor manejo de conexiones
        this.lines.forEach((line, i) => {
            if (!line) return;
            
            const parentIdx = line.userData.parentIndex;
            const childIdx = line.userData.childIndex;
            
            if (parentIdx === undefined || childIdx === undefined) return;
            
            const parentPos = positions[parentIdx];
            const childPos = positions[childIdx];
            
            if (!parentPos || !childPos) return;
            
            // Interpolación para líneas también
            let pPos = parentPos;
            let cPos = childPos;
            
            if (this.interpolationEnabled && nextFrame && nextFrame.positions[parentIdx] && 
                nextFrame.positions[childIdx] && t > 0 && t < 1) {
                const nextParent = nextFrame.positions[parentIdx];
                const nextChild = nextFrame.positions[childIdx];
                
                pPos = [
                    parentPos[0] + (nextParent[0] - parentPos[0]) * t,
                    parentPos[1] + (nextParent[1] - parentPos[1]) * t,
                    parentPos[2] + (nextParent[2] - parentPos[2]) * t
                ];
                
                cPos = [
                    childPos[0] + (nextChild[0] - childPos[0]) * t,
                    childPos[1] + (nextChild[1] - childPos[1]) * t,
                    childPos[2] + (nextChild[2] - childPos[2]) * t
                ];
            }
            
            const linePositions = line.geometry.attributes.position.array;
            linePositions[0] = pPos[0];
            linePositions[1] = pPos[1];
            linePositions[2] = pPos[2];
            linePositions[3] = cPos[0];
            linePositions[4] = cPos[1];
            linePositions[5] = cPos[2];
            line.geometry.attributes.position.needsUpdate = true;
            line.geometry.computeBoundingSphere();
        });
    }

    animate() {
        requestAnimationFrame(() => this.animate());

        if (this.isPlaying && this.frames.length > 0) {
            const delta = this.clock.getDelta();
            this.frameIndex = (this.frameIndex + this.fps * delta) % this.frames.length;
            
            const currentFrameIdx = Math.floor(this.frameIndex);
            const nextFrameIdx = (currentFrameIdx + 1) % this.frames.length;
            const t = this.frameIndex - currentFrameIdx; // Fracción para interpolación
            
            const currentFrame = this.frames[currentFrameIdx];
            const nextFrame = this.frames[nextFrameIdx];
            
            if (currentFrame) {
                this.updateSkeletonPose(currentFrame, nextFrame, t);
            }
        }

        this.controls.update();
        this.renderer.render(this.scene, this.camera);
    }
    
    // Métodos de control de reproducción
    play() {
        this.isPlaying = true;
    }
    
    pause() {
        this.isPlaying = false;
    }
    
    stop() {
        this.isPlaying = false;
        this.frameIndex = 0;
        if (this.frames.length > 0) {
            this.updateSkeletonPose(this.frames[0]);
        }
    }
    
    toggleInterpolation() {
        this.interpolationEnabled = !this.interpolationEnabled;
        console.log('Interpolación:', this.interpolationEnabled ? 'ON' : 'OFF');
    }
}