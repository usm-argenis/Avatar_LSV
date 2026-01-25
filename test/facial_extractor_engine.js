// ============================================================================
// MOTOR PROFESIONAL DE EXTRACCIÓN DE EXPRESIONES FACIALES
// Versión 2.0 - Sistema de alta precisión con normalización y filtrado
// ============================================================================

class FacialExpressionEngine {
    constructor() {
        this.smoothingFrames = 5; // Frames para suavizado temporal
        this.noiseThreshold = 0.08; // Umbral para filtrar ruido
        this.history = []; // Historial de frames para suavizado
        this.referenceScale = null; // Escala de referencia (distancia entre ojos)
        
        // Definir shape keys con configuración precisa
        this.shapeKeyConfigs = this.initializeShapeKeyConfigs();
    }
    
    initializeShapeKeyConfigs() {
        return {
            // === OJOS ===
            eyeBlinkLeft: {
                landmarks: { top: 159, bottom: 145, left: 33, right: 133 },
                type: 'eye_aspect_ratio',
                thresholds: { closed: 0.15, open: 0.25 },
                invert: true
            },
            eyeBlinkRight: {
                landmarks: { top: 386, bottom: 374, left: 362, right: 263 },
                type: 'eye_aspect_ratio',
                thresholds: { closed: 0.15, open: 0.25 },
                invert: true
            },
            eyeSquintLeft: {
                landmarks: { top: 159, bottom: 145, left: 33, right: 133 },
                type: 'eye_aspect_ratio',
                thresholds: { squinted: 0.18, normal: 0.23 },
                invert: true
            },
            eyeSquintRight: {
                landmarks: { top: 386, bottom: 374, left: 362, right: 263 },
                type: 'eye_aspect_ratio',
                thresholds: { squinted: 0.18, normal: 0.23 },
                invert: true
            },
            eyeWideLeft: {
                landmarks: { top: 159, bottom: 145, left: 33, right: 133 },
                type: 'eye_aspect_ratio',
                thresholds: { normal: 0.25, wide: 0.35 },
                invert: false
            },
            eyeWideRight: {
                landmarks: { top: 386, bottom: 374, left: 362, right: 263 },
                type: 'eye_aspect_ratio',
                thresholds: { normal: 0.25, wide: 0.35 },
                invert: false
            },
            
            // === CEJAS ===
            browInnerUp: {
                landmarks: { brow: [55, 285], reference: [6, 10] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.45, raised: 0.55 },
                invert: false
            },
            browDownLeft: {
                landmarks: { brow: 46, reference: [6, 70] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.42, down: 0.35 },
                invert: true
            },
            browDownRight: {
                landmarks: { brow: 276, reference: [6, 300] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.42, down: 0.35 },
                invert: true
            },
            browOuterUpLeft: {
                landmarks: { brow: 46, reference: [10, 70] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.52, raised: 0.62 },
                invert: false
            },
            browOuterUpRight: {
                landmarks: { brow: 276, reference: [10, 300] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.52, raised: 0.62 },
                invert: false
            },
            
            // === BOCA ===
            mouthSmileLeft: {
                landmarks: { corner: 61, center: 13, reference: [33, 263] },
                type: 'mouth_width',
                normalizedThresholds: { rest: 0.55, smile: 0.70 },
                invert: false
            },
            mouthSmileRight: {
                landmarks: { corner: 291, center: 13, reference: [33, 263] },
                type: 'mouth_width',
                normalizedThresholds: { rest: 0.55, smile: 0.70 },
                invert: false
            },
            mouthFrownLeft: {
                landmarks: { corner: 61, center: 13, reference: [33, 263] },
                type: 'mouth_width',
                normalizedThresholds: { rest: 0.55, frown: 0.48 },
                invert: true
            },
            mouthFrownRight: {
                landmarks: { corner: 291, center: 13, reference: [33, 263] },
                type: 'mouth_width',
                normalizedThresholds: { rest: 0.55, frown: 0.48 },
                invert: true
            },
            mouthOpen: {
                landmarks: { top: 13, bottom: 14, reference: [10, 152] },
                type: 'vertical_distance',
                normalizedThresholds: { closed: 0.03, open: 0.15 },
                invert: false
            },
            jawOpen: {
                landmarks: { top: 0, bottom: 17, reference: [10, 152] },
                type: 'vertical_distance',
                normalizedThresholds: { closed: 0.20, open: 0.35 },
                invert: false
            },
            mouthFunnel: {
                landmarks: { top: 13, bottom: 14, left: 61, right: 291 },
                type: 'aspect_ratio',
                thresholds: { normal: 0.3, funnel: 0.8 },
                invert: false
            },
            mouthPucker: {
                landmarks: { left: 61, right: 291, reference: [33, 263] },
                type: 'horizontal_distance',
                normalizedThresholds: { rest: 0.55, pucker: 0.40 },
                invert: true
            },
            mouthUpperUpLeft: {
                landmarks: { lip: 13, nose: 2, reference: [10, 152] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.12, up: 0.08 },
                invert: true
            },
            mouthUpperUpRight: {
                landmarks: { lip: 13, nose: 2, reference: [10, 152] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.12, up: 0.08 },
                invert: true
            },
            mouthLowerDownLeft: {
                landmarks: { lip: 14, chin: 152, reference: [10, 152] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.15, down: 0.20 },
                invert: false
            },
            mouthLowerDownRight: {
                landmarks: { lip: 14, chin: 152, reference: [10, 152] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.15, down: 0.20 },
                invert: false
            },
            
            // === MEJILLAS ===
            cheekSquintLeft: {
                landmarks: { cheek: 116, reference: [123, 227] },
                type: 'distance',
                normalizedThresholds: { rest: 0.12, squint: 0.08 },
                invert: true
            },
            cheekSquintRight: {
                landmarks: { cheek: 345, reference: [352, 447] },
                type: 'distance',
                normalizedThresholds: { rest: 0.12, squint: 0.08 },
                invert: true
            },
            cheekPuff: {
                landmarks: { left: 116, right: 345, reference: [33, 263] },
                type: 'horizontal_distance',
                normalizedThresholds: { rest: 0.85, puff: 0.95 },
                invert: false
            },
            
            // === NARIZ ===
            noseSneerLeft: {
                landmarks: { nostril: 36, bridge: 6, reference: [10, 152] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.25, sneer: 0.20 },
                invert: true
            },
            noseSneerRight: {
                landmarks: { nostril: 266, bridge: 6, reference: [10, 152] },
                type: 'vertical_distance',
                normalizedThresholds: { rest: 0.25, sneer: 0.20 },
                invert: true
            }
        };
    }
    
