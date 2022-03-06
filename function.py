
import string
import re
from nltk.corpus import stopwords
import sklearn
import pickle
import numpy as np
from nltk.stem.snowball import SnowballStemmer 


stemmer = SnowballStemmer("russian") 
russian_stopwords = stopwords.words("russian")

PATH = __file__.replace("function.py","")

def lower_text(text:str):
    return text.lower()

def clean_text(text:str):
    punctuation = string.punctuation
    punctuation+="«»"
    return text.translate(str.maketrans('', '', punctuation))
    
def del_mul_spaces(text:str):
    return re.sub(r"\s+"," ",text)

def del_number(text:str):
    numbers = re.compile("[0-9]+")
    return re.sub(numbers,"",text)

def del_other_chars(text:str):
    substr = re.compile(r"[a-zA-ZА-Яа-я]\.[a-zA-ZА-Яа-я]\.")
    return re.sub(substr,"",text)

def del_stopwords(text:str):
    list_words = text.split(" ")
    result = [token for token in list_words if token not in russian_stopwords]
    return " ".join(result)

def stemm_text(text:str, stemmer=stemmer):
    return " ".join((stemmer.stem(token) for token in text.split(" ")))

def del_one_char(text:str):
    return " ".join([token for token in text.split(" ") if len(token)>1])


def cleaning_text(text:str):
    functions = [lower_text,del_other_chars,clean_text,del_mul_spaces,del_number]
    for function in functions:
        text = function(text)
    return text
    
def setting_words(text:str):
    text = del_one_char(stemm_text(del_stopwords(text)))
    return text

def predict(message):
  text = message
  with open(f"{PATH}modelRidge.sav","rb") as file, \
  open(f"{PATH}coef.sav","r") as file_coef, \
  open(f"{PATH}vectorizer.sav","rb") as file_vect:
      modelRL = pickle.load(file)
      vectorizer = pickle.load(file_vect)
      coef = file_coef.read().split(" ")
      coef = [int(tocken)  for tocken in coef if tocken!=""] 
      cleantext = np.array(setting_words(cleaning_text(text))).reshape(1)
      x = vectorizer.transform(cleantext)[:,coef]
      predict = modelRL.predict(x)
      return(predict[0].upper())
      

      
