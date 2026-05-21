"""
Бизнес-логика приложения.

Содержит логику обработки данных о подшипниках:
- Поиск и фильтрация
- Расчеты характеристик
- Определение аналогов
- Валидация данных
"""

import json
import os
from collections import Counter, defaultdict
from datetime import datetime


class AutocompleteEngine:
    """Движок автодополнения поисковых запросов"""

    def __init__(self, dict_path: str = "data/autocomplete_dict.json"):
        self.dict_path = dict_path
        self.terms = []
        self.index = {}
        self.metadata = {}
        self._terms_by_value: dict[str, dict] = {}
        self.load_dictionary(dict_path)

    def load_dictionary(self, dict_path: str):
        """Загрузить словарь автодополнения"""
        if not os.path.exists(dict_path):
            print(f"Словарь автодополнения не найден: {dict_path}")
            return

        try:
            with open(dict_path, encoding="utf-8") as f:
                data = json.load(f)
                self.terms = data.get("terms", [])
                self.index = data.get("index", {})
                self.metadata = data.get("metadata", {})
                self._terms_by_value = {t["value"]: t for t in self.terms}
        except Exception as e:
            print(f"Ошибка при загрузке словаря: {e}")

    def suggest(self, prefix: str, limit: int = 10, types: list[str] = None) -> list[dict]:
        """
        Генерировать предложения по префиксу

        Алгоритм:
        1. Нормализовать запрос (lowercase, удалить спецсимволы)
        2. Найти в префиксном дереве
        3. Отсортировать по частотности
        4. Применить фильтры по типу
        5. Вернуть top-N результатов
        """
        if not prefix or len(prefix) < 1:
            return []

        # Нормализация запроса
        normalized_prefix = prefix.lower().strip()

        # Поиск в индексе
        candidates = self.index.get(normalized_prefix, [])

        # Если не найдено в индексе, ищем в полном списке терминов
        if not candidates:
            candidates = []
            for term in self.terms:
                if term["value"].lower().startswith(normalized_prefix):
                    candidates.append(term["value"])

        # Получаем полную информацию о кандидатах
        suggestions = []
        for candidate in candidates[: limit * 2]:  # Берем больше для фильтрации
            term_info = self._terms_by_value.get(candidate)
            if term_info:
                # Фильтр по типу
                if types and term_info["type"] not in types:
                    continue

                # Подсветка совпадения
                highlighted = self._highlight_match(term_info["value"], prefix)

                suggestions.append(
                    {
                        "value": term_info["value"],
                        "type": term_info["type"],
                        "frequency": term_info["frequency"],
                        "highlight": highlighted,
                    }
                )

        # Сортировка по частотности
        suggestions.sort(key=lambda x: x["frequency"], reverse=True)

        return suggestions[:limit]

    def _highlight_match(self, value: str, prefix: str) -> str:
        """Подсветка совпадающей части"""
        if not prefix:
            return value

        # Находим позицию совпадения (регистронезависимо)
        value_lower = value.lower()
        prefix_lower = prefix.lower()

        pos = value_lower.find(prefix_lower)
        if pos == -1:
            return value

        # Создаем подсвеченную версию
        highlighted = value[:pos] + "<b>" + value[pos : pos + len(prefix)] + "</b>" + value[pos + len(prefix) :]

        return highlighted

    def get_popular_searches(self, limit: int = 10) -> list[dict]:
        """Получить самые популярные поисковые запросы"""
        # Сортируем по частотности
        sorted_terms = sorted(self.terms, key=lambda x: x["frequency"], reverse=True)

        # Возвращаем топ-N
        return sorted_terms[:limit]


