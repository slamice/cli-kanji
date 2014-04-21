#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import random
import argparse
import pprint


KANJI_YAML = 'kanji.yaml'
IGNORE_LIST = 'ignore_list.yaml'

def random_level():
    return 'N' + str(random.randint(1, 5))

def get_random_kanji(level):
    f = open(KANJI_YAML, 'r')
    dataMap = yaml.safe_load(f)
    f.close()

    if level == '':
        level = random_level()

    kanji = dataMap[level]
    selection = random.choice(kanji)
    char = selection['kanji']

    print 'What does '+ char + ' mean?'
    var = raw_input()

    if iequal(var, selection['Meaning']):
        print '\n-==*== Yes! You got it! ==*==-\n'
        print_kanji(selection)
    else:
        print '\nNo, try another one :( \n'
        print_kanji(selection)

# Equals (ignore case)
def iequal(a, b):
    try:
       return a.upper() == b.upper()
    except AttributeError:
       return a == b


def print_kanji(selected):
    print 'Kanji: '+ selected['kanji']
    print 'Onyomi: '+ selected['Onyomi']
    print 'Kunyomi: '+ selected['Kunyomi']
    print 'Meaning: '+ selected['Meaning']

# Get input from user
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    usage = "usage: %prog [options]"

    parser.add_argument("level", type=str,
                    help="select JLPT level from  N1|N2|...|N5",
                    default='N5')

    args = parser.parse_args()

    get_random_kanji(args.level)

# -i adds kanji to ignore list
# Default fetches random kanji
# optional: specify Kanji