import pickle
import re
import string
from collections import defaultdict

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


PATH = __file__.replace("function.py", "")


class CleanText(str):
    def __init__(self, text=''):
        self.options = defaultdict(bool)

    def __call__(self, text=''):
        if self.options['full_transform']:
            text = self.remove_whit_re(text)
            text = self.remove_punctuation(text)
            text = self.remove_stopwords(text)
            text = self.apply_stemming(text)
            return text
        text = self.remove_whit_re(text)
        text = self.remove_punctuation(text)
        text = self.remove_one_char(text)
        return text

    def set_options(self,
                    simple=False,
                    full_transform=False,
                    ):
        self.options['simple'] = simple
        self.options['full_transform'] = full_transform

    def remove_one_char(self, text: str = ''):
        if self:
            text = self + ' ' + text
        return ' '.join([word for word in text.split(' ') if len(word) > 1 or len(word) > 18])

    def remove_inicial(self, text: str = ''):
        if self:
            text = self + ' ' + text
        return re.sub("\.*\s[A-ZА-Я]\.", "", text)

    def remove_whit_re(self, text: str = ''):
        if self:
            text = self + ' ' + text
        return re.sub("[A-ZА-Я]\.|http[://A-Za-zА-Яа-я\.]*|www.*[A-Za-z]+\.[a-zA-Z]+", "", text)

    def lower(self, text: str):
        if self:
            text = self + ' ' + text
        return text.lower()

    def remove_punctuation(self, text: str = ''):
        if self:
            text = self + ' ' + text
        whitespace = string.whitespace.replace(' ', '')
        punctuations = string.punctuation + '«»'
        digits = string.digits
        schars = whitespace + punctuations + digits
        text = text.replace('-', ' ')
        return "".join([char for char in text.lower() \
                        if char not in schars])

    def remove_stopwords(self, text: str = ''):
        if self:
            text = self + ' ' + text
        stemmer = SnowballStemmer('russian')
        stop_words = stopwords.words('russian')
        return " ".join([stemmer.stem(word) for word in text.split(' ') if word not in stop_words])

    def apply_stemming(self, text: str = ''):
        if self:
            text = self + ' ' + text
        stemmer = SnowballStemmer('russian')
        return " ".join(stemmer.stem(word) for word in text.split(' '))

    def transform(self, lst_good_words: list, text: str = ''):
        if self:
            text = self + ' ' + text
        return " ".join([words for words in text.split(' ') if words in lst_good_words])


def predict(message):
    text = message
    with open(f"{PATH}modelRidge.sav", "rb") as file:
        modelFT = pickle.load(file)
        cleaner = CleanText()
        clean_text = cleaner(text)
        topic_predict = modelFT.predict(x)
        topic_predict = topic_predict[0][0].replace('__label__', '').replace('_', ' ')
        return topic_predict
