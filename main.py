import os
import pandas as pd
import re
import random

def parse_word_list(filename):
    file = open(filename, "r")
    data = file.read()
    data_list = data.split('\n')
    file.close()
    k = []
    for item in data_list:
        item = item.replace(' ', '')
        k.append(item)
    return k

def random_item(items):
    return items[random.randint(0, len(items)-1)]


# def generate_name(mode):
#     grammars = [closed_list, open_list, vowel_list, open_list]
#     if mode == 1:
#         grammar = [closed_list, open_list, vowel_list, open_list]
#     elif mode == 2:
#         grammar = [open_list, vowel_list, closed_list, closed_list]
#     elif mode == 3:
#         grammar = [vowel_list, open_list, closed_list, open_list]
#     elif mode == 4:
#         grammar = [grammars[random.randint(0, len(grammars)-1)], grammars[random.randint(0, len(grammars)-1)], grammars[random.randint(0, len(grammars)-1)], grammars[random.randint(0, len(grammars)-1)]]

#     benedict_string = random_item(grammar[0]) + random_item(grammar[1]) + ' ' + random_item(grammar[2]) + random_item(grammar[3])
#     return benedict_string.title()



# closed_list = parse_word_list("closed_first.txt")
# open_list = parse_word_list("open_first.txt")
# vowel_list = parse_word_list("vowels.txt")

# name = generate_name(2)
# print(name)

class Name():
    def __init__(self):
        self.closed_list = parse_word_list("closed_first.txt")
        self.open_list = parse_word_list("open_first.txt")
        self.vowel_list = parse_word_list("vowels.txt")
    
    def __str__(self):
        benedict_string = random_item(self.open_list) + random_item(self.vowel_list) + ' ' + random_item(self.closed_list) + random_item(self.closed_list)
        return benedict_string.title()

name = Name()
print(name)

def app(environ, start_response):
        name = str(Name()).encode('utf-8')
        data = b"%s!\n" % name
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])