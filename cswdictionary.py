import csv
from tqdm import tqdm

# df = pd.read_csv('dictionaries/en-dict.csv')
# words = df.the
#
# print(words)

def csv_to_words(file):
    lan = []
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            lan.append((row[0], int(row[1])))
    return lan


english = csv_to_words('dictionaries/en-dict.csv')
german = csv_to_words('dictionaries/de-dict.csv')
urban = csv_to_words('dictionaries/urban.csv')

eng_tot = english + urban

eng = {}

for word in tqdm(eng_tot):
    if word[0] in eng:
        eng[word[0]] += word[1]
    else:
        eng[word[0]] = word[1]


eng = sorted(eng.items(), key=lambda item: item[1], reverse = True)

tot = {}

german = dict(german)
for word in eng:
    if word[0] not in german:
        tot[word[0]] = word[1]

i = 0
j = 0
file = "dictionaries/csw.csv"
with open(file, 'w', encoding='utf-8') as f:
    for word in tot.keys():
        j += 1
        i += tot[word]
        f.write(f"{word},{tot[word]}\n")

print(f"Outputted file {file} with {j} terms with word frequencies out of {i}")


# eng_tot = list(dict(eng_tot).items())
# eng_tot = sorted(eng_tot, key=lambda x: x[1], reverse = True)