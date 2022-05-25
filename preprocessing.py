from cleantext import clean
from tqdm import tqdm

print("Reading tweets...")
with open("corpora/extracted-tweets/all-tweets-2022-04.txt", 'r', encoding='utf-8') as f:
    tweets = f.readlines()

remove = ['@', '*']

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

        f.write(tweet_clean)
        f.write("\n")
# print(tweets_clean)
# remove = ['@', 'https://']
#
# pp.pprint(tweets)
# tweets_clean = []
# for tweet in tweets:
#     tweet = tweet.replace("&amp;", " & ")
#     words = tweet.split()
#     words_clean = []
#     for word in words:
#         if not any((r in word) for r in remove):
#             words_clean.append(word)
#     tweet_clean = ' '.join(words_clean)
#     tweets_clean.append(tweet_clean)
