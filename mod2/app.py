from flask import Flask, render_template, request
from task1 import get_summary_rss
import subprocess
from datetime import datetime
from task4 import get_weekday_greeting
from task6 import get_file_preview
from html import escape
from task5 import max_number
from task7 import tracker


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the tasks app!'

@app.route('/get_summary_rss')
def get_summary_rss_route():
    file_path = 'output_file.txt'
    summary_rss = get_summary_rss(file_path)
    return f'Summary RSS: {summary_rss}'

@app.route('/get_mean_size')
def get_mean_size_route():
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    process = subprocess.Popen(['python3', 'task2.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output_mean_size, _ = process.communicate(input=output.encode('utf-8'))

    return f'Mean size of files: {output_mean_size.decode("utf-8")}'


weekdays = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')

@app.route('/hello-world/<name>')
def hello_world(name):
    greeting_word, current_weekday = get_weekday_greeting()
    return f"Привет, {name}. {greeting_word} {current_weekday}!"

@app.route('/max_number/<path:numbers>')
def max_number_route(numbers):
    max_num = max_number(numbers)
    if max_num is not None:
        return f"Максимальное переданное число: <i>{max_num}</i>"
    else:
        return "Ошибка: принимаются только числа, укажите через / , например /8/14/14/110..."

@app.route('/preview/<int:size>/<path:relative_path>')
def file_preview(size, relative_path):
    abs_path, result_size, result_text = get_file_preview(size, relative_path)
    if abs_path is None:
        return 'File not found', 404


    abs_path = f'<b>{abs_path}</b>'
    result_text = result_text.replace('\n', '<br>')
    return f'{abs_path} {result_size}<br>{result_text}'

@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    tracker.add_expense(date, number)
    return f"Expense of {number} rubles added for {date}."

@app.route('/calculate/<int:year>')
def calculate_yearly_expenses(year):
    total_expenses = tracker.calculate_yearly_expenses(year)
    return f"Total expenses for year {year}: {total_expenses} rubles."

@app.route('/calculate/<int:year>/<int:month>')
def calculate_monthly_expenses(year, month):
    total_expenses = tracker.calculate_monthly_expenses(year, month)
    return f"Total expenses for {month}/{year}: {total_expenses} rubles."


if __name__ == '__main__':
    app.run(debug=True)
