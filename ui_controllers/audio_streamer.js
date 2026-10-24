export function playJarvisVoice() {
  const audio = new Audio(`/ui_layout/speech.mp3?t=${Date.now()}`);
  audio.play().catch(e => console.warn("Audio waiting for user gesture:", e));
}
