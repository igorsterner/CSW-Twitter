import biblib.bib
import sys
from tqdm import tqdm
import json
import csv



print("Importing")
# bib_file = 'citations/test.bib'
bib_file = 'citations/anthology+abstracts.bib'
with open(bib_file, 'r', encoding='utf-8') as fp:
    db = biblib.bib.Parser().parse(fp, log_fp=sys.stderr).get_entries()
terms = ['Code-switching',
         'code-switching',
         'Code-Switching',
         'code-Switching',
         'Code switching',
         'code switching',
         'Code Switching',
         'code Switching',
         'Code-mixing',
         'code-mixing',
         'Code-Mixing',
         'code-Mixing',
         'Code mixing',
         'code Mixing',
         'Code Mixing',
         'code mixing']

match = {str(k): 0 for k in range(1998,2023)}
print(match)
for ent in db.values():
    key = ent.key
    if 'title' in ent:
        title = ent['title']
        if any((t in title) for t in terms):
            match[ent['year']] += 1
        else:
            if 'abstract' in ent:
                abstract = ent['abstract']
                if any((t in abstract) for t in terms):
                    match[ent['year']] += 1

with open("results/citations.csv", 'w') as f:
    for key in match.keys():
        f.write(f"{key}, {match[key]}\n")