import nltk
#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if w not in stop_words]

print("Input:")
print(word_tokens)
print()
print("Output:")
print(filtered_sentence)