class DocumentSearchEngine:
    """Движок поиска документов"""

    def __init__(
        self, index_path: str = "data/document_index.json", similarity_path: str = "data/similarity_matrix.json"
    ):
        self.index_path = index_path
        self.similarity_path = similarity_path
        self.documents = {}
        self.similarity_matrix = {}
        self.load_data()

    def load_data(self):
        """Загрузить индекс документов и матрицу схожести"""
        # Загрузка индекса документов
        if os.path.exists(self.index_path):
            try:
                with open(self.index_path, encoding="utf-8") as f:
                    self.documents = json.load(f)
            except Exception as e:
                print(f"Ошибка при загрузке индекса документов: {e}")

        # Загрузка матрицы схожести
        if os.path.exists(self.similarity_path):
            try:
                with open(self.similarity_path, encoding="utf-8") as f:
                    self.similarity_matrix = json.load(f)
            except Exception as e:
                print(f"Ошибка при загрузке матрицы схожести: {e}")

    def search(self, query: str, limit: int = 20) -> list[dict]:
        """
        Простой поиск по документам

        В реальной системе здесь должен быть полнотекстовый поиск
        (Elasticsearch, PostgreSQL Full-Text Search, etc.)
        """
        if not query:
            return []

        query_lower = query.lower()
        results = []

        for doc_id, doc in self.documents.items():
            # Простой поиск по названию и описанию
            if query_lower in doc["title"].lower() or query_lower in doc.get("excerpt", "").lower():

                # Вычисление релевантности (упрощенно)
                relevance = 0.5
                if query_lower in doc["title"].lower():
                    relevance += 0.5

                results.append(
                    {
                        "id": doc_id,
                        "title": doc["title"],
                        "path": doc["path"],
                        "excerpt": doc.get("excerpt", ""),
                        "relevance": relevance,
                    }
                )

        # Сортировка по релевантности
        results.sort(key=lambda x: x["relevance"], reverse=True)

        return results[:limit]

    def get_similar_documents(self, document_id: str, limit: int = 5) -> list[dict]:
        """Получить похожие документы для конкретного документа"""
        if document_id not in self.similarity_matrix:
            return []

        similar = self.similarity_matrix[document_id].get("similar", [])

        # Дополняем информацией из индекса
        result = []
        for sim_doc in similar[:limit]:
            doc_id = sim_doc["doc_id"]
            if doc_id in self.documents:
                result.append(
                    {
                        "id": doc_id,
                        "title": sim_doc.get("title", self.documents[doc_id]["title"]),
                        "path": self.documents[doc_id]["path"],
                        "similarity": sim_doc["score"],
                    }
                )

        return result


class SearchHistory:
    """Управление историей поиска (заглушка для работы без БД)"""

    def __init__(self):
        # Per-user lists for O(1) reads; flat _all list for O(1) global analytics
        self._by_user: defaultdict[str, list[dict]] = defaultdict(list)
        self._all: list[dict] = []

    @property
    def history(self) -> list[dict]:
        """Flat list of all entries; O(1) — backed by a maintained list."""
        return self._all

    def add_search(self, user_id: str, query: str, results_count: int, session_id: str = None):
        """Добавить запись в историю поиска"""
        entry = {
            "user_id": user_id,
            "query": query,
            "results_count": results_count,
            "session_id": session_id,
            "timestamp": datetime.now().isoformat(),
        }
        self._by_user[user_id].append(entry)
        self._all.append(entry)

    def get_user_history(self, user_id: str, limit: int = 50) -> list[dict]:
        """Получить историю поиска пользователя"""
        entries = sorted(self._by_user[user_id], key=lambda x: x["timestamp"], reverse=True)
        return entries[:limit]

    def clear_user_history(self, user_id: str):
        """Очистить историю поиска пользователя"""
        if user_id in self._by_user:
            removed_ids = {id(e) for e in self._by_user.pop(user_id)}
            self._all = [e for e in self._all if id(e) not in removed_ids]

    def get_popular_queries(self, limit: int = 10) -> list[dict]:
        """Получить популярные поисковые запросы"""
        return [{"query": q, "count": c} for q, c in Counter(h["query"] for h in self._all).most_common(limit)]
