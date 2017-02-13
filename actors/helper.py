# coding=utf-8
from __future__ import unicode_literals
import os

RUSSIAN_ENGLISH_SYMBOLS = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'j',
    'з': 'z',
    'и': 'i',
    'й': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'c',
    'ш': 'sh',
    'щ': 'sh',
    'ь': '\'',
    'ы': 'y',
    'ъ': '\'',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',
    'ч': 'ch',
    'ө': 'o',
    'ң': 'n',   
    'ү': 'u',
}


def transform(path):
    def wrapped(instance, filename):

        filename = filename.lower()
        for key in RUSSIAN_ENGLISH_SYMBOLS:
            if key in filename:
                filename = filename.replace(key, RUSSIAN_ENGLISH_SYMBOLS[key])
        return os.path.join(path, filename)

    return wrapped