    // Calcular distancia euclidiana 2D
    distance2D(p1, p2) {
        return Math.sqrt(Math.pow(p2.x - p1.x, 2) + Math.pow(p2.y - p1.y, 2));
    }
    
    // Calcular distancia vertical
    distanceY(p1, p2) {
        return Math.abs(p2.y - p1.y);
    }
    
    // Calcular distancia horizontal
    distanceX(p1, p2) {
        return Math.abs(p2.x - p1.x);
    }
    
    // Calcular escala de referencia (distancia entre ojos)
    calculateReferenceScale(landmarks) {
        const leftEye = landmarks[33];
        const rightEye = landmarks[263];
        return this.distance2D(leftEye, rightEye);
    }
    
    // Calcular aspect ratio de ojo
    calculateEyeAspectRatio(landmarks, config) {
        const top = landmarks[config.landmarks.top];
        const bottom = landmarks[config.landmarks.bottom];
        const left = landmarks[config.landmarks.left];
        const right = landmarks[config.landmarks.right];
        
        if (!top || !bottom || !left || !right) return 0.20; // Valor neutral si faltan landmarks
        
        const height = this.distanceY(top, bottom);
        const width = this.distanceX(left, right);
        
        return height / (width + 0.0001); // Evitar división por 0
    }
    
