def open_text():
    with open ('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        lines = text.splitlines()
        words = lines.strip(' ')
        print(lines)

open_text()
