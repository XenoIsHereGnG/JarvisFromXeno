export interface TelemetryPayload {
  cpu: { overall: number; threads: number[]; freq_mhz: number };
  ram: { used_gb: number; total_gb: number; percent: number };
  disk: { free_gb: number; percent: number };
  nodes: Array<{ id: number; category: string; content: string }>;
}

export interface CommandPacket {
  prompt: string;
}
