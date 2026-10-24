class TacticalIntentClassifier:
    AGENTS_MAP = {
        "Coding Agent": ["codice", "script", "python", "errore", "programma", "debug", "file"],
        "Browser Agent": ["cerca", "google", "chrome", "web", "sito", "youtube", "internet"],
        "System Agent": ["apri", "chiudi", "volume", "schermo", "mouse", "scrivi", "blocca", "processi"],
        "Research Agent": ["analizza", "spiega", "guarda", "visione", "cosa", "perché", "riassumi"],
        "Memory Agent": ["ricorda", "memoria", "salva", "nota", "database"]
    }

    @classmethod
    def classify(cls, prompt: str) -> dict:
        p_low = prompt.lower()
        scores = {agent: 0.15 for agent in cls.AGENTS_MAP}
        for agent, keywords in cls.AGENTS_MAP.items():
            for kw in keywords:
                if kw in p_low:
                    scores[agent] += 0.35
        best_agent = max(scores, key=scores.get)
        confidence = min(0.99, scores[best_agent])
        return {"agent": best_agent, "confidence": round(confidence * 100, 1), "distribution": scores}
