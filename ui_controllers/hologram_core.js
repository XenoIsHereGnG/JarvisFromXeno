(function initThreeHolo() {
  const container = document.getElementById("holo-canvas-wrapper");
  if (!container) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
  camera.position.z = 5.5;

  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
  renderer.setSize(container.clientWidth, container.clientHeight);
  container.appendChild(renderer.domElement);

  const sphereGeo = new THREE.SphereGeometry(1.8, 22, 22);
  const wireMat = new THREE.MeshBasicMaterial({ color: 0x00e5ff, wireframe: true, transparent: true, opacity: 0.35 });
  const globe = new THREE.Mesh(sphereGeo, wireMat);
  scene.add(globe);

  const ringGeo = new THREE.RingGeometry(2.3, 2.35, 64);
  const ringMat = new THREE.MeshBasicMaterial({ color: 0x0088ff, side: THREE.DoubleSide });
  const ring = new THREE.Mesh(ringGeo, ringMat);
  ring.rotation.x = Math.PI / 2.2;
  scene.add(ring);

  function loop() {
    requestAnimationFrame(loop);
    globe.rotation.y += 0.002;
    ring.rotation.z += 0.003;
    renderer.render(scene, camera);
  }
  loop();
})();
