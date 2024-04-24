from flask import Flask, render_template
import random
from datetime import datetime, timedelta

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

# Задача 2
cars_list = ["Chevrolet", "Renault", "Ford", "Lada"]

# Задача 3
cat_breeds = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

# Задача 6
with open("war_and_peace.txt", "r", encoding="utf-8") as book_file:
    words = book_file.read().split()

def get_random_word():
    return random.choice(words).strip(".,!?\"':;()")

# Задача 7
counter_visits = 0

@app.route('/hello_world')
def hello_world():
    return "Привет, мир!"

@app.route('/cars')
def cars():
    return ", ".join(cars_list)

@app.route('/cats')
def cats():
    return random.choice(cat_breeds)

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Точное время: {current_time}"

@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = (datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S")
    return f"Точное время через час будет {current_time_after_hour}"

@app.route('/get_random_word')
def get_random():
    return get_random_word()

@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1
    return f"Страница была посещена {counter_visits} раз"

if __name__ == '__main__':
    app.run(debug=True)