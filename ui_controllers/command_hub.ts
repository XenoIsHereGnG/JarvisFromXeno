import { updateHardwareGauges } from './gauges_manager.js';
import { playJarvisVoice } from './audio_streamer.js';

const telemetryWs = new WebSocket(`ws://${location.host}/ws/telemetry`);
const commandWs = new WebSocket(`ws://${location.host}/ws/commands`);

telemetryWs.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateHardwareGauges(data.cpu.overall, data.ram.percent, data.disk.percent);
};

commandWs.onmessage = (event) => {
  const data = JSON.parse(event.data);
  const feed = document.getElementById("transcript-feed");
  if (feed) feed.innerText = `JARVIS: ${data.response}`;
  if (data.has_audio) playJarvisVoice();
};

export function submitCommand(text: string) {
  if (!text.trim()) return;
  commandWs.send(JSON.stringify({ prompt: text }));
}

document.getElementById("btn-submit")?.addEventListener("click", () => {
  const inp = document.getElementById("terminal-input") as HTMLInputElement;
  submitCommand(inp.value);
  inp.value = "";
});
