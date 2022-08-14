from flask import Flask  # Подключаем необходимые инструменты из модуля flask
from config import FlaskConfig  # Подключаем конфигурационный класс
from app.main.all_posts_views import all_posts_blueprint  # Подключаем блюпринт для вывода ленты
from app.post.post_view import post_with_comments_blueprint  # Подключаем блюпринт для вывода поста с комментариями
from app.search.search_view import posts_by_keyword_blueprint  # Подключаем блюпринт для вывода выбранных постов по ключу

app = Flask(__name__)  # Создаём наше приложение
app.config.from_object(FlaskConfig)  # Подключаем для доступа к конфигурационным константам

# Регистрируем блюпринты
app.register_blueprint(all_posts_blueprint)
app.register_blueprint(post_with_comments_blueprint)
app.register_blueprint(posts_by_keyword_blueprint)


# Добавляем обработчики ошибок
@app.errorhandler(500)
def internal_server_error(error):
    return "<h3>Похоже, такого поста не существует или проблема с базой данных</h3>", 500


@app.errorhandler(404)
def page_not_found(error):
    return "<h3>Похоже, такой страницы не существует</h3>", 404


if __name__ == "__main__":
    app.run()
