from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
from pymystem3 import Mystem
from nltk.corpus import stopwords, brown
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer
import nltk
import re
import time
from os import listdir

def preproccesor(data):
    #препроцесссор текста
    m = Mystem()
    # переход на нижний регистр
    def to_lower(text):
        text = text.lower()
        return text
    
    # очищение текста
    def clean_text(lower_case):
        words  = nltk.word_tokenize(lower_case)
        punctuations = ['.', ',', '/', '!', '?', ';', ':', '(',')', '[',']', '-', '_', '%']
        punctuations = re.sub(r'\W', ' ', str(lower_case))
        stop_words  = stopwords.words('russian')
        w_num = re.sub('\w*\d\w*', '', lower_case).strip()
        lower_case = re.sub(r'\s+[a-zA-Z]\s+', ' ', lower_case)
        lower_case = re.sub(r'\s+', ' ', lower_case, flags=re.I)
        lower_case = re.sub(r'^b\s+', '', lower_case)
        lower_case = re.sub(r'^b\s+', '', lower_case)
        keywords = [word for word in words if not word in stop_words  and word in punctuations and  word in w_num]
        return keywords
    
    # лемматизация текста
    def lemmatize_sentence(text):
        lemmas = m.lemmatize(text)
        return "".join(lemmas).strip()
    
    data = str(data)
    data = to_lower(data)
    text = clean_text(data)

    sentence = ' '.join(text)
    start = time.time()
    clean_data = lemmatize_sentence(sentence)
    print(time.time() - start)
    return sentence