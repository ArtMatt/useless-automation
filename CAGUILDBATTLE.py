import auto
import time
import os

def login(name):
  auto.URL('firefox http://web3.castleagegame.com/castle_ws/connect_login.php')
  time.sleep(5)
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
  auto.mm(843,495)
  auto.mc(1)

def guildbattle():
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
  time.sleep(4) # DELETE
  auto.mc(1) # Joins Battle
  time.sleep(4) # DELETE
  auto.scrolldown(6)
  time.sleep(4) # DELETE
  auto.mm(515,477)
  time.sleep(4) # DELETE
  auto.mc(1) # Clicks Your Guild
  time.sleep(4) # DELETE
  auto.scrolldown(8)
  auto.mm(431,437)
  auto.mc(1) # Clicks West
  auto.scrolldown(9)
  auto.mm(725,530)
  auto.mc(1) # Heals Emissary
  time.sleep(4)
  auto.mm(503, 543)
  auto.mmc(1,10,2)
 
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
  auto.scrollup(10)
  auto.mm(860,160)
  auto.mc(1)

def close():
  logout()
  auto.mm(487,68)
  auto.mc(1)

def fest():
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

def cycleGB():
  startGB()
  end = False
  while end != 0
    temp = theboys.pop()
    #login(str(temp))
    #guildbattle()
    #close()
    print temp
    time.sleep(1)
    end = temp

def cycleF():
  temp = theboys.pop()
  login(str(temp))
  fest()
