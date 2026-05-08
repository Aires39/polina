from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Здесь мы описываем качества для каждой карточки
    qualities = [
        {"q": "Самая милая", "img": "photo1.jpg"},
        {"q": "Безумно красивая", "img": "photo2.jpg"},
        {"q": "Очень умная", "img": "photo3.jpg"},
        {"q": "Добрая душа", "img": "photo4.jpg"},
        {"q": "Моя поддержка", "img": "photo5.jpg"},
        {"q": "Лучшая в мире", "img": "photo6.jpg"}
    ]
    return render_template('index.html', cards=qualities)

if __name__ == '__main__':
    app.run(debug=True)