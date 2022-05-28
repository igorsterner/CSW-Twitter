import pprint

with open("corpora/clean-tweets/clean-tweets-2022-04.txt", 'r', encoding = 'utf-8') as f:
    tweets = f.read().splitlines()

tweets = tweets[0:10]

for tweet in tweets:
    print(tweet)