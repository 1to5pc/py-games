def choose_colour():
    global colour
    global subject
    import random
    randomNumber=random.randint(1,4)
    if randomNumber==1:
        colour="Red"
        subject="History"
    elif randomNumber==2:
        colour="Blue"
        subject="Science"
    elif randomNumber==3:
        colour="Green"
        subject="Political"
    else:
        colour="Yellow"
        subject="Geography"
choose_colour()
def choose_question(colour):
    if colour=="Red":
        question="When was ---- built?"
    elif colour=="Blue":
        question="How many chambers does the human heart have?"
    elif colour=="Green":
        question="How long did ----- stay in presidency?"
    elif colour=="Yellow":
        question="In which continent is ------ situated?"
    else:
        question="Invalid colour"
    return question
exitgame=""
while exitgame!="exit":
    exitgame=input("Press enter to spin the wheel or type 'exit' to exit the game   : ")
    if exitgame!="exit":
        choose_colour()
        question=choose_question(colour)
        print("The colour chosen is:", colour)
        print("Your question is:", question)