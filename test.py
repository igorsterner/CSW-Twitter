import nltk
import pprint as pp
from cleantext import clean

tweet = 'Danke &amp; schön, Dich in der "Arche Freiheit" zu haben 😊'

print(clean(tweet,
            lower = False,
            no_urls=True,
            no_emoji = True,
            lang= 'de',
            no_emails = True,
            no_phone_numbers = True,
            ))