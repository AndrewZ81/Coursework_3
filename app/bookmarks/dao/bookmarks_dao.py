# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


class BookmarksDAO:  # Создаём DAO для работы с закладками

    def __init__(self, posts_path, bookmarks_path):
        """
        Создаёт атрибуты posts_path, bookmarks_path
        :param posts_path: Путь к файлу с лентой
        :param bookmarks_path: Путь к файлу с закладками
        """
        self.posts_path = posts_path
        self.bookmarks_path = bookmarks_path

    def load_all_posts(self):
        """
        Загружает все посты
        :return: Список постов
        """
        try:
            file = open(self.posts_path, encoding="utf-8")
            all_posts = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.posts_path} с постами для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.posts_path} с постами для загрузки не удалось считать")
        else:
            file.close()
            return all_posts

    def load_post_by_id(self, post_id):
        """
        Загружает пост по идентификатору
        :param post_id: Идентификатор поста для поиска
        :return: Пост в формате словаря
        """
        post_by_id = {}
        for i in self.load_all_posts():
            if i["pk"] == post_id:
                post_by_id.update(i)
                break

        # Обрабатываем ошибку, когда не существует постов с данным идентификатором
        try:
            if not len(post_by_id):
                raise ValueError("Не существует постов с данным идентификатором")
        except ValueError:
            raise
        else:
            return post_by_id

    def load_all_bookmarks(self):
        """
        Загружает все закладки
        :return: Список закладок
        """
        try:
            file = open(self.bookmarks_path, encoding="utf-8")
            all_bookmarks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.bookmarks_path} с закладками для загрузки не найден")
        except JSONDecodeError:
            raise ValueError(f"Файл {self.bookmarks_path} с закладками для загрузки не удалось считать")
        else:
            file.close()
            return all_bookmarks

    def add_bookmark(self, post_id):
        """
        Добавляет пост в закладки
        :param post_id: Идентификатор поста для добавления в закладки
        :return: Сохраненный файл с закладками формата JSON после добавления закладки
        """
        bookmarks = self.load_all_bookmarks()
        new_bookmark = self.load_post_by_id(post_id)
        if new_bookmark not in bookmarks:
            bookmarks.append(new_bookmark)
            file = open(self.bookmarks_path, "w", encoding="utf-8")
            return json.dump(bookmarks, file, indent=2, ensure_ascii=False)
