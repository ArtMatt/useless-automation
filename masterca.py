import auto
import time
import os

def login(name):
  auto.URL('firefox http://web3.castleagegame.com/castle_ws/connect_login.php')
  time.sleep(10)
  auto.mm(860,160)
  auto.mc(1)
  auto.mm(506,400)
  auto.mc(1)
  time.sleep(1)
  auto.mm(626, 400)
  auto.md(1)
  auto.mm(410,400)
  auto.mu(1)
  auto.C('Delete')
  time.sleep(1)
  auto.k(name)
  auto.C("Tab")
  auto.C("Delete")
  auto.k("Stew")
  auto.C("Return")
  time.sleep(6)
  auto.mm(843,495) # CLOSES ANNOYING MINING MESSAGE
  auto.mc(1)
  time.sleep(2)
  auto.mm(224,450)
  auto.mc(1)

def guildbattleFirst():
  time.sleep(5)
  auto.mm(848,452)
  auto.mm(848,562) 
  auto.mc(1) # Clicks Battle
  time.sleep(4)
  auto.scrolldown(6)
  auto.mm(728,511)
  auto.mc(1) # Click Join Battle
  time.sleep(4)
  auto.mm(507,560)
  time.sleep(1) # DELETE
  auto.mc(1) # Joins Battle
  time.sleep(1) # DELETE
  auto.scrolldown(6)
  time.sleep(4) # DELETE
  auto.mm(515,477)
  time.sleep(1) # DELETE
  auto.mc(1) # Clicks Your Guild
  time.sleep(1) # DELETE
  auto.scrolldown(8)
  auto.mm(431,437)
  auto.mc(1) # Clicks West
  auto.scrolldown(26)
  auto.mm(725,530)
  auto.mc(1) # Heals Emissary
  time.sleep(4)
  auto.mm(503, 543)
  auto.mmc(1,9,2)
 

def guildbattleAfter():
  time.sleep(5)
  auto.mm(848,452)
  auto.mc(1)
  time.sleep(1)
  auto.mm(848,562) 
  auto.mc(1) # Clicks Battle
  time.sleep(4)
  auto.scrolldown(6)
  auto.mm(728,511)
  auto.mc(1) # Click Join Battle
  time.sleep(4)
  #auto.mm(507,560)
  #time.sleep(1) # DELETE
  #auto.mc(1) # Joins Battle
  #time.sleep(1) # DELETE
  auto.scrolldown(6)
  time.sleep(4) # DELETE
  auto.mm(515,477)
  time.sleep(1) # DELETE
  auto.mc(1) # Clicks Your Guild
  time.sleep(1) # DELETE
  auto.scrolldown(8)
  auto.mm(431,437)
  auto.mc(1) # Clicks West
  auto.scrolldown(26)
  auto.mm(725,530)
  auto.mc(1) # Heals Emissary
  time.sleep(4)
  auto.mm(503, 543)
  auto.mmc(1,9,2)

def startGB():
  login("matthewgcasey@gmail.com")
  time.sleep(5)
  auto.mm(848,452)
  auto.mm(848,562) 
  auto.mc(1) # Clicks Battle
  auto.downscroll(7)
  auto.mm(730,453)
  auto.mc(1)
  close()

def logout():
  auto.C("Home")
  auto.mm(860,160)
  auto.mc(1)

def close():
  logout()
  auto.mm(487,68)
  auto.mc(1)

