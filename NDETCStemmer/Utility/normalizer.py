from nltk.tokenize import RegexpTokenizer

def normalize(normalizerInput, stopword=False,fromFile=False):
    words=normalizerInput
    if fromFile:
        with open(normalizerInput, encoding="utf8") as f:
            words = f.read().replace('\n',' ').strip()

    tokenizer = RegexpTokenizer("[\w\-]+")
    words = tokenizer.tokenize(words.lower())
    if stopword:
        list_stopword = set(line.rstrip('\n') for line in open('./NDETCStemmer/DictFile/stopwords.txt', encoding="utf8"))
        for word in words:
            if word in list_stopword:
                words.remove(word)

    return words