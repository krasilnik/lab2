
#Create a class that performs statistical processing of a text file
#- counting characters, words, sentences, etc. Determine the required
#attributes-data and attributes-methods in class for working with the text file.

import re


class TextReader:

    @staticmethod
    def characters(name):
        f = open(name)
        text = f.read()
        f.close()
        return len(text)

    @staticmethod
    def count_special_characters(symbol, name):
        f = open(name)
        text = f.read()
        f.close()
        return text.count(symbol)

    @staticmethod
    def words(name):
        f = open(name)
        text = f.read()
        f.close()
        return len(text.split())

    @staticmethod
    def sentences(name):
        f = open(name)
        text = f.read()
        f.close()
        result = re.split(r"[.?!\n]+", text)
        return len(list(filter(lambda x: x, result)))

    @staticmethod
    def show_text(name):
        f = open(name)
        text = f.read()
        f.close()
        return text