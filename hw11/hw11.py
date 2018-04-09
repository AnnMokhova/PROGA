import re

def open_file():
    text = ''
    with open('Viking.html', 'rb') as f:
        text = f.read()
    return text

def change_words(text):
    change = re.sub(r'([^А-Яа-я])Викинг((?:а(?:м(?:и)))|((?:о)?в)?|у|и[^А-Яа-я])', r'\1Бурундук\2',text.decode('utf-8'))
    change = re.sub(r'([^А-Яа-я])викинг((?:а(?:м(?:и)))|((?:о)?в)?|у|и[^А-Яа-я])', r'\1бурундук\2',change)
    return change

def empty_file(change):
    with open('text.txt', 'w', encoding='utf-8') as empty_file:
       empty_file.write(change) 
   
def main():
    empty_file(change_words(open_file()))

main()
