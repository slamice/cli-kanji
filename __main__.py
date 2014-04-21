#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import random

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
    print random.choice(kanji)


#def remove_kanji(kanji):
#    stream = open(KANJI_YAML, 'w')

#def reset_ignore_list():

# Get input from user
if __name__ == '__main__':
    get_random_kanji('')

# -l specify level
# -i adds kanji to ignore list
# Default fetches random kanji
# optional: specify Kanji