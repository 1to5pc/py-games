import random
nplayers=0
score1=0
score2=0
score3=0
score4=0
player1=""
player2=""
player3=""
player4=""
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
    if nplayers==1:
        player1=input("Enter name of player 1: ")
    elif nplayers==2:
        player1=input("Enter name of player 1: ")
        player2=input("Enter name of player 2: ")
    elif nplayers==3:
        player1=input("Enter name of player 1: ")
        player2=input("Enter name of player 2: ")
        player3=input("Enter name of player 3: ")
    else:
        player1=input("Enter name of player 1: ")
        player2=input("Enter name of player 2: ")
        player3=input("Enter name of player 3: ")
        player4=input("Enter name of player 4: ")
        return
def choose_color():
    global colqor
    colqor = random.randint(1,4)

choose_players()
choose_color()
print(nplayers, player1, player2, player3, player4, colqor)
