#!/usr/bin/python3

FILE = 'file.txt'
NEEDLE = 'Test123ABC'

import codecs

if __name__ == '__main__':
  with codecs.open(FILE, 'r', 'utf-8', 'strict') as fh:
    for line in fh:
      if NEEDLE in line:
        print(line.strip())