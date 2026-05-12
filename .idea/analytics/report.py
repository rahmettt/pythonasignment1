# report.py — класс Report демонстрирует АССОЦИАЦИЮ (USES-A)
# Report НЕ наследует от DataAnalyser или ResultSaver
# Он просто ХРАНИТ ссылки на них и использует их методы


class Report:
    # Отвечает за: запуск анализа + сохранение результата в одном месте
    # Это паттерн "Фасад" — один класс объединяет работу других классов

    def __init__(self, analyser, saver):
        self.analyser = analyser  # USES-A DataAnalyser (или его дочерний класс)
        self.saver = saver        # USES-A ResultSaver

    def generate(self):
        # Запускает полный цикл: анализ → вывод → сохранение
        print("Generating report...")
        self.analyser.analyse()        # запускаем анализ
        self.analyser.print_results()  # печатаем результат
        self.saver.save_json()         # сохраняем в JSON
        print("Report complete.")