    // Calcular distancia vertical normalizada
    calculateVerticalDistance(landmarks, config) {
        let distance;
        
        if (Array.isArray(config.landmarks.brow)) {
            // Promedio de múltiples puntos
            const distances = config.landmarks.brow.map(idx => {
                const point = landmarks[idx];
                const ref = landmarks[config.landmarks.reference[0]];
                if (!point || !ref) return 0;
                return this.distanceY(point, ref);
            }).filter(d => d > 0);
            
            if (distances.length === 0) return 0;
            distance = distances.reduce((a, b) => a + b) / distances.length;
        } else {
            const pointIdx = config.landmarks.brow || config.landmarks.lip || config.landmarks.nostril || config.landmarks.top;
            const point = landmarks[pointIdx];
            const ref = landmarks[config.landmarks.reference[0]];
            
            if (!point || !ref) return 0;
            distance = this.distanceY(point, ref);
        }
        
        // Normalizar por escala de referencia
        if (this.referenceScale === 0) return 0;
        return distance / this.referenceScale;
    }
    
    // Calcular distancia horizontal normalizada
    calculateHorizontalDistance(landmarks, config) {
        const p1 = landmarks[config.landmarks.left || config.landmarks.corner];
        const p2 = landmarks[config.landmarks.right];
        const ref1 = landmarks[config.landmarks.reference[0]];
        const ref2 = landmarks[config.landmarks.reference[1]];
        
        if (!p1 || !p2 || !ref1 || !ref2) return 0;
        
        const distance = this.distanceX(p1, p2);
        const refDistance = this.distanceX(ref1, ref2);
        
        if (refDistance === 0) return 0;
        return distance / refDistance;
    }
    
    // Calcular aspect ratio
    calculateAspectRatio(landmarks, config) {
        const top = landmarks[config.landmarks.top];
        const bottom = landmarks[config.landmarks.bottom];
        const left = landmarks[config.landmarks.left];
        const right = landmarks[config.landmarks.right];
        
        if (!top || !bottom || !left || !right) return 0;
        
        const height = this.distanceY(top, bottom);
        const width = this.distanceX(left, right);
        
        return height / (width + 0.0001);
    }
    
    // Calcular distancia simple normalizada
    calculateDistance(landmarks, config) {
        const point = landmarks[config.landmarks.cheek];
        const ref = landmarks[config.landmarks.reference[0]];
        
        if (!point || !ref) return 0;
        
        const distance = this.distance2D(point, ref);
        
        if (this.referenceScale === 0) return 0;
        return distance / this.referenceScale;
    }
    
