Translate a word/phrase from german to english using the first result from dict.cc.

## Requirements
This requires python 3 and will _NOT_ run under python 2.

## Installation instructions

Supply a tab delimited dictionary at $XDG\_DATA\_HOME/translate\_de\_en/dictionary.txt.
The first column is the german word and the second column is the english word.

    pip install git+https://github.com/roberttstephens/translate_de_en.git


## Usage

    usage: translate_de_en.py [-h] [--refresh] word
    
    Translate a german word to english.
    
    positional arguments:
      word        The word to translate to german.
    
    optional arguments:
      -h, --help  show this help message and exit
      --refresh   Refresh the database.


## Examples

    translate_de_en.py freund
