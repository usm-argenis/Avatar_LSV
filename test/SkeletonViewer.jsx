import React from 'react';
import SignAvatar from '../frontend/src/components/SignAvatar';

function SkeletonViewer() {
  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <SignAvatar urlToSkeletonJson="/skeletons/avatar_skeleton.json" />
    </div>
  );
}

export default SkeletonViewer;