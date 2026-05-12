# main.py — главный файл программы
# Здесь НЕТ определений классов — только импорты и вызовы методов
# Все классы живут в пакете analytics/

# Task 2 (Practice 8): импортируем из пакета analytics
from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser
# GpaAnalyser — наш вариант A
# CountryAnalyser — второй класс для демонстрации полиморфизма (Task 5)


def main():

    # ── Шаг 1: FileManager — проверяем файл и создаём папку ──────────────
    fm = FileManager('students.csv')
    if not fm.check_file():
        # check_file() вернул False — файла нет, останавливаем программу
        print('Stopping program.')
        exit()
    fm.create_output_folder()

    # ── Шаг 2: DataLoader — загружаем CSV и смотрим первые строки ────────
    dl = DataLoader('students.csv')
    dl.load()     # загружает все 10000 строк в dl.students
    dl.preview()  # печатает первые 5

    # ── Шаг 3: Lambda / Map / Filter (из Practice 5) ─────────────────────
    students = dl.students

    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)

    # filter() оставляет только студентов у которых GPA > 3.8
    # lambda s: ... — анонимная функция, s — один студент (словарь)
    high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, students))
    print(f"GPA > 3.8 : {len(high_gpa)}")

    # map() применяет функцию к каждому элементу и возвращает новый список
    # здесь: извлекаем GPA каждого студента как число
    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print(f"GPA values (first 5) : {gpa_values[:5]}")

    # ещё один filter — студенты с study_hours > 4 часов в день
    hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, students))
    print(f"study_hours_per_day > 4 : {len(hard_workers)}")
    print("-" * 30)

    # ── Шаг 4: Демо обработки ошибок — намеренно неверный файл ───────────
    dl_bad = DataLoader('wrong_file.csv')
    dl_bad.load()
    # программа НЕ упадёт — ошибка поймается в except внутри DataLoader.load()

    # ── Шаг 5: Polymorphism — Task 5, Practice 7 ─────────────────────────
    # Создаём список из двух разных анализаторов
    # for loop вызывает одинаковые методы (.analyse(), .print_results()) на обоих
    # но поведение разное — это и есть полиморфизм
    analysers = [
        GpaAnalyser(dl.students),       # наш основной вариант A
        CountryAnalyser(dl.students),   # второй класс для демонстрации
    ]

    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)

    for a in analysers:
        print(a)          # вызывает __str__() каждого объекта
        a.analyse()       # каждый класс делает своё — GpaAnalyser считает GPA, CountryAnalyser считает страны
        a.print_results() # каждый класс печатает по-своему

    # ── Шаг 6: Report — Task 4, Practice 7 (Association) ─────────────────
    # Report ИСПОЛЬЗУЕТ GpaAnalyser и ResultSaver (не наследует — ассоциация)
    # saver ссылается на result первого анализатора (GpaAnalyser)
    saver = ResultSaver(analysers[0].result, 'output/result.json')
    report = Report(analysers[0], saver)
    report.generate()
    # generate() внутри вызывает: analyse() → print_results() → save_json()


if __name__ == '__main__':
    main()