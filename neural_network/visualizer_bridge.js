window.drawNeuralNetworkHUD = function(canvasId, nnData) {
  const canvas = document.getElementById(canvasId);
  if (!canvas || !nnData || !nnData.layers) return;
  const ctx = canvas.getContext("2d");
  const w = (canvas.width = canvas.clientWidth);
  const h = (canvas.height = canvas.clientHeight);
  ctx.clearRect(0, 0, w, h);

  const layers = [nnData.layers.input, nnData.layers.hidden1, nnData.layers.hidden2, nnData.layers.output];
  const layerX = [w * 0.1, w * 0.38, w * 0.68, w * 0.9];
  const coords = [];

  layers.forEach((layer, lIdx) => {
    const col = [];
    const stepY = h / (layer.length + 1);
    layer.forEach((val, nIdx) => {
      col.push({ x: layerX[lIdx], y: stepY * (nIdx + 1), val: val });
    });
    coords.push(col);
  });

  // Sinapsi pulsanti
  for (let l = 0; l < coords.length - 1; l++) {
    coords[l].forEach(src => {
      coords[l + 1].forEach(dst => {
        const alpha = Math.min(0.85, (src.val + dst.val) * 0.35);
        ctx.strokeStyle = `rgba(0, 229, 255, ${alpha})`;
        ctx.lineWidth = alpha * 1.8;
        ctx.beginPath();
        ctx.moveTo(src.x, src.y);
        ctx.lineTo(dst.x, dst.y);
        ctx.stroke();
      });
    });
  }

  // Neuroni
  coords.forEach((col, lIdx) => {
    col.forEach(node => {
      const radius = lIdx === 3 ? 6 : 4.2;
      ctx.fillStyle = node.val > 0.6 ? "#00ffaa" : "#00e5ff";
      ctx.shadowColor = ctx.fillStyle;
      ctx.shadowBlur = 10 * node.val;
      ctx.beginPath();
      ctx.arc(node.x, node.y, radius, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;
    });
  });
};
