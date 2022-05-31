import sys
import csv
from tqdm import tqdm

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)


def leipzig_dict(file_in, min_freq):
    dictionary = {}
    with open(file_in, 'r', newline='', encoding='utf-8') as f:
        doc = csv.reader(f, delimiter='\t')

        for line in doc:
            phrase = line[1].lower()
            phrase = phrase.replace('-', ' ')
            for word in phrase.split():
                if (int(line[2]) > min_freq) and word.isalpha() and (len(word) > 2):
                    if word in dictionary:
                        dictionary[word] += int(line[2])
                    else:
                        dictionary[word] = int(line[2])

    return dictionary


def write_dictionary(dictionary, file_out):
    i = 0
    j = 0

    with open(file_out, 'w', encoding='utf-8') as w:
        for word in dictionary.keys():
            j += 1
            i += dictionary[word]
            w.write(f"{word},{dictionary[word]}\n")

    print(f"Outputted file {file_out} with {j} terms with word frequencies out of {i}")


def dictcc_dict(file_in):
    print("Hello!")
    dictionary = []
    with open(file_in, 'r', newline='', encoding='utf-8') as f:
        doc = csv.reader(f, delimiter='\t')
        for line in tqdm(doc):
            if len(line) == 0 or line[0][0] == '#':
                continue
            # dictionary.append(line[0])
            # phrase = line[0].lower()
            phrase = line[0]
            # if phrase == 'Digga! [Slang] [Kumpel!]':
            #     print(line)
            #     phrase = ''.join([i for i in phrase if (i.isalpha() or i == ' ')])
            #     print(phrase)
            #     for word in phrase.split():
            #         if word.isalpha() and (len(word) > 2):
            #             print(word)

            phrase = ''.join([i for i in phrase if (i.isalpha() or i == ' ')])
            # brackets = ['(', ')', '{', '}', '[', ']', "'", '!', '?', '#']
            # if phrase == 'In Istanbul treffen Orient und Okzident aufeinander.':
            #     print(line)
            #     for b in brackets:
            #         phrase = phrase.replace(b, '')
            #     print(phrase)
            # for b in brackets:
            #     phrase = phrase.replace(b, '')
            for word in phrase.split():
                dictionary.append(word.lower())

    print(f"Outputted {len(set(dictionary))} terms of dict.cc")

    return set(dictionary)


# eng_file = "dictionaries/Leipzig Dict/100k-en-news-2020.txt"
# eng_words = "dictionaries/en-dict.csv"
# eng = leipzig_dict(eng_file, 5)
# write_dictionary(eng, eng_words)

# de_file = "dictionaries/Leipzig Dict/300k-de-news-2021.txt"
# de_words = "dictionaries/de-dict.csv"
# de = leipzig_dict(de_file, 2)
# write_dictionary(de, de_words)


de_dictcc_file = "dictionaries/dict.cc/dictdict.txt"
dictcc_words = "dictionaries/de-dictcc.txt"
de_dictcc = dictcc_dict(de_dictcc_file)

with open(dictcc_words, 'w', encoding='utf-8') as w:
    for word in de_dictcc:
        w.write(f"{word}\n")
