import sys

def decrypt(cipher):
    result = []
    skip_next = False
    for char in cipher:
        if skip_next:
            skip_next = False
            continue
        if char == '.':
            if result:
                result.pop()
            skip_next = True
        elif char == '..':
            if result:
                result.pop()
            if result:
                result.pop()
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    cipher = sys.stdin.read().strip()
    print(decrypt(cipher))


# $ echo 'абраа..-.кадабра' | python3 task3.py