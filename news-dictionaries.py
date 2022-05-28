import csv

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']


def leipzig_dict(file_in):
    dictionary = {}
    with open(file_in, 'r', newline='', encoding='utf-8') as f:
        doc = csv.reader(f, delimiter='\t')

        for line in doc:
            low_word = line[1].lower()
            if (int(line[2]) > 5) and line[1].isalpha() and (len(line[1]) > 2):
                if low_word in dictionary:
                    dictionary[low_word] += int(line[2])
                else:
                    dictionary[low_word] = int(line[2])

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


eng_file = "dictionaries/Leipzig Dict/100k-en-news-2020.txt"
eng_words = "dictionaries/en-dict.csv"
eng = leipzig_dict(eng_file)
write_dictionary(eng, eng_words)

de_file = "dictionaries/Leipzig Dict/100k-de-news-2021.txt"
de_words = "dictionaries/de-dict.csv"
de = leipzig_dict(de_file)
write_dictionary(de, de_words)
