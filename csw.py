import pprint
import nltk
from tqdm import tqdm
import csv

# source = "corpora/clean-tweets/clean-tweets-2022-04.txt"
source = "humanevaluation/100-sampled-tweets.txt"
eval = "humanevaluation/100-sampled-tweets-igor.txt"
# eval = "cswdatabase/csw-2022-04.txt"

with open(source, 'r', encoding = 'utf-8') as f:
    tweets = f.read().splitlines()
    tweets = tweets[1::7]

print(tweets)
print(len(tweets))

words = []

with open("dictionaries/csw.txt", 'r', encoding='utf-8') as f:
    words = f.read().splitlines()

removal = ['owo', 'uwu']
for r in removal:
    words.remove(r)
# words.remove("pokemon")
# words_tup = csv_to_words('dictionaries/csw.csv')
# words = [i[0] for i in words_tup]
len_tweets = len(tweets)
csw = {}
i = 0
c = 0

print(f"Tweets loaded from {source} and are being processed and written to {eval}")

with open(eval,  'w', encoding = 'utf-8') as f:
    for tweet in tqdm(tweets):
        isCSW = False
        lastCSW = True
        log = ""

        for word in nltk.word_tokenize(tweet):
            if len(word) > 35:
                isCSW = False
                break
            if word[0].isupper():
                if lastCSW:
                    log += "..."
                    lastCSW = False
            elif word.lower() in words:
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
            c += 1
            f.write(log)
            f.write('\n')
            f.write(tweet)
            f.write('\n')
            f.write('-----------------------------------------------------------\n')

csw = sorted(csw.items(), key=lambda item: item[1], reverse = True)
with open('results/csw.csv', 'w', encoding='utf-8') as f:
    for word in csw:
        f.write(f"{word[0]},{word[1]}\n")

print(f"Outputted {c} Code-switched tweets out of {len_tweets} which accounts for {100*c/len_tweets}% of all tweets")