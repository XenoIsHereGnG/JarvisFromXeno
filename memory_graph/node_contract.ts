export interface MemoryNode {
  id: number;
  category: 'Command' | 'System' | 'Directive' | 'Insight';
  content: string;
  weight?: number;
}

export interface GraphPayload {
  nodes: MemoryNode[];
  edges: { source: number; target: number }[];
}
