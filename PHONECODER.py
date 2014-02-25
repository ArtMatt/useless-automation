import masterca
import auto
import os
import time
#import date.time
import keyboard

file = open('codes.txt', 'r')
x = file.read()

def addcode():
  print "FROM PHONE CLOSE: vnc to phone"
  masterca.sshPhone()
  print "FROM PHONECLOSE: closing phone apps"
  masterca.phoneHome()
  masterca.phoneClose()
  time.sleep(1) 
#  auto.mm(553,139)
#  auto.mc(1)	
#  print "consider everything"
#  time.sleep(20)
  print "clicking CASTLE AGE!?"
  masterca.phoneCA('matthewgcasey@gmail.com','Stew')
  time.sleep(3)
  print "xxentering codes now"
  masterca.coder()
  for line in x:
    print "for line in x"
    time.sleep(1)
    if line != " ":
      print "typing letter"
      time.sleep(4)
      auto.k(line)
    else:
      auto.mm(585,236)
      print "confirming invite" 
      auto.mc(1)
      time.sleep(12)
      print "closing action message?"
      auto.mm(631,202)
      auto.mc(1)
      time.sleep(3)
      auto.mm(602,331)
      auto.mc(1)
      time.sleep(2)
      auto.mm(444,358)
      auto.mc(1)
      time.sleep(5)



 
###      gorsedicka = raw_input(" DOCUMENT FINDINGS")
###      successes = successes + 1
###      now = datetime.datetime.now()
###      print "Thusfar: ", successes#, "  elapsed time", now - then, " total", now - started
###
###def commune(coords):
###  if coords[-1] == 3:
###    master.zip(6, coords[1])
###  elif coords[-1] == 2:
###    master.zip(6, int(coords[1]))
###  else:
###    master.zip(6, int(coords[1]))
  #ask = raw_input(" HMM?")
  #os.system("xte 'keydown Alt_L' 'key F4' 'keyup Alt_L'")
  #os.system("xte 'keydown Alt_L' 'key F4' 'keyup Alt_L'")

addcode()
