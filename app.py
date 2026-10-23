from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    items = [
        {'name': 'Зимова куртка-пуховик', 'category': 'Куртки', 'price': 3200},
        {'name': 'Демісезонна куртка', 'category': 'Куртки', 'price': 2400},
        {'name': 'Шкіряна куртка', 'category': 'Куртки', 'price': 5800},
        {'name': 'Джинсова куртка', 'category': 'Куртки', 'price': 1900},
        {'name': 'Бомбер', 'category': 'Куртки', 'price': 2100},
        {'name': 'Класичне пальто', 'category': 'Пальта', 'price': 4500},
        {'name': 'Вовняне пальто оверсайз', 'category': 'Пальта', 'price': 5200},
        {'name': 'Тренч', 'category': 'Пальта', 'price': 3900},
        {'name': 'Пальто-кокон', 'category': 'Пальта', 'price': 4800},
        {'name': 'Вітровка', 'category': 'Легка верхній одяг', 'price': 1800},
        {'name': 'Дощовик', 'category': 'Легка верхній одяг', 'price': 1500},
        {'name': 'Софтшелл', 'category': 'Легка верхній одяг', 'price': 2300},
        {'name': 'Жилет утеплений', 'category': 'Жилети', 'price': 1700},
        {'name': 'Жилет пуховий', 'category': 'Жилети', 'price': 2000},
        {'name': 'Парка з капюшоном', 'category': 'Парки', 'price': 4100},
        {'name': 'Парка зимова з хутром', 'category': 'Парки', 'price': 4900},
        {'name': 'Анорак', 'category': 'Парки', 'price': 2600},
        {'name': 'Дублянка', 'category': 'Зимовий одяг', 'price': 7500},
        {'name': 'Шуба штучна', 'category': 'Зимовий одяг', 'price': 6200},
        {'name': 'Куртка гірськолижна', 'category': 'Спортивний одяг', 'price': 5400},
    ]
    return render_template('shop.html', items=items)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    # debug=True: автоматичний перезапуск після змін у коді та детальні повідомлення про помилки.
    # Використовується лише під час розробки.
    app.run(debug=True)
