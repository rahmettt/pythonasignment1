import csv  # для чтения CSV файла


class DataLoader:
    # Отвечает ТОЛЬКО за: загрузку данных из CSV и предпросмотр первых строк

    def __init__(self, filename):
        self.filename = filename
        self.students = []  # сюда загрузим всех студентов как список словарей

    def load(self):
        # Открывает CSV, каждая строка становится словарём {'student_id': ..., 'GPA': ..., ...}
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            # Файл не найден — печатаем ошибку и не падаем
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
        except Exception as e:
            print(f"Error: {e}")
        return self.students

    def preview(self, n=5):
        # Печатает первые n строк (по умолчанию 5)
        print(f"First {n} rows:")
        print("-" * 30)
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 30)