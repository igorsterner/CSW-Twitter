from collections import Counter

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']
entries = ""

# with open("dictionaries/en-dict.txt", 'r', encoding='utf-8') as f:
#     english = f.read().splitlines()

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
i = 0
j = 0
with open("dictionaries/urban.csv", 'w', encoding='utf-8') as f:
    for word in top_words:
        if (word[1] > 5) and (word[0].isalpha()):
            urban[word[0]] = word[1]
            j += 1
            i += word[1]
            f.write(f"{word[0]},{word[1]}\n")

print(f"Urban dictionary is {len(urban)} words long")

print(f"Outputted file with {j} terms with word frequencies out of {i}")
