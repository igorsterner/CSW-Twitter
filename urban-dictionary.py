from tqdm import tqdm
from collections import Counter

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

entries = []
dictionary = []

print("Gathering all terms in Urban Dictionary")

for char in alphabet[0:26]:
    with open(f"dictionaries/urban-dictionary/data/{char.upper()}.data", 'r', encoding = 'utf-8') as f:
        entries += f.read().splitlines()

print(f"Finished gathering {len(entries)} terms in Urban Dictionary")

print("Writing distinct words")

with open("dictionaries/urban.txt", 'w', encoding = 'utf-8') as w:
    for entry in tqdm(entries):
        entry = entry.replace('"', '')
        for word in entry.split():
            save = True
            lower_word = word.lower()
            if word.isalpha():

            if save:
                if lower_word not in dictionary:
                    dictionary.append(lower_word)
                    w.write(lower_word)
                    w.write('\n')

print(f"Finished saving {len(dictionary)} distinct words from the Urban Dictionary")
# print(dictionary[0:1000])
# print(len(dictionary))