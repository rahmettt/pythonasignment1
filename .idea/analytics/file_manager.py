import os  # нужен для проверки файлов и создания папок


class FileManager:
    # Отвечает ТОЛЬКО за: проверку CSV файла и создание папки output/

    def __init__(self, filename):
        # сохраняем имя файла внутри объекта
        self.filename = filename

    def check_file(self):
        # Проверяет существует ли файл на диске
        # Возвращает True если есть, False если нет
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder='output'):
        # Создаёт папку output/ если её ещё нет
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")