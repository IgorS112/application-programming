import os

def get_file_preview(size, relative_path):
    abs_path = os.path.abspath(relative_path)
    try:
        with open(abs_path, 'r') as file:
            result_text = file.read(size)
            result_size = len(result_text)
            return abs_path, result_size, result_text
    except FileNotFoundError:
        return None, None, None


# http://127.0.0.1:5000/preview/5/doc/simple.txt