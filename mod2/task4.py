from datetime import datetime
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

weekdays = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')

def get_weekday_greeting():
    weekday_index = datetime.today().weekday()
    current_weekday = weekdays[weekday_index]
    parsed_weekday = morph.parse(current_weekday)[0]
    if current_weekday in ['понедельник', 'вторник', 'четверг', 'воскресенье']:
        greeting_word = "Хорошего"
    else:
        greeting_word = "Хорошей"
    return greeting_word, parsed_weekday.inflect({'gent'}).word.capitalize()

greeting, weekday = get_weekday_greeting()
print(f"Привет, Игорь. {greeting} {weekday}!")
