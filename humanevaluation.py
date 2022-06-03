import numpy as np

def rand_csw():
    with open("cswdatabase/csw-2022-04.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()

    num_tweets = 79207

    count = 100
    i = 0
    tweets = []

    while i < count:
        rand_tweet = 3*np.random.randint(0, num_tweets-1)
        tweets.append(lines[rand_tweet:rand_tweet+3])
        i += 1

    with open("humanevaluation/100-sampled-csw.txt", 'w', encoding='utf-8') as w:
        for tweet in tweets:
            for line in tweet:
                w.write(line)

def rand_tweet():
    with open("corpora/clean-tweets/department/clean-tweets-2022-04.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()

    num_tweets = len(lines)

    count = 100
    i = 0
    tweets = []

    while i < count:
        rand_tweet = np.random.randint(0, num_tweets-1)
        tweets.append(lines[rand_tweet])
        i += 1

    with open("humanevaluation/100-sampled-tweets.txt", 'w', encoding='utf-8') as w:
        for tweet in tweets:
            w.write(tweet)

rand_tweet()