    // Extraer valor de un shape key específico
    extractShapeKeyValue(landmarks, name, config) {
        let rawValue;
        
        switch (config.type) {
            case 'eye_aspect_ratio':
                const aspectRatio = this.calculateEyeAspectRatio(landmarks, config);
                const thresholdKeys = Object.keys(config.thresholds);
                const minThreshold = config.thresholds[thresholdKeys[0]];
                const maxThreshold = config.thresholds[thresholdKeys[1]];
                
                if (config.invert) {
                    rawValue = Math.max(0, Math.min(1, (maxThreshold - aspectRatio) / (maxThreshold - minThreshold)));
                } else {
                    rawValue = Math.max(0, Math.min(1, (aspectRatio - minThreshold) / (maxThreshold - minThreshold)));
                }
                break;
                
            case 'vertical_distance':
                const vDist = this.calculateVerticalDistance(landmarks, config);
                const vThresholdKeys = Object.keys(config.normalizedThresholds);
                const vMinThreshold = config.normalizedThresholds[vThresholdKeys[0]];
                const vMaxThreshold = config.normalizedThresholds[vThresholdKeys[1]];
                
                if (config.invert) {
                    rawValue = Math.max(0, Math.min(1, (vMinThreshold - vDist) / (vMinThreshold - vMaxThreshold)));
                } else {
                    rawValue = Math.max(0, Math.min(1, (vDist - vMinThreshold) / (vMaxThreshold - vMinThreshold)));
                }
                break;
                
            case 'horizontal_distance':
                const hDist = this.calculateHorizontalDistance(landmarks, config);
                const hThresholdKeys = Object.keys(config.normalizedThresholds);
                const hMinThreshold = config.normalizedThresholds[hThresholdKeys[0]];
                const hMaxThreshold = config.normalizedThresholds[hThresholdKeys[1]];
                
                if (config.invert) {
                    rawValue = Math.max(0, Math.min(1, (hMinThreshold - hDist) / (hMinThreshold - hMaxThreshold)));
                } else {
                    rawValue = Math.max(0, Math.min(1, (hDist - hMinThreshold) / (hMaxThreshold - hMinThreshold)));
                }
                break;
                
            case 'aspect_ratio':
                const ar = this.calculateAspectRatio(landmarks, config);
                const arThresholdKeys = Object.keys(config.thresholds);
                const arMinThreshold = config.thresholds[arThresholdKeys[0]];
                const arMaxThreshold = config.thresholds[arThresholdKeys[1]];
                
                rawValue = Math.max(0, Math.min(1, (ar - arMinThreshold) / (arMaxThreshold - arMinThreshold)));
                break;
                
            case 'distance':
                const dist = this.calculateDistance(landmarks, config);
                const dThresholdKeys = Object.keys(config.normalizedThresholds);
                const dMinThreshold = config.normalizedThresholds[dThresholdKeys[0]];
                const dMaxThreshold = config.normalizedThresholds[dThresholdKeys[1]];
                
                if (config.invert) {
                    rawValue = Math.max(0, Math.min(1, (dMinThreshold - dist) / (dMinThreshold - dMaxThreshold)));
                } else {
                    rawValue = Math.max(0, Math.min(1, (dist - dMinThreshold) / (dMaxThreshold - dMinThreshold)));
                }
                break;
                
            default:
                rawValue = 0;
        }
        
        return rawValue;
    }
    
    // Extraer todos los shape keys de un frame
    extractFromFrame(landmarks) {
        if (!landmarks || landmarks.length < 478) {
            return null;
        }
        
        // Calcular escala de referencia
        this.referenceScale = this.calculateReferenceScale(landmarks);
        
        const shapeKeys = {};
        
        // Extraer cada shape key
        for (const [name, config] of Object.entries(this.shapeKeyConfigs)) {
            try {
                shapeKeys[name] = this.extractShapeKeyValue(landmarks, name, config);
            } catch (error) {
                console.warn(`Error extracting ${name}:`, error);
                shapeKeys[name] = 0;
            }
        }
        
        return shapeKeys;
    }
    
    // Aplicar suavizado temporal
    applySmoothing(shapeKeys) {
        const smoothed = {};
        
        // Si no hay suficiente historial, retornar valores sin suavizar
        if (this.history.length < 2) {
            return shapeKeys;
        }
        
        const framesToAverage = Math.min(this.smoothingFrames, this.history.length);
        
        for (const key in shapeKeys) {
            let sum = 0;
            for (let i = 0; i < framesToAverage; i++) {
                sum += this.history[this.history.length - 1 - i][key] || 0;
            }
            smoothed[key] = sum / framesToAverage;
        }
        
        return smoothed;
    }
    
    // Filtrar ruido (valores muy pequeños)
    filterNoise(shapeKeys) {
        const filtered = {};
        
        for (const [key, value] of Object.entries(shapeKeys)) {
            filtered[key] = value < this.noiseThreshold ? 0 : value;
        }
        
        return filtered;
    }
    
    // Procesar frame completo
    processFrame(landmarks) {
        // Extraer valores crudos
        let shapeKeys = this.extractFromFrame(landmarks);
        
        if (!shapeKeys) {
            return null;
        }
        
        // Agregar al historial
        this.history.push(shapeKeys);
        if (this.history.length > this.smoothingFrames) {
            this.history.shift();
        }
        
        // Aplicar suavizado temporal
        shapeKeys = this.applySmoothing(shapeKeys);
        
        // Filtrar ruido
        shapeKeys = this.filterNoise(shapeKeys);
        
        // Redondear valores
        for (const key in shapeKeys) {
            shapeKeys[key] = Math.round(shapeKeys[key] * 100) / 100;
        }
        
        return shapeKeys;
    }
    
