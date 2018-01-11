def open_text():
    with open ('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        splited_text = text.split()
        q = []
        for word in splited_text:
            q.append(word.strip(',-.()—"«»“„'))
        print(q)
        
open_text()