def fest(): # delete the first chunk of lines for the old method festAfter()
  time.sleep(5)
  auto.scrolldown(3)
  auto.mm(848,276)
  auto.mm(842,459)
  auto.mc(1) # clicks into festival
  time.sleep(4)
  auto.mm(696,558)
  auto.mc(1) # clicks enter for festival
  time.sleep(4)
  auto.mc(1)  # joins something....
  auto.C("Home")  # process about to be reset
  auto.mm(224,450)
  auto.mc(1)
  time.sleep(5)
  auto.scrolldown(3)
  auto.mm(848,276) 
  auto.mm(842,459)
  auto.mc(1) # clicks into festival
  time.sleep(2)
  auto.mm(696,558)
  auto.mc(1) # clicks enter for festival
  time.sleep(4)
  auto.mc(1) # clicks enter for festival just incase.....
  time.sleep(2)
  auto.scrolldown(4)
  auto.mm(510,508)
  auto.mc(1) # your guilds
  time.sleep(2)
  auto.scrolldown(5)
  auto.mm(413, 463)
  auto.mc(1)
  auto.scrolldown(7)
  auto.mm(743,506)
  auto.mc(1) # first heal
  auto.mm(729,481)
  auto.mc(1) # first heal backup!!!
  time.sleep(4)
  auto.mm(516,544)
  auto.mmc(1,9,3)
  close()

def festFirst():
  time.sleep(5)
  auto.scrolldown(3)
  auto.mm(848,276) 
  auto.mm(842,459)
  auto.mc(1) # clicks into festival
  time.sleep(4)
  auto.mm(696,558)
  auto.mc(1) # clicks enter for festival
  time.sleep(4)
  auto.mc(1)  # joins something....
  time.sleep(4)
  auto.scrolldown(5)
  auto.mm(510,508)
  auto.mc(1) # your guilds
  time.sleep(4)
  auto.scrolldown(5)
  auto.mm(413, 463)
  auto.mc(1)
  auto.scrolldown(7)
  auto.mm(743,506)
  auto.mc(1) # first heal
  time.sleep(4)
  auto.mm(516,544)
  auto.mmc(1,9,3)
  close()
  
theboys = [0, 'matthewgcasey@gmail.com', 'Aphillistienio@gmail.com', 'Bphillistienio@gmail.com', 'phillistienio3@gmail.com', 'phillistienio4@gmail.com', '5phillistienio@gmail.com', '6phillistienio@gmail.com', '7phillistienio@gmail.com', 'guruphillistienio@gmail.com', 'mattsliferocks@gmail.com', 'phillistienioa@gmail.com', 'phillistienio2@gmail.com', 'wandphillistienio@gmail.com', 'exphillistienio@gmail.com', 'vizphillistienio@gmail.com', 'bombphillistienio@gmail.com']

def cycleGBF():
  startGB()
  print "hey"
  end = 1
  while end != 0:
    temp = theboys.pop()
    login(str(temp))
    guildbattleFirst()
    close()
    end = temp

def cycleGBA():
  print "hey"
  end = 1
  while end != 0:
    temp = theboys.pop()
    login(str(temp))
    guildbattleAfter()
    close()
    end = temp

def cycleFest():# this used to be After
  end = 1
  while end != 0:
    temp = theboys.pop(2)
    login(str(temp))
    fest()
    close()
    ent = temp

def cycleFestFirst():
  end = 1
  while end != 0:
    temp = theboys.pop()
    login(str(temp))
    festFirst()
    close()
    ent = temp

def GBcollect():
  end = 1
  while end != 0:
    temp = theboys.pop()
    login(str(temp))
    collect()
    close()
  
def collect():
  time.sleep(5)
  auto.mm(848,452)
  auto.mm(848,562) 
  auto.mc(1) # Clicks Battle
  time.sleep(4)
  auto.scrolldown(6)
  auto.mm(728,511)
  auto.mc(1) # Click Join Battle
  time.sleep(3)
  auto.mm(657,564)
  auto.mc(1) 
  time.sleep(2)
 
def addcode():
  counter = 0
  stop = False
  file = open('codes.txt', 'r')
  x = file.read()
  while stop == False:
    while counter != 10:
      auto.URL('firefox http://web3.castleagegame.com/castle_ws/army.php')
      time.sleep(8)
      auto.scrolldown(8)
      auto.mm(500,500)
      auto.mc(1)
      time.sleep(1)
      if line != " ":
        auto.k(line)
      elif line == " ":
        auto.C("Return")
        counter = counter + 1

