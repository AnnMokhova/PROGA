import re

def open_f():
    with open('mystem.xml', encoding='utf-8') as f:
        text = f.read()
        for line in f:
            line = line.replace('\n', '')
    return text

def change(text):
    tag = re.sub(r'lex=|</?w>|<se>|</?se>|<ana|gr=|</?body>|</?html>|/>', '', text)        
    print(tag)
    with open('text_write4.txt', 'w', encoding='utf-8') as fl:
        for line in tag:
            #for word in line:
                #if word.endswith('"'):
                    
                    #line = line.replace('" ', '",')
            fl.write(str(line))
            
change(open_f())
