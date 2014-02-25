import os
import time

def mm(x,y): # mouse move
  temp = "xte 'mousemove " + str(x) + " " + str(y) + "'"
  os.system(temp) 
  #locate()
  time.sleep(.1)

def mc(button):
  temp = "xte 'mouseclick " + str(button) + "'"
  os.system(temp) 
  time.sleep(.1)

def mmc(button, amount, pause): # Multi mouse click, button, amount pressed, pause between clicks
  ticker = int(amount)
  temp = "xte 'mouseclick " + str(button) + "'"
  while ticker != 0:
    os.system(temp) 
    time.sleep(int(pause))
    ticker = ticker - 1

def md(button):  # mouse button down
  temp = "xte 'mousedown " + str(button) + "'"
  os.system(temp) 
  time.sleep(.1)

def mu(button):  # mouse up 
  temp = "xte 'mouseup " + str(button) + "'"
  os.system(temp) 
  time.sleep(.1)

def k(j): # key a phrase, this will tap in an entire phrase, sentence, paragraph or epic
  temp = "xte 'str " + str(j) + "'"
  os.system(temp) 
  time.sleep(.1)

def C(J): # key in a named key (i.e. Enter, Delete, F5, Backspace)
  temp = "xte 'key " + str(J) + "'"
  os.system(temp) 
  time.sleep(.1)
 
def s(S): # sleep command
  temp = 'sleep ' + str(S)
  os.system(temp) 
  time.sleep(.1)

def locate():
  os.system('xdotool getmouselocation --shell')
  time.sleep(.1)
 
def URL(url):
  os.system(url)
  time.sleep(.1)

def scrolldown(D):
  mm(1018,568)
  count = D
  while count != 0:
    mc(1)
    count = count - 1
    time.sleep(.5)

def scrollup(U):
  mm(1018,150)
  count = U
  while count != 0:
    mc(1)
    count = count - 1
    time.sleep(.5)
