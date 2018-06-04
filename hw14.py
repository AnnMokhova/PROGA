#вариант 2

import re

def open_file(): 
    with open('text.txt', encoding='utf-8') as f:
        text = f.read()
        symbols_to_remove = """,:;()-—*«»"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        nude_text = re.sub(r'\n|\n\n|\t', '', text)
        nude_text = re.sub(r'\!|\?', '.', nude_text)
        splited_sentences = nude_text.split('.')
        return splited_sentences

def count_everything(splited_sentences):
    needed_sentences = []
    for sentence in splited_sentences:
        words = str(splited_sentences).split()
        if len(words) >= 10:
            needed_sentences.append(sentence)
    for sentence in needed_sentences:
        Big_words = [word for word in sentence.split() if word.istitle()]
        print('\n'.join(Big_words))
                
def main():
    count_everything(open_file())

main()
