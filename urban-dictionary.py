from tqdm import tqdm
from collections import Counter
import pprint

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
entries = ""

# with open(f"dictionaries/urban-dictionary/data/A.data", 'r', encoding='utf-8') as f:
#     entries = f.read().replace('\n', ' ')

with open("dictionaries/100k-en.txt", 'r', encoding='utf-8') as f:
    english = f.read().splitlines()

for char in alphabet[0:26]:
    with open(f"dictionaries/urban-dictionary/data/{char.upper()}.data", 'r', encoding = 'utf-8') as f:
        entries += f.read().replace('\n', ' ').replace('"','')

print(len(entries))

print("Splitting words...")
words = entries.split()

print("Passing words to instance of Counter class...")
Counter = Counter(words)

print("Finding most common words...")
top_words = Counter.most_common(100000)

urban = []
for word in tqdm(top_words):
    if word not in english:
        urban.append(word)

print(urban)
print(len(urban))

print("Done")

# print(type(top_words))
# pprint.pprint(top_words)


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#
# entries = []
# dictionary = []
#
# print("Gathering all terms in Urban Dictionary")
#
# for char in alphabet[0:26]:
#     with open(f"dictionaries/urban-dictionary/data/{char.upper()}.data", 'r', encoding = 'utf-8') as f:
#         entries += f.read().splitlines()
#
# print(f"Finished gathering {len(entries)} terms in Urban Dictionary")
#
# print("Writing distinct words")
#
# with open("dictionaries/urban.txt", 'w', encoding = 'utf-8') as w:
#     for entry in tqdm(entries):
#         entry = entry.replace('"', '')
#         for word in entry.split():
#             save = True
#             lower_word = word.lower()
#             if word.isalpha():
#
#             if save:
#                 if lower_word not in dictionary:
#                     dictionary.append(lower_word)
#                     w.write(lower_word)
#                     w.write('\n')
#
# print(f"Finished saving {len(dictionary)} distinct words from the Urban Dictionary")
# print(dictionary[0:1000])
# print(len(dictionary))