    // Reset historial
    reset() {
        this.history = [];
    }
    
    // Configurar parámetros
    setSmoothing(frames) {
        this.smoothingFrames = Math.max(1, Math.min(10, frames));
    }
    
    setNoiseThreshold(threshold) {
        this.noiseThreshold = Math.max(0, Math.min(0.5, threshold));
    }
}

// ============================================================================
// APLICACIÓN PRINCIPAL
// ============================================================================

let engine, faceMesh, video;
let model3D, meshesWithTargets = [];
let animationData = null;
let currentResults = null;
let isAnalyzing = false;
let isSyncing = false;
let analysisAborted = false;

// Inicializar
window.addEventListener('DOMContentLoaded', () => {
    engine = new FacialExpressionEngine();
    initializeUI();
    initializeThreeJS();
    initializeMediaPipe();
    initializeVideoHandlers();
});

function initializeUI() {
    // Sliders de configuración
    document.getElementById('smoothingSlider').addEventListener('input', (e) => {
        const value = parseInt(e.target.value);
        engine.setSmoothing(value);
        document.getElementById('smoothingValue').textContent = value;
    });
    
    document.getElementById('noiseSlider').addEventListener('input', (e) => {
        const value = parseInt(e.target.value) / 100;
        engine.setNoiseThreshold(value);
        document.getElementById('noiseValue').textContent = value.toFixed(2);
    });
    
    // Crear panel de shape keys
    createShapeKeysPanel();
}

function createShapeKeysPanel() {
    const panel = document.getElementById('shapeKeysPanel');
    const categories = {
        'OJOS': ['eyeBlinkLeft', 'eyeBlinkRight', 'eyeSquintLeft', 'eyeSquintRight', 'eyeWideLeft', 'eyeWideRight'],
        'CEJAS': ['browInnerUp', 'browDownLeft', 'browDownRight', 'browOuterUpLeft', 'browOuterUpRight'],
        'BOCA': ['mouthSmileLeft', 'mouthSmileRight', 'mouthFrownLeft', 'mouthFrownRight', 'mouthOpen', 'jawOpen', 'mouthFunnel', 'mouthPucker', 'mouthUpperUpLeft', 'mouthUpperUpRight', 'mouthLowerDownLeft', 'mouthLowerDownRight'],
        'MEJILLAS': ['cheekSquintLeft', 'cheekSquintRight', 'cheekPuff'],
        'NARIZ': ['noseSneerLeft', 'noseSneerRight']
    };
    
    for (const [category, keys] of Object.entries(categories)) {
        panel.innerHTML += `<div class="section-title">${category}</div>`;
        
        keys.forEach(key => {
            panel.innerHTML += `
                <div class="shape-key-item">
                    <div class="shape-key-name">${key}</div>
                    <div class="shape-key-bar">
                        <div class="shape-key-fill" id="bar-${key}"></div>
                    </div>
                    <div class="shape-key-value" id="val-${key}">0.00</div>
                </div>
            `;
        });
    }
}

