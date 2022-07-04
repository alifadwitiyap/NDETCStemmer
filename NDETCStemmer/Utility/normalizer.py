from nltk.tokenize import RegexpTokenizer

def normalize(stemmer_input, stopword=False,from_file=False,stopword_file=None):
    words=stemmer_input
    if from_file:
        with open(stemmer_input, encoding="utf8") as f:
            words = f.read().replace('\n',' ').strip()

    tokenizer = RegexpTokenizer("[\w\-]+")
    words = tokenizer.tokenize(words.lower())
    if stopword:
        for word in words:
            if word in stopword_file:
                words.remove(word)

    return words