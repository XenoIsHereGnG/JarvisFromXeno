export function cleanResponseForSpeech(rawMarkdown) {
  return rawMarkdown
    .replace(/[#*_~`]/g, '')
    .replace(/\[.*?\]\(.*?\)/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}
