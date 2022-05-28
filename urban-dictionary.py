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
    if (word[1] > 5) and (word[0].isalpha()):
        urban[word[0]] = word[1]

print(f"Urban dictionary is {len(urban)} words long")
urban = {k: v for k, v in sorted(urban.items(), key=lambda item: item[1], reverse = True)}
print(urban)
i = 0
j = 0
file = "dictionaries/urban.csv"
with open(file, 'w', encoding='utf-8') as f:
    for word in urban.keys():
        j += 1
        i += urban[word]
        f.write(f"{word},{urban[word]}\n")

print(f"Outputted file {file} with {j} terms with word frequencies out of {i}")
