import pprint
import nltk
from tqdm import tqdm
import csv

with open("corpora/clean-tweets/clean-tweets-2022-04.txt", 'r', encoding = 'utf-8') as f:
    tweets = f.read().splitlines()

words = []
with open("dictionaries/csw.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        words.append(row[0])
# words_tup = csv_to_words('dictionaries/csw.csv')
# words = [i[0] for i in words_tup]
tweets = tweets[0:1000]
csw = {}
with open("cswdatabase/csw.txt",  'w', encoding = 'utf-8') as f:
    for tweet in tqdm(tweets):
        isCSW = False
        lastCSW = True
        log = ""
        for word in nltk.word_tokenize(tweet.lower()):
            if word in words:
                if word in csw:
                    csw[word] += 1
                else:
                    csw[word] = 1
                isCSW = True
                lastCSW = True
                log += word + " "
            elif lastCSW:
                log += "..."
                lastCSW = False
        if isCSW:
            f.write(log)
            f.write('\n')
            f.write(tweet)
            f.write('\n')
            f.write('-----------------------------------------------------------\n')

csw = sorted(csw.items(), key=lambda item: item[1], reverse = True)
with open('results/csw.csv', 'w', encoding='utf-8') as f:
    for word in csw:
        f.write(f"{word[0]},{word[1]}\n")