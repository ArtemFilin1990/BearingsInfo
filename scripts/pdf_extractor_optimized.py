#!/usr/bin/env python3
"""
Оптимизированный скрипт для извлечения данных из PDF-файлов и сохранения в SQLite.

Возможности:
- Параллельная обработка PDF файлов через ThreadPoolExecutor
- Логирование всех ошибок в parser_errors.log
- Извлечение данных по регулярному выражению
- Сохранение в SQLite БД (таблица extracted_data)
- Обработка повреждённых PDF с пропуском
"""

import sqlite3
import re
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import sys

try:
    import PyPDF2
except ImportError:
    print("Ошибка: Требуется установка PyPDF2")
    print("Установите: pip install PyPDF2")
    sys.exit(1)

# Настройка логирования
logging.basicConfig(
    filename="parser_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Оптимизированное регулярное выражение для поиска обозначений подшипников
# Группировка альтернатив, избегание жадных квантификаторов
BEARING_PATTERN = re.compile(
    r"\b(?:"
    r"(?:\d{1,2})\s?(?:0{2,3}|1{2,3}|2{2,3}|3{2,3})\s?(?:[0-9]{2,4})"  # ГОСТ формат
    r"|"
    r"(?:[67]\d{3}(?:ZZ|RS|2RS)?)"  # ISO формат с уплотнениями
    r"|"
    r"(?:N[UJKP]?\d{3,4}[A-Z]*)"  # SKF/FAG формат
    r")\b",
    re.IGNORECASE,
)


class PDFExtractor:
    """Класс для извлечения данных из PDF файлов в SQLite."""

    def __init__(self, pdf_folder: str, db_path: str = "bearings_data.db"):
        """
        Инициализация экстрактора.

        Args:
            pdf_folder: Путь к папке с PDF файлами
            db_path: Путь к файлу SQLite БД
        """
        self.pdf_folder = Path(pdf_folder)
        self.db_path = db_path

        if not self.pdf_folder.exists():
            error_msg = f"Критическая ошибка: Папка не найдена - {self.pdf_folder}"
            logging.critical(error_msg)
            print(error_msg)
            sys.exit(1)

        if not self.pdf_folder.is_dir():
            error_msg = f"Критическая ошибка: Указанный путь не является папкой - {self.pdf_folder}"
            logging.critical(error_msg)
            print(error_msg)
            sys.exit(1)

        self._init_database()

    def _init_database(self):
        """Создание БД и таблицы, если их нет."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS extracted_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT NOT NULL,
                    page_number INTEGER NOT NULL,
                    extracted_value TEXT NOT NULL,
                    extraction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(filename, page_number, extracted_value)
                )
            """
            )

            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_filename 
                ON extracted_data(filename)
            """
            )

            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            error_msg = f"Критическая ошибка БД: {e}"
            logging.critical(error_msg)
            print(error_msg)
            sys.exit(1)

    def _extract_from_pdf(self, pdf_path: Path) -> list:
        """
        Извлечение данных из одного PDF файла.

        Args:
            pdf_path: Путь к PDF файлу

        Returns:
            list: Список кортежей (filename, page_number, extracted_value)
        """
        results = []
        filename = pdf_path.name

        try:
            with open(pdf_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                total_pages = len(pdf_reader.pages)

                for page_num in range(total_pages):
                    try:
                        page = pdf_reader.pages[page_num]
                        text = page.extract_text()

                        if text:
                            # Поиск всех совпадений с паттерном
                            matches = BEARING_PATTERN.findall(text)

                            for match in matches:
                                # Нормализация (удаление лишних пробелов)
                                normalized = re.sub(r"\s+", "", match)
                                results.append((filename, page_num + 1, normalized))

                    except Exception as e:
                        logging.error(f"Ошибка на странице {page_num + 1} файла {filename}: {e}")
                        continue

        except PyPDF2.errors.PdfReadError as e:
            logging.error(f"Повреждённый PDF файл {filename}: {e}")
            print(f"⚠ Пропущен повреждённый файл: {filename}")

        except Exception as e:
            logging.error(f"Ошибка обработки файла {filename}: {e}")

        return results

    def _save_to_database(self, data: list):
        """
        Сохранение данных в БД.

        Args:
            data: Список кортежей (filename, page_number, extracted_value)
        """
        if not data:
            return

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Параметризованный запрос для защиты от SQL-инъекций
            cursor.executemany(
                """INSERT OR IGNORE INTO extracted_data 
                   (filename, page_number, extracted_value) 
                   VALUES (?, ?, ?)""",
                data,
            )

            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            logging.error(f"Ошибка сохранения в БД: {e}")

    def process_all_pdfs(self, max_workers: int = 4):
        """
        Параллельная обработка всех PDF файлов в папке.

        Args:
            max_workers: Максимальное количество потоков
        """
        pdf_files = list(self.pdf_folder.glob("**/*.pdf"))

        if not pdf_files:
            print(f"⚠ PDF файлы не найдены в {self.pdf_folder}")
            return

        print(f"Найдено PDF файлов: {len(pdf_files)}")
        print(f"Начало обработки с {max_workers} потоками...\n")

        processed = 0
        total_records = 0

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Запуск параллельной обработки
            future_to_pdf = {executor.submit(self._extract_from_pdf, pdf): pdf for pdf in pdf_files}

            for future in as_completed(future_to_pdf):
                pdf_path = future_to_pdf[future]
                try:
                    data = future.result()

                    if data:
                        self._save_to_database(data)
                        total_records += len(data)
                        print(f"✓ {pdf_path.name}: извлечено {len(data)} записей")
                    else:
                        print(f"○ {pdf_path.name}: данные не найдены")

                    processed += 1

                except Exception as e:
                    logging.error(f"Ошибка обработки {pdf_path.name}: {e}")
                    print(f"✗ {pdf_path.name}: ошибка обработки")

        print(f"\n{'='*60}")
        print(f"Обработка завершена!")
        print(f"Обработано файлов: {processed}/{len(pdf_files)}")
        print(f"Извлечено записей: {total_records}")
        print(f"База данных: {self.db_path}")
        print(f"Лог ошибок: parser_errors.log")
        print(f"{'='*60}")

    def get_statistics(self):
        """Вывод статистики из БД."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM extracted_data")
            total = cursor.fetchone()[0]

            cursor.execute(
                """
                SELECT filename, COUNT(*) as count 
                FROM extracted_data 
                GROUP BY filename 
                ORDER BY count DESC 
                LIMIT 10
            """
            )
            top_files = cursor.fetchall()

            conn.close()

            print(f"\n{'='*60}")
            print("СТАТИСТИКА БАЗЫ ДАННЫХ")
            print(f"{'='*60}")
            print(f"Всего записей: {total}")
            print(f"\nТоп-10 файлов по количеству извлечённых данных:")
            for filename, count in top_files:
                print(f"  {filename}: {count} записей")
            print(f"{'='*60}\n")

        except sqlite3.Error as e:
            logging.error(f"Ошибка получения статистики: {e}")


def main():
    """Основная функция."""
    # Настройка путей
    pdf_folder = Path(__file__).parent.parent / "docs" / "gost"
    db_path = "bearings_data.db"

    # Создание экстрактора
    extractor = PDFExtractor(str(pdf_folder), db_path)

    # Обработка всех PDF (4 потока для оптимальной производительности)
    extractor.process_all_pdfs(max_workers=4)

    # Вывод статистики
    extractor.get_statistics()


if __name__ == "__main__":
    main()
