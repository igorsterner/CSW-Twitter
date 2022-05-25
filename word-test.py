import nltk
import enchant
d = enchant.Dict("en_US")

# English Dictionary
with open("dictionaries/old/1000-en.txt", 'r', encoding ='utf8') as f:
    englishwords = f.read().splitlines()

# English Dictionary
with open("dictionaries/old/1000-de.txt", 'r', encoding ='utf8') as f:
    germanwords = f.read().splitlines()

eng_words = englishwords
de_words = germanwords

# German words in text
with open("corpora/wmt-14-de.txt", 'r', encoding ='utf8') as f:
    corpa = f.read()
    corpa_sent = f.readlines()

for sentence in corpa_sent:
    for word in nltk.word_tokenize(sentence):
        if word not in de_words and d.check(word):
            print(word)
            print(sentence)
            print("------")
            continue

# germ_sent = nltk.sent_tokenize(german)
corpa_words = nltk.word_tokenize(corpa)

print(corpa_words)

# corpa_words = 70,763 deutsche wörter aus beispieltext
# de_words = top 1000 deutsche Wörter
# d.check()/: -> bool = englischer Wörterbuchprüfer

output = {}
for word in list(corpa_words):
    if word not in de_words and d.check(word):
        if word in output:
            output[word] += 1
        else:
            output[word] = 1

print(output)

for w in sorted(output, key=output.get, reverse=True):
    print(w, output[w])

# common = list(eng_words & germ_words)
#
# removal = ["I", "die", "am", "will", "in", "a", "war", "an", "was", "also", "so", "man", "fast", "hat", "all"]
#
# for r in removal:
#     common.remove(r)
#
# print(common)
#
# for sent in germ_sent:
#     words = nltk.word_tokenize(sent)
#     # for word in common:
#     if "separate" in words:
#         # print(word)
#         print(sent)
