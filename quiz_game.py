# Work in progress for **/**/****, aka unkown time
# Contributions are welcome. 
import random
import platform
nplayers=0
nowplaying=0

def choose_players():
     try:
         nplayers=int(input("Input the number of players(1-4): "))
     except:
         nplayers=1
     for x in range (1,(nplayers+1)):
            playernm=''
            while playernm=='':  
               playernm=str(input("Input player name: "))
            globals()['player'+str(x)] = playernm
            globals()['score'+str(x)] = 0

def random_color():
    global color
    color_num = random.randint(0,1) #Change "1" to "3" upon completion of program
    ColorToQtype=["sci_q", "his_q"]
    color=ColorToQtype[color_num]
    print(color)


def random_qno(qlistlen):
    global q_no
    q_no=random.randint(0,(qlistlen-1))
    print(q_no)

def scoring_system():
     global nowplaying
     global score1
     score=0
     tryno=1
     print("Now playing:", str(player1), "(" + str(nowplaying) + ")")
     if color=="sci_q":
        question=sci_q[q_no]
        answer=sci_a[q_no]
     elif color=="his_q":
        question=his_q[q_no]
        answer=his_a[q_no]
     while tryno<=2:
          usranswer=str(input(question))
          usranswer=usranswer.lower()
          if usranswer == answer:
               score1+=2
               print("Your answer is correct!")
               tryno=3
          else:
               print("Try again.")
               tryno=tryno+1
     print("Your score is:", score1)

def sysinfo():
     py_ver=(platform.python_version())
     systype=(platform.system())
     print("Python version:", py_ver)
     print("System type:", systype)
     print()

sci_q=['What does DNA stand for?', 'How many bones are in the human body?', 'At what temperature are Celsius and Fahrenheit equal?', 'What is the only even prime number?', 'What does USB stand for?', 'Sound travels faster in air than in water: true or false?', 'Where in the human body can the smallest bone be found?']
sci_a=['deoxyribonucleic acid', '206', '-40', '2', 'universal serial bus', 'false', 'ear']
his_q=['Which country did Germany invade to kickstart World War II?', 'What language was spoken in Ancient Rome?', 'In Ancient Rome, what was a thermae?', 'Who is known as the "Father of Medicine"?', 'The First Opium War was fought between Great Britain and which other country?', 'Who is credited with inventing the telephone?', 'What was the name of the Nazi official secret police?']
his_a=['poland', 'latin', 'public baths', 'hippocrates', 'china', 'alexander graham bell', 'gestapo']

sysinfo()
input("Press Enter to start game...")

choose_players()
random_color()
random_qno(len(sci_q)) #Recheck
scoring_system()
for x in range (0,7): #For debugging
     print(sci_q[x], sci_a[x]) #For debugging
     print(his_q[x], his_a[x]) #For debugging
#print(nplayers, player1, player2, player3, player4) #For debugging
#print(globals()) #For debugging