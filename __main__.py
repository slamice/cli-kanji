#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


def get_random_kanji(level):
    stream = open("kanji.yaml", "r")
    docs = yaml.load_all(stream)
    for doc in docs:
        for k,v in doc.items():
            if k == 'kanji':
                print k, "->", v.encode('utf-8')
        print "\n",


if __name__ == '__main__':
    get_random_kanji('N5')

# specify level
# Default randomly fetches kanji
# optional: specify Kanji