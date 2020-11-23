import joblib
from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,

    Doc
)
from Object_detection_image import get_image
from loguru import logger


segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
addr_extractor = AddrExtractor(morph_vocab)

class EVENT:
    Fire = "F"
    Dtp = "D"
    Vodosnabgenie = "WS"
    Trash = "T"
    Light = "L"
    Roads = "R"
    Lakes_and_Rivers = "LR"

    VALUES = {Lakes_and_Rivers, Fire, Dtp, Light, Roads, Vodosnabgenie, Trash}

class DANGER:
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    VALUES = {LOW, MEDIUM, HIGH}

def get_danger_level(text: str) -> int:
    if text == EVENT.Light or text == EVENT.Vodosnabgenie or text == EVENT.Trash:
        return DANGER.LOW
    elif text == EVENT.Lakes_and_Rivers or text == EVENT.Roads:
        return DANGER.MEDIUM
    elif text == EVENT.Dtp or text == EVENT.Fire:
        return DANGER.HIGH

def classify(text: str) -> str:
    classificator = joblib.load('C:\\Users\\Lancetnik\\Desktop\\python\\hacks\\digital-lead\\python-backend\\project\\message_getter\\model\\models\\classificator.sav')
    vectorizer = joblib.load('C:\\Users\\Lancetnik\\Desktop\\python\\hacks\\digital-lead\\python-backend\\project\\message_getter\\model\\models\\vectorizer.sav')
    # preproc = joblib.load('C:\\Users\\Lancetnik\\Desktop\\python\\hacks\\digital-lead\\python-backend\\project\\message_getter\\model\\models\\preproccesor.sav')
    # text = preproc(text)
    vector_text = vectorizer.transform([text])
    cl = classificator.predict(vector_text)
    if  cl == 0: return EVENT.Light
    elif cl == 1: return EVENT.Lakes_and_Rivers
    elif cl == 2: return EVENT.Roads
    elif cl == 3: return EVENT.Trash
    elif cl == 4: return EVENT.Dtp
    elif cl == 5: return EVENT.Fire
    elif cl == 6: return EVENT.Vodosnabgenie

def find_address(text: str) -> str:
    def get_addres(match):
        if not match: return ''
        adres = ''
        for i in match.fact.parts:
                adres += i.type+' '+i.value+' ' 
        return(adres[:len(adres)-1])
    match = addr_extractor.find(text)
    return get_addres(match)

def get_file(file):
    if get_image(file) == 0:
        return EVENT.Dtp
    if get_image(file) == 1:
        return EVENT.Fire