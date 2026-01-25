import React, { useRef, useEffect, useState, useMemo } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import * as THREE from "three";

function SkeletonMesh({ skeletonJson, scale=1.0 }) {
  const groupRef = useRef();
  const [timeIdx, setTimeIdx] = useState(0);
  const fps = skeletonJson?.fps || 30;
  const frames = skeletonJson?.frames || [];
  const bones = skeletonJson?.bones || [];
  const interval = 1 / fps;

  // Prepare refs for spheres and lines
  const jointRefs = useMemo(() => bones.map(() => React.createRef()), [bones]);
  const lineRefs = useMemo(() => bones.map(() => React.createRef()), [bones]);

  // Helper to set mesh position
  useEffect(() => {
    if (!frames.length) return;
    // set initial frame
    const pos0 = frames[0].positions;
    for (let i = 0; i < pos0.length; i++) {
      const r = jointRefs[i].current;
      if (r) r.position.set(pos0[i][0]*scale, pos0[i][1]*scale, pos0[i][2]*scale);
    }
  }, [skeletonJson]);

  // Animation loop: advances frames based on time
  useFrame((state, delta) => {
    if (!frames.length) return;
    // compute current frame index from elapsed time
    const t = state.clock.getElapsedTime();
    const idx = Math.floor(t * fps) % frames.length;
    const frame = frames[idx];
    for (let i = 0; i < frame.positions.length; i++) {
      const p = frame.positions[i];
      const r = jointRefs[i].current;
      if (r) {
        r.position.x = p[0]*scale;
        r.position.y = p[1]*scale;
        r.position.z = p[2]*scale;
      }
    }
    // update lines between parent-child
    for (let i = 0; i < bones.length; i++) {
      const parent = bones[i].parent;
      if (parent >= 0) {
        const a = jointRefs[parent].current;
        const b = jointRefs[i].current;
        const line = lineRefs[i].current;
        if (a && b && line) {
          const positions = line.geometry.attributes.position.array;
          positions[0] = a.position.x; positions[1] = a.position.y; positions[2] = a.position.z;
          positions[3] = b.position.x; positions[4] = b.position.y; positions[5] = b.position.z;
          line.geometry.attributes.position.needsUpdate = true;
          line.geometry.computeBoundingSphere();
        }
      }
    }
  });

  return (
    <group ref={groupRef}>
      {bones.map((b, i) => (
        <group key={i}>
          <mesh ref={jointRefs[i]}>
            <sphereGeometry args={[0.02, 8, 8]} />
            <meshStandardMaterial emissive={new THREE.Color(i===0?0x00ff00:0x0044ff)} />
          </mesh>
          {b.parent >= 0 ? (
            <line key={"line"+i} ref={lineRefs[i]}>
              <bufferGeometry>
                <bufferAttribute attachObject={['attributes','position']} count={2} array={new Float32Array(6)} itemSize={3} />
              </bufferGeometry>
              <lineBasicMaterial linewidth={2} />
            </line>
          ) : null}
        </group>
      ))}
    </group>
  );
}

export default function SignAvatar({ skeletonPath, scale = 1.0 }) {
  const [skeleton, setSkeleton] = useState(null);

  useEffect(() => {
    if (!skeletonPath) return;
    fetch(skeletonPath)
      .then(r => r.json())
      .then(j => {
        console.log("Loaded skeleton:", j);  // Debug log
        setSkeleton(j);
      })
      .catch(err => console.error("Error loading skeleton:", err));
  }, [skeletonPath]);

  return skeleton ? (
    <group>
      <SkeletonMesh skeletonJson={skeleton} scale={scale} />
      <gridHelper args={[10, 10]} />
      <axesHelper args={[5]} />
      <ambientLight intensity={0.8} />
      <directionalLight position={[3, 5, 2]} intensity={0.8} />
    </group>
  ) : null;
}
