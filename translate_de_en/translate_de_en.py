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

def get_words(word):
    """
    Get up to 3 english words matching a german word.
    """
    C.execute(
        "SELECT english FROM dictionary WHERE german=? LIMIT 3",
        tuple([word.lower()])
    )
    result = C.fetchall()
    if result:
        return [item[0] for item in result]

def refresh_db():
    """
    Save the text file into a sqlite database and table.
    """
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
    with open(os.path.join(DIRECTORY, 'dictionary.txt')) as dictionary_file:
        for line in dictionary_file:
            sections = line.split("\t")
            german = sections[0]
            english = sections[1]
            german = re.sub(r'{.*}', '', german)
            german = re.sub(r'\[.*\]', '', german)
            german = german.strip()
            german = german.lower()
            C.execute('INSERT INTO dictionary VALUES (?, ?)', (german, english))
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
    parser.add_argument(
        '--multiple',
        action='store_true',
        help='Return up to 3 matching english words'
    )
    parser.add_argument('word', help='The word to translate to german.')
    args = parser.parse_args()
    if args.refresh:
        refresh_db()
    if args.multiple:
        words = get_words(args.word)
        if words:
            print(','.join(words))
    else:
        english = get_word(args.word)
        if english:
            print(english)

if __name__ == '__main__':
    main()
