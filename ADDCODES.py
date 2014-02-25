import masterca
import auto
import os
import time

file = open('codes.txt', 'r')
x = file.read()

def addcode():
  counter = 0
  auto.URL('firefox http://web3.castleagegame.com/castle_ws/army.php')
  time.sleep(8)
  auto.scrolldown(8)
  auto.mm(500,500)
  auto.mc(1)
  time.sleep(1)
  for line in x:
    if line != " ":
      auto.k(line)
    else:
      auto.C("Return")
      counter = counter + 1
      auto.scrolldown(4)
      auto.mm(500,480)
      auto.mc(1)
      time.sleep(1)

addcode()
