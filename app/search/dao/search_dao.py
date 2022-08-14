# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class SearchDAO:  # Создаём DAO для выборки постов по ключевому слову

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

    def load_posts_by_keyword(self, keyword):
        """
        Загружает выборку постов по ключевому слову
        :param keyword: Ключевое слово для поиска в постах
        :return: Выборку постов по ключевому слову в формате списка
        """
        posts_by_keyword = []
        for i in self.load_all_posts():
            if len(posts_by_keyword) == 10:
                break
            else:
                if keyword.lower() in i["content"].lower():
                    posts_by_keyword.append(i)
        return posts_by_keyword