function initializeThreeJS() {
    const canvas = document.getElementById('canvas3d');
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x0a0e27);
    
    const camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
    camera.position.set(0, 1.6, 2);
    
    const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
    renderer.setSize(canvas.clientWidth, canvas.clientHeight);
    
    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.target.set(0, 1.4, 0);
    controls.update();
    
    scene.add(new THREE.AmbientLight(0xffffff, 0.7));
    const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight.position.set(5, 10, 5);
    scene.add(dirLight);
    
    // Cargar modelo Luis
    const loader = new THREE.GLTFLoader();
    loader.load('output/glb/Luis/Luis.glb', (gltf) => {
        model3D = gltf.scene;
        scene.add(model3D);
        
        const box = new THREE.Box3().setFromObject(model3D);
        const center = box.getCenter(new THREE.Vector3());
        model3D.position.sub(center);
        model3D.position.y = 0;
        
        model3D.traverse(child => {
            if (child.isMesh && child.morphTargetInfluences) {
                meshesWithTargets.push(child);
            }
        });
        
        updateQuality('good', 'Modelo Cargado', `${meshesWithTargets.length} meshes con morph targets`);
    });
    
    function animate() {
        requestAnimationFrame(animate);
        controls.update();
        renderer.render(scene, camera);
    }
    animate();
    
    // Handle resize
    window.addEventListener('resize', () => {
        camera.aspect = canvas.clientWidth / canvas.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(canvas.clientWidth, canvas.clientHeight);
    });
}

