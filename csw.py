import nltk
from tqdm import tqdm

source = "corpora/cleaned-tweets/tweets-"
eval = "corpora/csw/csw-"

class CSW:

    def __init__(self, csw_dict):
        with open("dictionaries/" + csw_dict, 'r', encoding='utf-8') as f:
            self.words = f.read().splitlines()

        removal = ['owo', 'uwu']
        for r in removal:
            self.words.remove(r)

    def csw_tweets(self, date):

        with open(source + date + '.txt', 'r', encoding='utf-8') as f:
            tweets = f.read().splitlines()

        # tweets = tweets[:1000]

        len_tweets = len(tweets)
        i = 0
        c = 0
        csw = {}

        print(f"Tweets loaded from {date} and are being processed")

        with open(eval + date + '.txt', 'w', encoding='utf-8') as f:
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
                    elif word.lower() in self.words:
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

        print(
            f"{date}: outputted {c} Code-switched tweets out of {len_tweets} which accounts for {100 * c / len_tweets}% of all tweets")


if __name__ == "__main__":
    date = '2022-01'
    C = CSW("csw.txt")
    C.csw_tweets(date)
