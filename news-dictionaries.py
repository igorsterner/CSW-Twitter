import csv

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']


def leipzig_dict(file_in, file_out):
    i = 0
    j = 0
    with open(file_in, 'r', newline='', encoding='utf-8') as f:
        with open(file_out, 'w', encoding='utf-8') as w:
            for line in csv.reader(f, delimiter='\t'):
                if int(line[2]) > 5:
                    w.write(f"{line[1]}, {line[2]}\n")
                    i += int(line[2])
                    j += 1

    print(f"Outputted file {file_out} with {j} terms with word frequencies out of {i}")


eng_file = "dictionaries/Leipzig Dict/100k-en-news-2020.txt"
eng_words = "dictionaries/en-dict.csv"
leipzig_dict(eng_file, eng_words)

de_file = "dictionaries/Leipzig Dict/100k-de-news-2021.txt"
de_words = "dictionaries/de-dict.csv"
leipzig_dict(de_file, de_words)
