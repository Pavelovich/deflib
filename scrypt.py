#!/usr/bin/python
import string

# rot13 function
def rot13(rot13string):
  rot13cipher = string.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM')
  return string.translate(rot13string, rot13cipher)

# QWERTY cipher functions
def qwertyCrypt(qcrString):
  qcrCipher = string.maketrans('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                               'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
  return string.translate(qcrString, qcrCipher)

def qwertyCipher(qciString):
  qciCipher = string.maketrans('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM',
                               'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
  return string.translate(qciString, qciCipher)
