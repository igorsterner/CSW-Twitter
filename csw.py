import pprint
import nltk
from cswdictionary import csv_to_words

with open("corpora/clean-tweets/clean-tweets-2022-04.txt", 'r', encoding = 'utf-8') as f:
    tweets = f.read().splitlines()

words_tup = csv_to_words('dictionaries/csw.csv')
words = [i[0] for i in words_tup]
words.remove("URL")
tweets = tweets[0:30]

for tweet in tweets:
    for word in nltk.word_tokenize(tweet):
        if word in words:
            print(word)
            print(tweet)
            print("-------")
            break
