import json  # для записи словаря Python в JSON формат


class ResultSaver:
    # Отвечает ТОЛЬКО за: сохранение результата анализа в JSON файл

    def __init__(self, result, output_path):
        self.result = result            # словарь с результатами (от DataAnalyser)
        self.output_path = output_path  # путь к файлу, например 'output/result.json'

    def save_json(self):
        # Записывает self.result в файл как JSON с отступами
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
                # indent=4 — красивые отступы в 4 пробела для читаемости файла
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")