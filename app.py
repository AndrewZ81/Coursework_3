# Подключаем необходимые инструменты из модуля flask
from flask import Flask

# Подключаем конфигурационный класс
from config import CONFIG

# Создаём наше приложение
app = Flask(__name__)
app.config.from_object(CONFIG)
