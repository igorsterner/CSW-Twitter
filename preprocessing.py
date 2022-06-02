from cleantext import clean
from tqdm import tqdm
from langdetect import detect

print("Reading tweets...")
with open("corpora/extracted-tweets/all-tweets-2022-04.txt", 'r', encoding='utf-8') as f:
    tweets = f.readlines()

remove = ['@', '*']
i = 0
numtweets = len(tweets)

print("Cleaning tweets...")

with open("corpora/clean-tweets/clean-tweets-2022-04.txt", 'w', encoding='utf-8') as f:
    for tweet in tqdm(tweets):

        tweet_clean = clean(tweet,
                            lower=False,
                            no_urls=True,
                            no_emoji=True,
                            no_emails=True,
                            no_phone_numbers=True,
                            # no_numbers=True,
                            lang='de',
                            )
        words = tweet_clean.split()
        words_clean = []
        for w in words:
            if not any((r in w) for r in remove):
                words_clean.append(w)
        tweet_clean = ' '.join(words_clean)

        try:
            lan = detect(tweet_clean)
        except:
            lan = 'error'

        if lan != 'de':
            i += 1
            continue

        f.write(tweet_clean)
        f.write("\n")

perc = (i/numtweets)*100
print(f"{perc}% of tweets were identified as non-German (that is {i} out of {numtweets})")