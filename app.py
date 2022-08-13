from flask import Flask  # Подключаем необходимые инструменты из модуля flask
from config import FlaskConfig  # Подключаем конфигурационный класс
from app.main.all_posts_views import all_posts_blueprint  # Подключаем блюпринт для вывода ленты

app = Flask(__name__)  # Создаём наше приложение
app.config.from_object(FlaskConfig)  # Подключаем для доступа к конфигурационным константам
app.register_blueprint(all_posts_blueprint)  # Регистрируем блюпринты

if __name__ == "__main__":
    app.run()
