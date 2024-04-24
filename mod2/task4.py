from flask import Flask
from datetime import datetime

app = Flask(__name__)

def get_weekday_greeting():
    weekday_index = datetime.today().weekday()
    days = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
    if weekday_index in [0, 1, 3, 6]:
        return "Хорошего", days[weekday_index]
    else:
        return "Хорошей", days[weekday_index]

@app.route('/hello-world/<name>')
def hello_world(name):
    greeting, weekday = get_weekday_greeting()
    return f"Привет, {name}! {greeting} {weekday}!"

if __name__ == '__main__':
    app.run(debug=True)
