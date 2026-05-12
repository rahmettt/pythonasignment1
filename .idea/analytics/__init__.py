# __init__.py — этот файл превращает папку analytics/ в Python пакет
# Когда пишешь "from analytics import FileManager" — Python смотрит сюда
# Точка перед именем файла (.file_manager) означает "из той же папки" — относительный импорт

from .file_manager import FileManager
from .data_loader import DataLoader
from .analyser import DataAnalyser
from .result_saver import ResultSaver
from .report import Report