import auto
import os
import masterca
import time


def addcode():
  counter = 0
  file = open('codes.txt', 'r')
  x = file.read()
  for line in x:
    if counter != 10:
      if line != " ":
        auto.k(line)
      elif line == " ":
        auto.C("Return")

addcode()
