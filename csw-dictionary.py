import csv
import pprint
from collections import defaultdict
import pandas as pd
from operator import itemgetter


# df = pd.read_csv('dictionaries/en-dict.csv')
# words = df.the
#
# print(words)

def csv_to_words(file):
    lan = []
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            lan.append((row[0], int(row[1])))
    return lan


english = csv_to_words('dictionaries/en-dict.csv')
german = csv_to_words('dictionaries/de-dict.csv')
urban = csv_to_words('dictionaries/urban.csv')

print(english[0:10])
print(urban[0:10])
eng_tot = english + german
print(eng_tot[0:10])
eng_tot = sorted(eng_tot,key=itemgetter(1))
print(eng_tot[0:10])