function initializeMediaPipe() {
    faceMesh = new FaceMesh({
        locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh@0.4.1633559619/${file}`
    });
    
    faceMesh.setOptions({
        maxNumFaces: 1,
        refineLandmarks: true,
        minDetectionConfidence: 0.7,
        minTrackingConfidence: 0.7
    });
    
    faceMesh.onResults((results) => {
        currentResults = results;
    });
}

function initializeVideoHandlers() {
    document.getElementById('videoInput').addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (file) {
            const url = URL.createObjectURL(file);
            loadVideo(url);
        }
    });
}

function loadDefaultVideo() {
    loadVideo('output/videos/amar.mp4');
}

function loadVideo(url) {
    video = document.createElement('video');
    video.src = url;
    video.crossOrigin = 'anonymous';
    
    video.addEventListener('loadedmetadata', () => {
        const fps = 30;
        const duration = video.duration;
        const totalFrames = Math.floor(duration * fps);
        
        document.getElementById('fpsValue').textContent = fps;
        document.getElementById('durationValue').textContent = duration.toFixed(1);
        document.getElementById('totalFramesValue').textContent = totalFrames;
        document.getElementById('analyzeBtn').disabled = false;
        
        // Dibujar primer frame
        drawVideoFrame();
        
        updateQuality('good', 'Video Cargado', `${totalFrames} frames, ${duration.toFixed(1)}s`);
    });
    
    video.addEventListener('timeupdate', updateVideoProgress);
}

function drawVideoFrame() {
    const canvas = document.getElementById('videoCanvas');
    const ctx = canvas.getContext('2d');
    
    if (video.videoWidth > 0) {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0);
    }
}

async function analyzeVideo() {
    if (isAnalyzing) return;
    
    isAnalyzing = true;
    analysisAborted = false;
    engine.reset();
    
    document.getElementById('analyzeBtn').style.display = 'none';
    document.getElementById('stopBtn').style.display = 'block';
    
    const fps = 30;
    const duration = video.duration;
    const frameInterval = 1 / fps;
    const totalFrames = Math.floor(duration * fps);
    
    animationData = {
        name: "facial_animation",
        fps: fps,
        duration: duration,
        frames: []
    };
    
    updateQuality('medium', 'Analizando...', 'Procesando frames...');
    
    let frameCount = 0;
    let currentTime = 0;
    
    while (currentTime < duration && !analysisAborted) {
        video.currentTime = currentTime;
        await new Promise(resolve => video.onseeked = resolve);
        
        // Dibujar frame
        drawVideoFrame();
        
        // Procesar con MediaPipe
        const canvas = document.getElementById('videoCanvas');
        currentResults = null;
        await faceMesh.send({ image: canvas });
        await new Promise(resolve => setTimeout(resolve, 50));
        
        let shapeKeys = {};
        
        if (currentResults && currentResults.multiFaceLandmarks && currentResults.multiFaceLandmarks[0]) {
            shapeKeys = engine.processFrame(currentResults.multiFaceLandmarks[0]);
            
            // Actualizar UI en tiempo real
            updateShapeKeysUI(shapeKeys);
            applyShapeKeysTo3D(shapeKeys);
        }
        
        animationData.frames.push({
            frame: frameCount,
            time: currentTime,
            shape_keys: shapeKeys || {}
        });
        
        frameCount++;
        currentTime += frameInterval;
        
        // Actualizar progreso
        const progress = (frameCount / totalFrames * 100);
        document.getElementById('videoProgress').style.width = progress + '%';
        document.getElementById('framesProcessed').textContent = frameCount;
    }
    
    isAnalyzing = false;
    document.getElementById('stopBtn').style.display = 'none';
    document.getElementById('analyzeBtn').style.display = 'block';
    document.getElementById('syncBtn').disabled = false;
    document.getElementById('exportBtn').disabled = false;
    
    if (analysisAborted) {
        updateQuality('bad', 'Análisis Detenido', 'Proceso cancelado por el usuario');
    } else {
        updateQuality('good', 'Análisis Completo', `${frameCount} frames procesados`);
    }
}

function stopAnalysis() {
    analysisAborted = true;
}

function toggleSync() {
    isSyncing = !isSyncing;
    
    if (isSyncing) {
        document.getElementById('syncBtn').textContent = '⏸️ Pausar Sync';
        syncLoop();
    } else {
        document.getElementById('syncBtn').textContent = '🔄 Sincronizar';
    }
}

function syncLoop() {
    if (!isSyncing || !animationData) return;
    
    const currentTime = video.currentTime;
    const fps = animationData.fps;
    const frameIndex = Math.floor(currentTime * fps);
    
    if (frameIndex < animationData.frames.length) {
        const frame = animationData.frames[frameIndex];
        updateShapeKeysUI(frame.shape_keys);
        applyShapeKeysTo3D(frame.shape_keys);
    }
    
    requestAnimationFrame(syncLoop);
}

function updateShapeKeysUI(shapeKeys) {
    for (const [key, value] of Object.entries(shapeKeys)) {
        const barEl = document.getElementById(`bar-${key}`);
        const valEl = document.getElementById(`val-${key}`);
        
        if (barEl && valEl) {
            barEl.style.width = (value * 100) + '%';
            valEl.textContent = value.toFixed(2);
            valEl.style.color = value > 0.1 ? '#38ef7d' : '#667eea';
        }
    }
}

function applyShapeKeysTo3D(shapeKeys) {
    meshesWithTargets.forEach(mesh => {
        if (mesh.morphTargetDictionary) {
            for (const [name, value] of Object.entries(shapeKeys)) {
                const idx = mesh.morphTargetDictionary[name];
                if (idx !== undefined) {
                    mesh.morphTargetInfluences[idx] = value;
                }
            }
        }
    });
}

function togglePlay() {
    if (video.paused) {
        video.play();
        document.getElementById('playPauseBtn').textContent = '⏸️';
    } else {
        video.pause();
        document.getElementById('playPauseBtn').textContent = '▶️';
    }
}

function seekVideo(event) {
    if (!video) return;
    
    const rect = event.target.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const percentage = x / rect.width;
    video.currentTime = percentage * video.duration;
}

function updateVideoProgress() {
    if (!video) return;
    
    const progress = (video.currentTime / video.duration) * 100;
    document.getElementById('videoProgress').style.width = progress + '%';
    
    const current = formatTime(video.currentTime);
    const total = formatTime(video.duration);
    document.getElementById('timeDisplay').textContent = `${current} / ${total}`;
}

function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

function updateQuality(level, text, subtext) {
    const dot = document.getElementById('qualityDot');
    const textEl = document.getElementById('qualityText');
    const subtextEl = document.getElementById('qualitySubtext');
    
    dot.className = `quality-dot ${level}`;
    textEl.textContent = text;
    subtextEl.textContent = subtext;
}

function exportJSON() {
    if (!animationData) {
        alert('No hay datos para exportar');
        return;
    }
    
    const blob = new Blob([JSON.stringify(animationData, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'amar_facial_animation_pro.json';
    a.click();
    
    updateQuality('good', 'JSON Exportado', 'Archivo descargado correctamente');
}
