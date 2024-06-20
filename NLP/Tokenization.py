import nltk
from nltk.corpus import udhr

udhr = nltk.corpus.udhr.words('English-Latin1')
udhr = udhr[:30]
print(udhr)
print("-----------------------------------------------------------------------------------------------------------------------------------------------")
sentneces = nltk.sent_tokenize(" ".join(udhr))
print(sentneces)