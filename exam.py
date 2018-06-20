import re
import os

def new_files():
    start_path = './news/'
    for root, dirs, files in os.walk(start_path):
        for file in files:
            fl = start_path + file
            with open(fl, 'r', encoding='cp1251') as f:
                text = f.read()
                for line in text:
                    print(line)
                    title = re.search('<title>(.*?)</title>', line)
                    with open('new.txt', 'w', encoding='utf-8') as new:
                        for el in title:
                            new.write(str(el) + '\t')

#def titles(all_lines):
    #titles = re.search('<title>(.*?)</title>', str(all_lines))
   # with open('text_write.txt', 'w', encoding='utf-8') as new:
  #      for el in titles:
 #           new.write(str(el))
#
#titles(new_files()) aaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaA

new_files()

