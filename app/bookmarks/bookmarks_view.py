from flask import Blueprint, render_template  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.bookmarks_dao import BookmarksDAO  # Подключаем для выборки закладок
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

bookmarks = BookmarksDAO(FlaskConfig.BOOKMARKS_PATH)  # Создаём объект класса

# Создаём блюпринт для работы с закладками
bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, url_prefix="/bookmarks")


@bookmarks_blueprint.route("/")
def show_all_bookmarks():
    """
    Создаёт эндпоинт для отображения закладок
    :return: Заполненный шаблон закладок
    """
    all_bookmarks = bookmarks.load_all_bookmarks()
    return render_template("bookmarks.html", bookmarks=all_bookmarks)
