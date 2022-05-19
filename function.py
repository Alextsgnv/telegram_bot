import pickle
import re
import string

import numpy as np
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


def lower_text(text: str) -> str:
    """Возвращает строку в нижнем регистре."""
    return text.lower()


def clean_text(text: str) -> str:
    """Возвращает строку без знаков пунктуации и препинаний."""
    punctuation = string.punctuation
    punctuation += "«»"
    return text.translate(str.maketrans('', '', punctuation))


def del_mul_spaces(text: str) -> str:
    """Заменяет множественные пробулы одним, и возвращает строку."""
    return re.sub(r"\s+", " ", text)


def del_number(text: str) -> str:
    """Возвращает строку без чисел."""
    numbers = re.compile("[0-9]+")
    return re.sub(numbers, "", text)


def del_other_chars(text: str) -> str:
    """Удаляет символы похожие на url ссылки."""
    substr = re.compile(r"[a-zA-ZА-Яа-я]\.[a-zA-ZА-Яа-я]\.")
    return re.sub(substr, "", text)


def del_stopwords(text: str) -> str:
    """Удаляет стоп слова."""
    russian_stopwords = stopwords.words("russian")
    list_words = text.split(" ")
    result = [token for token in list_words if token not in russian_stopwords]
    return " ".join(result)


def stemm_text(text: str) -> str:
    """Возвращает строку после стеминг преобразования."""
    stemmer = SnowballStemmer("russian")
    return " ".join((stemmer.stem(token) for token in text.split(" ")))


def del_one_char(text: str) -> str:
    """Возвращает строку, из которой удалены одиночные символы."""
    return " ".join([token for token in text.split(" ") if len(token) > 1])


def cleaning_text(text: str) -> str:
    """Применяет вышеуказанные функции к строке, и возвращает отформатированную строку."""
    functions = [lower_text, del_other_chars, clean_text, del_mul_spaces, del_number]
    for function in functions:
        text = function(text)
    return text


def setting_words(text: str) -> str:
    """Применяет стемминг к строке, удаляет одиночные символы и возвращает строку."""
    text = del_one_char(stemm_text(del_stopwords(text)))
    return text


def predict(message: str) -> str:
    """Преобразует текст из сообщения, применяет к полученой строке обученную модель,
    возвращает прогноз модели."""
    PATH = __file__.replace("function.py", "")
    text = message
    with open(f"{PATH}modelRidge.sav", "rb") as file, \
            open(f"{PATH}coef.sav", "r") as file_coef, \
            open(f"{PATH}vectorizer.sav", "rb") as file_vect:
        modelRL = pickle.load(file)
        vectorizer = pickle.load(file_vect)
        coef = file_coef.read().split(" ")
        coef = [int(tocken) for tocken in coef if tocken != ""]
        cleantext = np.array(setting_words(cleaning_text(text))).reshape(1)
        x = vectorizer.transform(cleantext)[:, coef]
        predict = modelRL.predict(x)
        return (predict[0].upper())
