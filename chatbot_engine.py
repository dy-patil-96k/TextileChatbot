import json
import math
import re
from pathlib import Path
from typing import Dict, List


class TextileChatbot:
    def __init__(self, knowledge_path: str):
        path = Path(knowledge_path)
        with path.open("r", encoding="utf-8") as f:
            self.knowledge: List[Dict[str, str]] = json.load(f)

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        return re.findall(r"[a-zA-Z]+", text.lower())

    def _vectorize(self, text: str) -> Dict[str, float]:
        words = self._tokenize(text)
        counts: Dict[str, float] = {}
        for w in words:
            counts[w] = counts.get(w, 0.0) + 1.0
        return counts

    @staticmethod
    def _cosine_similarity(v1: Dict[str, float], v2: Dict[str, float]) -> float:
        if not v1 or not v2:
            return 0.0

        dot = 0.0
        for key, val in v1.items():
            dot += val * v2.get(key, 0.0)

        norm1 = math.sqrt(sum(x * x for x in v1.values()))
        norm2 = math.sqrt(sum(x * x for x in v2.values()))
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return dot / (norm1 * norm2)

    def get_reply(self, user_message: str) -> str:
        user_vec = self._vectorize(user_message)

        best_score = 0.0
        best_answer = None
        for item in self.knowledge:
            q_vec = self._vectorize(item["question"])
            score = self._cosine_similarity(user_vec, q_vec)
            if score > best_score:
                best_score = score
                best_answer = item["answer"]

        if best_answer and best_score >= 0.2:
            return best_answer

        return (
            "I can help with textile topics like fabric types, GSM, weaving, "
            "dyeing, shrinkage, and care instructions. Please ask a specific question."
        )
