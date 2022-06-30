from pybtex.database.input import bibtex
from tqdm import tqdm

parser = bibtex.Parser()
bibdata = parser.parse_file("citations/anthology+abstracts.bib")
bibkeys = bibdata.entries.keys()
bibarray = []

match = {str(k): 0 for k in range(1998, 2023)}

terms = ['code-switching',
         'code switching',
         'code-switched',
         'code switched',
         'code-mixing',
         'code mixing',
         'code-mixed',
         'code mixed']
german = 0
term = "code-switching"

for bib_id in tqdm(bibdata.entries):
    b = bibdata.entries[bib_id].fields

    if int(b["year"]) < 1998:
        continue
    title = b["title"].casefold()
    if any((t in title) for t in terms):
        match[b["year"]] += 1
        if 'german' in title:
            german += 1
            print(title)
    elif "abstract" in b:
        abstract = b["abstract"].casefold()
        if any((t in abstract) for t in terms):
            match[b['year']] += 1
            if 'german' in abstract:
                german += 1
                print(title)

with open("results/citations.csv", 'w') as f:
    for key in match.keys():
        f.write(f"{key}, {match[key]}\n")
        print(f"({key}, {match[key]})")

print(f"The number of articles mentioning code-switching and german is: {german}")
