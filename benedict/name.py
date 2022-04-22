from pathlib import Path
from benedict.functions import parse_word_list, random_item


class Name():
    def __init__(self):
        self.closed_list = parse_word_list("benedict/data/closed_first.txt")
        self.open_list = parse_word_list("benedict/data/open_first.txt")
        self.vowel_list = parse_word_list("benedict/data/vowels.txt")
    
    def __str__(self):
        benedict_string = random_item(self.open_list) + random_item(self.vowel_list) + ' ' + random_item(self.closed_list) + random_item(self.closed_list)
        return benedict_string.title()