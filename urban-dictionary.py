from collections import Counter

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']
entries = ""

for char in alphabet[0:26]:
    with open(f"dictionaries/urban-dictionary/data/{char.upper()}.data", 'r', encoding='utf-8') as f:
        entries += f.read().replace('\n', ' ').replace('"', '')

print("Splitting words...")
words = entries.split()

print("Passing words to instance of Counter class...")
Counter = Counter(words)

print("Finding most common words...")
top_words = Counter.items()
urban = {}
for word in top_words:
    repeated = False
    low_word = word[0].lower()
    for i in range(len(low_word)-2):
        if low_word[i] == low_word[i+1] == low_word[i+2]:
            repeated = True
            break
    if (not repeated) and (word[1] > 10) and (word[0].isalpha()) and (len(word[0]) > 2) and (not word[0][0].isupper()):
        if low_word in urban:
            urban[low_word] += word[1]
        else:
            urban[low_word] = word[1]

print(f"Urban dictionary is {len(urban)} words long")
urban = {k: v for k, v in sorted(urban.items(), key=lambda item: item[1], reverse = True)}
i = 0
j = 0
file = "dictionaries/urban.csv"
with open(file, 'w', encoding='utf-8') as f:
    for word in urban.keys():
        j += 1
        i += urban[word]
        f.write(f"{word},{urban[word]}\n")

print(f"Outputted file {file} with {j} terms with word frequencies out of {i}")
