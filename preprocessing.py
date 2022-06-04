from cleantext import clean
from tqdm import tqdm
from langdetect import detect


def preprocess(month):
    print(f"Reading tweets for 2022-{month}...")
    with open(f"corpora/extracted-tweets/all-tweets-2022-{month}.txt", 'r', encoding='utf-8') as f:
        tweets = f.readlines()
    remove = ['@', '*']
    i = 0
    numtweets = len(tweets)

    print(f"Cleaning tweets for 2022-{month}...")

    with open(f"corpora/clean-tweets/clean-tweets-2022-{month}.txt", 'w', encoding='utf-8') as f:
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

    perc = (i / numtweets) * 100
    print(f"{perc}% of tweets were identified as non-German in 2022-{month} (that is {i} out of {numtweets})")


months = ['03', '02', '01']

for month in months:
    preprocess(month)
