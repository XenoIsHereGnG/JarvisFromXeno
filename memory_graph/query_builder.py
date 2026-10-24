class MemoryQueryBuilder:
    @staticmethod
    def insert_record(category: str, content: str) -> tuple:
        return ("INSERT INTO memories (source, category, content) VALUES ('Agent', ?, ?)", (category, content))
