from collections import defaultdict
from unidecode import unidecode
import re


def clean_text(s):
    decoded = unidecode(s)
    alpha_only = re.sub(r'\W', '', decoded)
    return alpha_only.lower()

def text_to_key(s):
    sort = sorted(s)
    return ''.join(sort)


def build_dict(filepath='/usr/share/dict/words'):
    anagramed_words = defaultdict(lambda: [])
    with open(filepath) as f:
        for word in f.readlines():
            cleaned_word = clean_text(word)
            key = text_to_key(cleaned_word)

            anagramed_words[key].append(cleaned_word)

    return anagramed_words

def get_possible(words, anagram_dict):
    possible_words = []
    for word, spots in words:
        if len(spots) == 0:
            continue

        cleaned_word = clean_text(word)
        key = text_to_key(cleaned_word)
        possible_words.append((set(anagram_dict[key]), spots))

    return possible_words

def recursively_make_answers(found_words, visit, index=0, s=''):
    if index >= len(found_words):
        visit(s)
        return

    words_set, spots = found_words[index]
    for word in words_set:
        letters = [word[index] for index in spots]
        recursively_make_answers(found_words, visit, index+1, s+''.join(letters))

if __name__ == '__main__':
    scrambled_1 = [
        ('ULQIT', [0]),
        ('LAVEES', [5]),
        ('BEEESTRMP', [0]),
        ('SVRTAEH', [0]),
        ('TECTHUNS', [6]),
        ('AUMUTN', []),
        ('ATOLFLOB', [5])
    ]

    scrambled_2 = [
        ('TEFON', [2, 4]),
        ('SOKIK', [0, 1, 3]),
        ('NIUMEM', [4]),
        ('SICONU', [3, 4])
    ]
    anagrams = build_dict()
    possible_words = get_possible(scrambled_2, anagrams)
    answers = []
    recursively_make_answers(possible_words, answers.append)

    for answer in answers:
        unscrambled = anagrams[text_to_key(answer)]
        print(unscrambled if len(unscrambled) > 0 else answer)
