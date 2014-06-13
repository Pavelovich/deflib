#!/usr/bin/python

import random

def alex():
  randAlex = random.randint(0,13)
  alexName = [ ['Alex',        'n'],
               ['Alexander',   'm'],
               ['Alexandra',   'f'],
               ['Alessandro',  'm'],
               ['Alessandra',  'f'],
               ['Alejandro',   'm'],
               ['Alejandra',   'f'],
               ['Aleksandr',   'm'],
               ['Aleksandra',  'f'],
               ['Aleksander',  'm'],
               ['Alexandria',  'f'],
               ['Aleksandrina','f'],
               ['Sascha',      'n'],
               ['Sasha',       'n'] ]
  return alexName[randAlex][0]
