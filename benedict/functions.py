import os, random

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