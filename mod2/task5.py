def max_number(numbers):
    try:
        numbers = list(map(int, numbers.split('/')))
        max_num = max(numbers)
        return max_num
    except ValueError:
        return None


# http://127.0.0.1:5000/max_number/10/2/9/1/100