export function renderMemoryNodes(canvasId: string, nodes: Array<{ id: number; category: string }>) {
  const canvas = document.getElementById(canvasId) as HTMLCanvasElement;
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.strokeStyle = 'rgba(0, 229, 255, 0.2)';

  nodes.forEach((node, i) => {
    const x = (i * 24 + 10) % canvas.width;
    const y = ((i * 17 + 20) % (canvas.height - 20)) + 10;
    ctx.fillStyle = node.category === 'Directive' ? '#00ffaa' : '#00e5ff';
    ctx.beginPath();
    ctx.arc(x, y, 3, 0, Math.PI * 2);
    ctx.fill();
  });
}
