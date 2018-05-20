import os
import re

def main():
    start_path = '.'
    with_kirill = []
    for root, dirs, files in os.walk(start_path):
        for dirname in dirs:
            if re.match(r'^[А-Яа-яЁё\s]+$', dirname):
                with_kirill.append(dirname)
    print('Количество папок в дереве с полностью кириллическими названиями: ', len(with_kirill))

main()
