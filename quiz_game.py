import random
import platform
nplayers=0
nowplaying=0
rcolor=0

def choose_players():
    nplayers=int(input("Input the number of players(1-4): "))
    for x in range (1,(nplayers+1)):
            playernm=str(input("Input player name: "))
            globals()['player'+str(x)] = playernm
            globals()['score'+str(x)] = 0

def choose_color():
    global color
    color = random.randint(1,4)

def sysinfo():
     py_ver=(platform.python_version())
     systype=(platform.system())
     print("Python version:", py_ver)
     print("System type:", systype)
     print()
sysinfo()
input("Press Enter to start game...")

choose_players()
choose_color()
print(nplayers, player1, player2, player3, player4) #For debugging
#print(globals()) #For debugging