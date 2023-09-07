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

sci_q=['What does DNA stand for?', 'How many bones are in the human body?', 'At what temperature are Celsius and Fahrenheit equal?', 'What is the only even prime number?', 'What does USB stand for?', 'Sound travels faster in air than in water: true or false?', 'Where in the human body can the smallest bone be found?', 'How many brains does an octopus have?']
sci_a=['deoxyribonucleic acid', '206', '-40', '2', 'universal serial bus', 'false', 'ear', '9']

sysinfo()
input("Press Enter to start game...")

choose_players()
choose_color()
for x in range (0,7): #For debugging
     print(sci_q[x], sci_a[x]) #For debugging
print(nplayers, player1, player2, player3, player4) #For debugging
#print(globals()) #For debugging