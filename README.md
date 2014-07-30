Translate a word/phrase from german to english using a dictionary lookup. Not intended for public use. If you wish to use this, you must supply your own tab delimited dictionary file at $XDG\_DATA\_HOME/translate\_de\_en/dictionary.txt.

## Requirements
This requires python 3 and will _NOT_ run under python 2.

## Installation instructions

Supply a tab delimited dictionary at $XDG\_DATA\_HOME/translate\_de\_en/dictionary.txt.
The first column is the german word and the second column is the english word.

    pip install git+https://github.com/roberttstephens/translate-de-en.git


## Usage

    usage: translate_de_en.py [-h] [--refresh] [--multiple] word
    
    Translate a german word to english.
    
    positional arguments:
      word        The word to translate to german.
    
    optional arguments:
      -h, --help  show this help message and exit
      --refresh   Refresh the database.
      --multiple  Return up to 3 matching english words



## Examples

    translate_de_en freund
    translate_de_en --refresh --multiple freund
