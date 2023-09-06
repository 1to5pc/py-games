import random
nplayers=0
score1=0
score2=0
score3=0
score4=0
nowplaying=0
colqor=0

def choose_players():
    global nplayers
    global score1
    global score2
    global score3
    global score4
    global player1
    global player2
    global player3
    global player4
    nplayers=int(input("Input the number of players(1-4): "))
    for x in range (1,(nplayers+1)):
            playernm=str(input("Input player name: "))
            globals()['player'+str(x)] = playernm
def choose_color():
    global colqor
    colqor = random.randint(1,4)

choose_players()
choose_color()
print(nplayers, player1, player2, player3, player4)
