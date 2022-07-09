import os
import json
from cleantext import clean
from tqdm import tqdm
from langdetect import detect


class Preprocessing:
    ''' Preprocessing of each tweet in a month and save cleaned tweets in text file
    Removes words containing particular characters (e.g. @ for tweets)
    Performs a standard sentence cleaning protocol from cleantext
    Ensures saved tweets are identified as German after cleaning
    '''

    def __init__(self, date):
        self.tweets_file = date
        self.RECORDINGS_DIR = f"corpora/zenodo-tweets/german-tweet-sample-{date}/"
        self.CLEAN_DIR = f"corpora/cleaned-tweets/tweets-{self.tweets_file}-test.txt"
        self.tweets = self.extraction()[0:100]

    def extraction(self):
        '''
        Method to extract all tweets from the downloaded JSON files
        :return: List of tweets
        '''
        for count, recording in enumerate(os.listdir(self.RECORDINGS_DIR)):

            self.tweets = []

            RECORDING_DIR = os.path.join(self.RECORDINGS_DIR, recording)
            json_file = os.listdir(RECORDING_DIR)[0]
            JSON_DIR = os.path.join(RECORDING_DIR, json_file)

            with open(JSON_DIR) as f:
                data = json.load(f)

            print(
                f"Writing text for {len(data)} tweets in file number {count + 1}/{len(os.listdir(self.RECORDINGS_DIR))}")

            for tweet in data:
                if "text" in tweet:
                    tweet = tweet["text"].replace("\n", " ")
                    self.tweets.append(tweet)

        return self.tweets

    def clean(self):
        '''
        Cleaning pipline: cleaning, language detection and removal
        '''
        print(f"Cleaning tweets for {self.tweets_file}...")

        self.cleaned_tweets = self.cleanlan()

        with open(self.CLEAN_DIR, 'w', encoding='utf-8') as f:
            for tweet in self.cleaned_tweets:
                f.write(tweet + "\n")

        self.stats()

    def cleanbasic(self):
        '''
        Cleaning using the cleantext library
        :return: list of cleaned tweets
        '''

        print("Cleaning using the cleantext library...")
        clean_tweets = []
        for tweet in tqdm(self.tweets):
            clean_tweet = clean(tweet,
                                lower=False,
                                no_urls=True,
                                no_emoji=True,
                                no_emails=True,
                                no_phone_numbers=True,
                                # no_numbers=True,
                                lang='de',
                                )
            clean_tweets.append(clean_tweet)
        return clean_tweets

    def cleanrem(self):
        '''
        List of tweets with words with special characters removed
        :return: list of tweets
        '''

        print("Removing words with special characters...")

        remove = ['@', '*']
        clean_tweets = []
        for tweet in tqdm(self.cleanbasic()):
            words = tweet.split()
            words_clean = []

            for w in words:
                if not any((r in w) for r in remove):
                    words_clean.append(w)
            clean_tweet = ' '.join(words_clean)

            clean_tweets.append(clean_tweet)
        return clean_tweets

    def cleanlan(self):
        '''
        Method to remove tweets that do not identify as German after cleaning
        :return: list of tweets
        '''
        print("Removing non-german tweets...")

        clean_tweets = []
        for tweet in tqdm(self.cleanrem()):
            try:
                if detect(tweet) != 'de':
                    continue
            except:
                continue

            clean_tweets.append(tweet)

        return clean_tweets

    def stats(self):
        '''
        Method to generate and print some basic stats about how many tweets kept
        '''
        numtweets = len(self.tweets)
        numcleantweets = len(self.cleaned_tweets)
        perc = (numcleantweets / numtweets) * 100
        print("STATS REPORT:")
        print(
            f"{perc}% of tweets were removed from {self.tweets_file} (that is {numcleantweets} out of {numtweets})")


dates = ['2022-01']

if __name__ == "__main__":
    for date in dates:
        C = Preprocessing(date)
        C.clean()