from pathlib import Path
from benedict.functions import parse_word_list, random_item


class Name():
    def __init__(self):
        self.closed_list = parse_word_list("benedict/data/closed_first.txt")
        self.open_list = parse_word_list("benedict/data/open_first.txt")
        self.vowel_list = parse_word_list("benedict/data/vowels.txt")
        self.cle_list = parse_word_list("benedict/data/cle_words.txt")
        self.endings_list = parse_word_list("benedict/data/endings.txt")
        self.three_letter_words_list = parse_word_list("benedict/data/three_letter_words.txt")
        self.four_letter_words_list = parse_word_list("benedict/data/four_letter_words.txt")
        self.five_letter_words_list = parse_word_list("benedict/data/five_letter_words.txt")
        self.rcon_words_list = parse_word_list("benedict/data/rcon_words.txt")

    def __str__(self):
        structure = [self.cle_list, self.four_letter_words_list, self.three_letter_words_list, self.rcon_words_list]
        # benedict_string = random_item(self.open_list) + random_item(self.vowel_list) + ' ' + random_item(self.closed_list) + random_item(self.closed_list)
        benedict_string = random_item(structure[0]) + random_item(structure[1]) + ' ' + random_item(structure[2]) + random_item(structure[3])
        return benedict_string.title()