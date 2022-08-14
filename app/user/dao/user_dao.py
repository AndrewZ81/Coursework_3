# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class UserDAO:  # Создаём DAO для выборки постов данного пользователя

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
            raise FileNotFoundError(f"Файл {self.path} с постами для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.path} с постами для загрузки не удалось считать")
        else:
            file.close()
            return all_posts

    def load_posts_by_user(self, name):
        """
        Загружает выборку постов данного пользователя
        :param name: Ключевое слово для поиска имени пользователя
        :return: Выборку постов данного пользователя в формате списка
        """
        posts_by_user = []
        for i in self.load_all_posts():
            if i["poster_name"].lower() == name.lower():
                posts_by_user.append(i)

        # Обрабатываем ошибку, когда не существует постов данного пользователя
        try:
            if not len(posts_by_user):
                raise ValueError("Не существует постов данного пользователя")
        except ValueError:
            raise
        else:
            return posts_by_user
