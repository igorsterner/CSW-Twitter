import sys
import csv
from tqdm import tqdm
from collections import Counter

maxInt = sys.maxsize
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)


class Dictionaries():

    def __init__(self, file_in, file_out):

        self.file_in = file_in
        self.file_out = file_out

        self.words = []

    def make_dict(self, dict_type):
        if dict_type == 'leipzig':
            self.leipzig_dict()
        elif dict_type == 'dictcc':
            self.dictcc_dict()
        elif dict_type == 'urban':
            self.urban_dictionary()
        else:
            raise Exception('Type of dictionary does not exist!')

        self.write_dict()

    def leipzig_dict(self, min_freq=5):
        DICT_IN_DIR = "dictionaries/dict-leipzig/" + self.file_in

        with open(DICT_IN_DIR, 'r', newline='', encoding='utf-8') as f:
            doc = csv.reader(f, delimiter='\t')

            for line in doc:
                phrase = line[1].lower()
                phrase = phrase.replace('-', ' ')
                for word in phrase.split():
                    if (int(line[2]) > min_freq) and word.isalpha() and (len(word) > 2):
                        self.words.append(word)

    def dictcc_dict(self):

        DICT_IN_DIR = "dictionaries/dict.cc/" + self.file_in
        with open(DICT_IN_DIR, 'r', newline='', encoding='utf-8') as f:
            doc = csv.reader(f, delimiter='\t')
            for line in tqdm(doc):
                if len(line) == 0 or line[0][0] == '#':
                    continue

                phrase = line[0]

                phrase = ''.join([i for i in phrase if (i.isalpha() or i == ' ')])

                for word in phrase.split():
                    self.words.append(word.lower())

    def urban_dictionary(self):

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', ' ']

        entries = ""

        for char in alphabet[0:26]:
            with open(f"dictionaries/urban-dictionary/data/{char.upper()}.data", 'r', encoding='utf-8') as f:
                entries += f.read().replace('\n', ' ').replace('"', '')

        words = entries.split()

        counter = Counter(words)

        top_words = counter.items()

        urban = {}
        for word in top_words:
            repeated = False
            low_word = word[0].lower()
            for i in range(len(low_word) - 2):
                if low_word[i] == low_word[i + 1] == low_word[i + 2]:
                    repeated = True
                    break
            if (not repeated) and (word[1] > 10) and (word[0].isalpha()) and (len(word[0]) > 2) and (
                    not word[0][0].isupper()):
                if low_word in urban:
                    urban[low_word] += word[1]
                else:
                    urban[low_word] = word[1]

        urban = {k: v for k, v in sorted(urban.items(), key=lambda item: item[1], reverse=True)}

        self.words = urban.keys()

    def write_dict(self):

        DICT_OUT_DIR = "dictionaries/" + self.file_out

        self.words = set(self.words)
        with open(DICT_OUT_DIR, 'w', encoding='utf-8') as w:
            for word in self.words:
                w.write(f"{word}\n")

        print(f"Outputted file {self.file_out} with {len(self.words)} words")

class CSWDictionary():

    def __init__(self):
        self.en = self.DictToList("en-dict.txt")
        self.de = self.DictToList("de-dict.txt")
        self.decc = self.DictToList("de-dictcc.txt")
        self.ch = self.DictToList("de-ch-dict.txt")
        self.at = self.DictToList("de-at-dict.txt")
        self.urban = self.DictToList("urban-dict.txt")

    def DictToList(self, file):
        with open("dictionaries/"+file, 'r', encoding='utf-8') as f:
            words = f.readlines()
        return words

    def CSWCombine(self):
        en_tot = self.en + self.urban
        de_tot = self.de + self.decc + self.ch + self.at

        self.en_tot = set(en_tot)
        self.de_tot = set(de_tot)

        self.tot = self.en_tot - self.de_tot

        with open('dictionaries/csw.txt', 'w', encoding='utf-8') as w:
            for word in self.tot:
                w.write(word)

    def stats(self):
        print(f"English: {len(self.en)}")
        print(f"German: {len(self.decc)} + {len(self.de)}")
        print(f"Austrian: {len(self.at)}")
        print(f"Swiss: {len(self.ch)}")
        print(f"Urban: {len(self.urban)}")

        print(f"All German: {len(self.de_tot)}")
        print(f"All English: {len(self.en_tot)}")

        print(f"After removing identical words, English: {len(self.tot)}")
        print(
            f"Removed {len(self.en_tot) - len(self.tot)} words or {100 * (len(self.en_tot) - len(self.tot)) / len(self.en)}% of the words")


if __name__ == "__main__":
    # # English
    # d = Dictionaries("100k-en-news-2020.txt", "en-dict.txt")
    # d.make_dict('leipzig')
    #
    # # German
    # d = Dictionaries("300k-de-news-2021.txt", "de-dict.txt")
    # d.make_dict('leipzig')
    #
    # # German Dict.cc
    # d = Dictionaries("dictdict.txt", "de-dictcc.txt")
    # d.make_dict('dictcc')
    #
    # # Swiss
    # d = Dictionaries("300k-de-ch-news-2012.txt", "de-ch-dict.txt")
    # d.make_dict('leipzig')
    #
    # # Austrian
    # d = Dictionaries("100k-de-at-news-2012.txt", "de-at-dict.txt")
    # d.make_dict('leipzig')
    #
    # # Urban Dictionary
    # d = Dictionaries(None, "urban-dict.txt")
    # d.make_dict('urban')

    # CSW Dictionary
    c = CSWDictionary()
    c.CSWCombine()
    c.stats()
