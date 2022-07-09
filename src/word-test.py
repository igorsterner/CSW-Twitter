import nltk
import enchant

DE_TEXT_DIR = "corpora/wmt-14-de.txt"
EN_DICT_DIR = "dictionaries/old/1000-en.txt"
DE_DICT_DIR = "dictionaries/old/1000-de.txt"


class WordTest:
    ''' Simple class to quickly search for potentially Code-switched words
    and gather some basic statistics about them
    '''

    def __init__(self):
        # English Dictionary
        with open(EN_DICT_DIR, 'r', encoding='utf8') as f:
            self.eng_words = f.read().splitlines()
        # Or from library
        self.d = enchant.Dict("en_US")
        # German Dictionary
        with open(DE_DICT_DIR, 'r', encoding='utf8') as f:
            self.de_words = f.read().splitlines()

        # German words in text
        with open(DE_TEXT_DIR, 'r', encoding='utf8') as f:
            self.text = f.readlines()

    def csw_checker(self):
        ''' Simple method to find CSW tweets
        Finds tweets with at least one word in English Dictionary but not in German Dictionary
        :return: Dictionary of tweets and single corresponding use of code-switching
        '''

        csw = {}
        for sentence in self.text:
            for word in nltk.word_tokenize(sentence):
                if word not in self.de_words and self.d.check(word):
                    csw[sentence] = word
                    continue
        return csw

    def csw_count(self):
        ''' Simple method to return counts of CSW words
        :return: list of most common words
        '''

        word_count = {}

        for word in self.csw_checker().values():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        return sorted(word_count, key=word_count.get, reverse=True)

if __name__ == "__main__":
    w = WordTest()
    print(w.csw_checker())
    print(w.csw_count())