from flask import Blueprint, render_template  # Подключаем для создания блюпринтов на основе шаблонов
from .dao.all_posts_dao import AllPostsDAO  # Подключаем для выборки всех постов
from config import FlaskConfig  # Подключаем для доступа к конфигурационным константам

all_posts = AllPostsDAO(FlaskConfig.POSTS_PATH)  # Создаём объект класса

# Создаём блюпринт главной страницы (далее - ленты)
all_posts_blueprint = Blueprint("all_posts_blueprint", __name__)


@all_posts_blueprint.route("/")
def show_all_posts():
    """
    Создаёт эндпоинт для ленты
    :return: Заполненный шаблон ленты
    """
    _all_posts = all_posts.load_all_posts()
    return render_template("index.html", posts=_all_posts)
