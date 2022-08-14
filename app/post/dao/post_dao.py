# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class PostDAO:  # Создаём DAO для выборки конкретного поста и комментариев к нему

    def __init__(self, posts_path, comments_path):
        """
        Создаёт атрибуты posts_path, comments_path
        :param posts_path: Путь к файлу со всеми постами
        :param comments_path: Путь к файлу со всеми комментариями
        """
        self.posts_path = posts_path
        self.comments_path = comments_path

    def load_all_posts(self):
        """
        Загружает все посты
        :return: Список постов
        """
        try:
            file = open(self.posts_path, encoding="utf-8")
            all_posts = json.load(file)
        except FileNotFoundError:
            quit(f"Файл {self.posts_path} с постами для загрузки не найден")
        except JSONDecodeError:
            quit(f"Файл {self.posts_path} с постами для загрузки не удалось считать")
        else:
            file.close()
            return all_posts

    def load_all_comments(self):
        """
        Загружает все комментарии
        :return: Список комментариев
        """
        try:
            file = open(self.comments_path, encoding="utf-8")
            all_comments = json.load(file)
        except FileNotFoundError:
            quit(f"Файл {self.comments_path} с комментариями для загрузки не найден")
        except JSONDecodeError:
            quit(f"Файл {self.comments_path} с комментариями для загрузки не удалось считать")
        else:
            file.close()
            return all_comments

    def load_post_with_comments(self, post_id):
        """
        Загружает выбранный пост полностью с комментариями
        :return: Выбранный пост полностью с комментариями в формате списка
        """
        post_with_comments = []
        for i in self.load_all_posts():
            if i["pk"] == post_id:
                post_with_comments.append(i)
                break
        for i in self.load_all_comments():
                if i["post_id"] == post_id:
                    post_with_comments.append(i)
        return post_with_comments
