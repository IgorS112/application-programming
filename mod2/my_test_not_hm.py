import sys

weekdays_tuple = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
weekdays_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
weekdays_dict = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'}

print("Размер кортежа:", sys.getsizeof(weekdays_tuple))
print("Размер списка:", sys.getsizeof(weekdays_list))
print("Размер словаря:", sys.getsizeof(weekdays_dict))





from task6 import get_file_preview

size = 3
relative_path = 'doc/simple.txt'
abs_path, result_size, result_text = get_file_preview(size, relative_path)

print(f'Absolute path: {abs_path}')
print(f'Result size: {result_size}')
print(f'Result text: {result_text}')
