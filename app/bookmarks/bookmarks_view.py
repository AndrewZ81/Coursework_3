from flask import Blueprint, render_template  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.bookmarks_dao import BookmarksDAO  # Подключаем для выборки закладок
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

all_bookmarks = BookmarksDAO(FlaskConfig.BOOKMARKS_PATH)  # Создаём объект класса

# Создаём блюпринт страницы закладок
all_bookmarks_blueprint = Blueprint("all_bookmarks_blueprint", __name__)


@all_bookmarks_blueprint.route("/bookmarks")
def show_all_bookmarks():
    """
    Создаёт эндпоинт для закладок
    :return: Заполненный шаблон закладок
    """
    _all_bookmarks = all_bookmarks.load_all_bookmarks()
    return render_template("bookmarks.html", bookmarks=_all_bookmarks)
