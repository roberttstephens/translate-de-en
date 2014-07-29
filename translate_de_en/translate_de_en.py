#!/usr/bin/env python3
"""
Translate a german word to english.
"""
import argparse
import re
import sqlite3
import os
import xdg
from xdg import BaseDirectory

DIRECTORY = xdg.BaseDirectory.save_data_path('translate_de_en')

CONN = sqlite3.connect(os.path.join(DIRECTORY, 'dictionary.db'))
C = CONN.cursor()

def get_dict():
    """
    Convert the text file into a python dictionary.
    """
    dictionary = {}
    with open(os.path.join(DIRECTORY, 'dictionary.txt')) as dictionary_file:
        for line in dictionary_file:
            german, english, _ = line.split("\t")
            german = re.sub(r'{.*}', '', german)
            german = re.sub(r'\[.*\]', '', german)
            german = german.strip()
            german = german.lower()
            dictionary[german] = english
    return dictionary

def get_word(word):
    """
    Get the english word when given a german word.
    """
    C.execute(
        "SELECT english FROM dictionary WHERE german=?",
        tuple([word.lower()])
    )
    result = C.fetchone()
    if result:
        return result[0]

def refresh_db():
    """
    Save the text file into a sqlite database and table.
    """
    dictionary = get_dict()
    C.execute(
        '''
        DROP TABLE if exists dictionary
        '''
    )
    C.execute(
        '''
        CREATE TABLE dictionary (german text, english text)
        '''
    )
    dictionary = get_dict()
    C.executemany('INSERT INTO dictionary VALUES (?, ?)', dictionary.items())
    CONN.commit()


def main():
    """
    Translate a german word to english.
    """
    parser = argparse.ArgumentParser(
        description='Translate a german word to english.'
    )
    parser.add_argument(
        '--refresh',
        action='store_true',
        help='Refresh the database.'
    )
    parser.add_argument('word', help='The word to translate to german.')
    args = parser.parse_args()
    if args.refresh:
        refresh_db()
    english = get_word(args.word)
    if english:
        print(english)

if __name__ == '__main__':
    main()