def sshPhone():
  os.system("xte 'keydown Control_L' 'keydown Alt_L'")
  os.system("xte 'key t'")
  os.system("xte 'keyup Alt_L' 'keyup Control_L'")
  time.sleep(5)
  auto.k('xtightvncviewer 192.168.1.254 -passwd ~/.vnc/passwd' )
  auto.C('Return')
  time.sleep(5)
  print "vnc'd to phone"
 
def phoneHome():
  print "master phoneHome starts"
  auto.mm(523,346)
  time.sleep(2)
  auto.mc(1)
  time.sleep(9)
  auto.mm(379,243)
  auto.mc(1)
  time.sleep(3)
  auto.mm(513,380)
  auto.mc(1)
  time.sleep(5)
  print "should be ensuring home screen....."
  auto.mm(650,296)
  os.system("xte 'mousedown 1'")
  auto.mm(388,296)
  os.system("xte 'mouseup 1'")
  time.sleep(2)

def phoneClose():
  print "master phoneClose starts"
  time.sleep(9)
  auto.mm(379,243)
  auto.mc(1)
  time.sleep(3)
  auto.mm(513,380)
  auto.mc(1) 
  auto.mc(1)  # opensup close bar?
  print "task bar open"
  time.sleep(5)
  auto.mm(401,497)
  auto.md(1) # initiates kill app process
  time.sleep(3)
  auto.mu(1)
  auto.mm(367,476)
  time.sleep(1)
  auto.mc(1)  # click the red negative to kill app
  auto.mm(467,376)
  time.sleep(1)
  auto.mc(1)
  
def CAclick():
  print "clicking CA?!"
  auto.mm(553,139)
  time.sleep(1)
  auto.mc(1)  
  time.sleep(10)


  #auto.mm(512,407)
  #auto.mc(1)
  #time.sleep(9)
  #print "about to click text bar"
  #auto.mm(516,310)
  #auto.mc(1)
  #time.sleep(1)
  #auto.k(str(name))
  #time.sleep(1)
  #auto.mm(453,315)
  #auto.mc(1)
  #auto.k(str(passwd))
  #time.sleep(10)

def CAslidedown(times):
  counter = times
  while counter != 0
    time.sleep(2)
    auto.mm(504,472)
    auto.md(1)
    counter = counter - 1
 
def CAlogout():
  time.sleep(1)
  auto.mm(638,528)
  auto.mc(1)
  time.sleep(10)
  CAslidedown(3)
  auto.mm(488,339)
  auto.mc(1)
  time.sleep(3)

def CAhomer():
  time.sleep(1)
  auto.mm(388,529)
  auto.mc(1)
 
def festset(daytime):
  CAhomer()
  time.sleep(3)

  print "this is the fest set function"
  auto.mm(547,219) # moves to battle tab
  auto.mc(1)
  time.sleep(10)
  auto.mm(632, 319) # moves to time button
  auto.mc(1)
  time.sleep(10)
  auto.mm(594,321)
  auto.mmc(1,5,3)
  auto.mm(594,395)
  auto.mmc(1,int(daytime),4)
  auto.mm(582,510)
  auto.mc(1)
  time.sleep(20)
  auto.mm(634,195)
  auto.mc(1)
  time.sleep(20)
  os.system("xte 'keydown Alt_L' 'key F4'")
  time.sleep(5)
  os.system("xte 'keydown Alt_L' 'key F4'")

 
def coder():
  time.sleep(5)
  auto.mm(577,529) #clicks army
  print "clicks army"
  auto.mc(1)
  time.sleep(5)
  auto.mm(587,223) # clicks clicks army tab
  print "clocks army tab"
  auto.mc
  time.sleep(5)
  auto.mm(602,331) # clicks invite
  print "clicks the invite button"
  auto.mc(1)
  time.sleep(2)
  auto.mm(444,358) # clicks text box
  print "clocks or clicks text box"
  auto.mc(1)
  

def phoneFestSet(daytime):
  auto.mm(547,219) # moves to battle tab
  auto.mc(1)
  time.sleep(10)
  auto.mm(632, 319) # moves to time button
  auto.mc(1)
  auto.mm(594,321)
  auto.mmc(1,5,3)
