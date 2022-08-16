# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class BookmarksDAO:  # Создаём DAO для выборки закладок

    def __init__(self, path):
        """
        Создаёт атрибут path
        :param path: Путь к файлу с закладками
        """
        self.path = path

    def load_all_bookmarks(self):
        """
        Загружает все закладки
        :return: Список закладок
        """
        try:
            file = open(self.path, encoding="utf-8")
            all_bookmarks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.path} с закладками для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.path} с закладками для загрузки не удалось считать")
        else:
            file.close()
            return all_bookmarks
