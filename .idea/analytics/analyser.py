# analyser.py — базовый класс DataAnalyser и дочерние классы


# =============================================================
#  БАЗОВЫЙ КЛАСС — DataAnalyser (Task 1, Practice 7)
#  Определяет общую структуру для всех анализаторов
#  Дочерние классы НАСЛЕДУЮТ от него и ПЕРЕОПРЕДЕЛЯЮТ методы
# =============================================================
class DataAnalyser:

    def __init__(self, students):
        self.students = students  # список всех студентов
        self.result = {}          # словарь с результатами анализа (заполняется в analyse())

    def analyse(self):
        # Заглушка — дочерние классы должны переопределить этот метод
        # Если вызвать напрямую на базовом классе — выведет это сообщение
        print("Not implemented — use a child class")

    def print_results(self):
        # Базовая версия: просто печатает каждый ключ-значение из self.result
        # Дочерние классы вызывают super().print_results() внутри своей версии
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        # __str__ вызывается когда делаешь print(объект)
        return f"DataAnalyser: base class, {len(self.students)} students"


# =============================================================
#  ДОЧЕРНИЙ КЛАСС — GpaAnalyser (Task 2, Practice 7) — ВАРИАНТ A
#  Наследует от DataAnalyser, переопределяет analyse() и print_results()
# =============================================================
class GpaAnalyser(DataAnalyser):

    def __init__(self, students):
        # super().__init__() — вызываем конструктор родительского класса
        # это инициализирует self.students и self.result
        super().__init__(students)

    def analyse(self):
        # Переопределяем метод родителя — здесь реальная логика анализа GPA
        gpas = []
        high_performers = 0  # счётчик студентов с GPA > 3.5

        for s in self.students:
            try:
                gpa = float(s['GPA'])
                gpas.append(gpa)
                if gpa > 3.5:
                    high_performers += 1
            except ValueError:
                # если значение GPA не конвертируется — пропускаем строку
                print(f"Warning: could not convert GPA for student {s.get('student_id', '?')} — skipping.")
                continue

        avg_gpa = round(sum(gpas) / len(gpas), 2)

        # Сохраняем результат в словарь — ResultSaver потом запишет это в JSON
        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": avg_gpa,
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high_performers
        }
        return self.result

    def print_results(self):
        # Task 3: переопределяем print_results() — добавляем заголовок и подвал
        # super().print_results() — вызываем метод РОДИТЕЛЯ, он печатает пары ключ: значение
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()  # печатает строки вида "average_gpa: 3.62"
        print("=" * 30)

    def __str__(self):
        # Переопределяем __str__ родителя — описываем именно этот класс
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


# =============================================================
#  ВТОРОЙ ДОЧЕРНИЙ КЛАСС — CountryAnalyser (для Task 5 — Polymorphism)
#  Нужен чтобы продемонстрировать полиморфизм: разные классы, одинаковый вызов
# =============================================================
class CountryAnalyser(DataAnalyser):

    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        # Считает количество студентов по каждой стране и топ-3
        country_counts = {}

        for s in self.students:
            country = s['country']
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1

        # sorted() сортирует по значению (count) в убывающем порядке
        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        self.result = {
            "analysis": "Country Analysis",
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": top_3,
            "all_countries": country_counts
        }
        return self.result

    def print_results(self):
        # Переопределяем с заголовком — та же идея что в GpaAnalyser
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)
        # Не вызываем super() здесь — словарь содержит вложенные данные,
        # поэтому печатаем вручную для красивого вывода
        print(f"total_students: {self.result['total_students']}")
        print(f"total_countries: {self.result['total_countries']}")
        print(f"top_3: {self.result['top_3']}")
        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"