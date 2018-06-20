import re
import os

def new_files():
    all_lines = []
    start_path = './news/'
    for root, dirs, files in os.walk(start_path):
        for file in files:
            fl = start_path + file
            with open(fl, 'r') as f:
                f = list(f)
                text = f.encode('cp1251')
                for line in text:
                    print(line)
                    if re.search('<title>(.*?)</title>', line):
                        all_lines.append(line)
    print(all_lines)
    return all_lines

#def titles(all_lines):
    #titles = re.search('<title>(.*?)</title>', str(all_lines))
   # with open('text_write.txt', 'w', encoding='utf-8') as new:
  #      for el in titles:
 #           new.write(str(el))
#
#titles(new_files())

new_files()

