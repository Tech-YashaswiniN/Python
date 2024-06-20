import nltk

# TOkenization

# nltk.download('punkt')

text1 = "Hello it's me yashaswini. How are you all."
print(text1)

# Splitting the text into words
print(nltk.word_tokenize(text1))

# Splitting the text into sentences
text2="Python is a programming language. Pyhton is a open source. Pyhton is free"
print(nltk.sent_tokenize(text2))