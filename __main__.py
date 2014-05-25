#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import argparse
import pprint
import json


KANJI_JSON = 'kanji.json'
IGNORE_LIST = 'ignore_list.json'

def random_level():
    return 'N' + str(random.randint(1, 5))

def get_kanji(level):
    f = open(KANJI_JSON, 'r')
    data = json.load(f)
    f.close()

    if level == '':
        level = random_level()

    selection = random.choice(data[level])
    char = (selection['kanji']).encode('utf8')

    print 'What does '+ char + ' mean?'
    var = raw_input()

    meanings = (selection['meaning']).split(',')

    for meaning in meanings:
        print var
        print meaning
        if iequal(var, meaning):
            print '\n-==*== Yes! You got it! ==*==-\n'
            print_kanji(selection)
            exit()
    else:
        print '\nNo, try another one :( \n'
        print_kanji(selection)

# Equals (ignore case)
def iequal(a, b):
    try:
       return a.upper() == b.upper()
    except AttributeError:
       return a == b

def ignore()


def print_kanji(selected):
    print 'Kanji: '+ (selected['kanji']).encode('utf8')
    print 'Onyomi: '+ selected['onyomi']
    print 'Kunyomi: '+ selected['kunyomi']
    print 'Meaning: '+ selected['meaning']

# Get input from user
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    usage = "usage: %prog [options]"

    parser.add_argument("level", type=str,
                    help="select JLPT level from  N1|N2|...|N5",
                    default='N5')

    parser.add_argument("ignore", type=str,
                    help="select kanji or meaning to ignore",
                    default='')

    args = parser.parse_args()

    get_kanji(args.level)