# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class AllPostsDAO:  # Создаём DAO для выборки всех постов

    def __init__(self, path):
        """
        Создаёт атрибут path
        :param path: Путь к файлу со всеми постами
        """
        self.path = path

    def load_all_posts(self):
        """
        Загружает все посты
        :return: Список постов
        """
        try:
            file = open(self.path, encoding="utf-8")
            all_posts = json.load(file)
        except FileNotFoundError:
            quit(f"Файл {self.path} с постами для загрузки не найден")
        except JSONDecodeError:
            quit(f"Файл {self.path} с постами для загрузки не удалось считать")
        else:
            file.close()
            return all_posts
