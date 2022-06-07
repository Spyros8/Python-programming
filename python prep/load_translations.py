""" Translation

Author: Josiah Wang
"""

import pprint # for pretty printing dictionaries

def load_translations(filename):
    """ Load a dict of translations from a text file.
    
    Each line in the text file should contain a set of words separated by tabs.
    
    The first word is the word in the source language, and the remaining words (one or more) are possible translations of the word in the target language.
    
    Args:
        filename (str) : The path to the translation lookup 
        
    Returns:
        dict : keys should be the word in the source language, value is a list of words in the target language
    """
    translation_dict = {}
    
    with open(filename, encoding = "utf8") as textfile:
        lines = textfile.readlines()
        for line in lines:
            words = line.strip().split("\t")
            source_word = words[0]
            target_words = words[1:]
            translation_dict[source_word] = target_words
    
    return translation_dict


def translate(sentence, translation_dict):
    """ Translate a sentence given a translation dictionary
    
    Args:
        sentence (str) : Sentence to translate
        translation_dict (dict) : keys are words in the source language, value is a list of words in the target language
        
    Returns:
        str : the sentence in the target language.
    """

    words = sentence.split()
    translated_words = []
    for word in words:
        if word in translation_dict:
            translation = translation_dict[word][0]
            translated_words.append(translation)
    return " ".join(translated_words)
    
    
def test_load():
    result = load_translations("french.txt")
    pprint.pp(result)
    
    assert len(result) == 18
    assert result["boy"] == ["garçon", "fils"]
    assert result["is"] == ["est"]
    

def test_translate():
    translation_dict = {
        "a": ["un", "une"],
        "and" : ["et"],
        "ball" : ["balle", "ballon", "boule"]
    }
    
    result = translate("a ball and a ball", translation_dict)
    expected = "un balle et un balle"
                
    assert result == expected


def test_pipeline():
    translation_dict = load_translations("french.txt")
    result = translate("a boy with a ball in the park", translation_dict)
    print(result)
    expected = "un garçon avec un balle dans le parc"
    assert result == expected
    
test_load()
test_translate()
test_pipeline()
