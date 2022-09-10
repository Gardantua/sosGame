
import random
import string

print("--------------------------SOS------------------------------")
a1="1"
a2="2"
a3="3"
b1="4"
b2="5"
b3="6"
c1="7"
c2="8"
c3="9"

playerName = "Siz "

winAlgCounter = 0

availableMoves = ["1","2","3","4","5","6","7","8","9"]

computertLetter = "o"
choosex_o = "x"

game = 0

lastPlayer = None
gamePlaceToPlay = None

def PrintBoard():
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    pp = f"""
          |     |     
       {a1}  |  {a2}  |  {a3}  
     _____|_____|_____
          |     |     
       {b1}  |  {b2}  |  {b3} 
     _____|_____|_____
          |     |     
       {c1}  |  {c2}  |  {c3}  
          |     |     

    """
    print(pp)
    winAlg()

def winAlg():
    global game
    global winAlgCounter
    if a1==a2==a3 or b1==b2==b3 or c1==c2==c3 or a1==b2==c3 or a3==b2==c1 or a1==b1==c1 or a2==b2==c2 or a3==b3==c3:
        game = 1
        if winAlgCounter==0:
            print(f"Oyunu kazanan: {lastPlayer}")
            winAlgCounter=1
        
    a=len(availableMoves)
    if a==0 and winAlgCounter==0:
        game = 1
        print("Berabere")


def spot():
    global game
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    
    placeToPlay = 1
    placeToPlay = input("Yer seçiniz")
    if placeToPlay not in availableMoves:
        print("Seçtiğiniz yer oynanabilir durumda değil.")
        spot()

    global gamePlaceToPlay 
    if placeToPlay == "1":
        a1 = choosex_o
    elif placeToPlay == "2":
        a2 = choosex_o
    elif placeToPlay == "3":
        a3 = choosex_o
    elif placeToPlay == "4":
        b1 = choosex_o
    elif placeToPlay == "5":
        b2 = choosex_o
    elif placeToPlay == "6":
        b3 = choosex_o
    elif placeToPlay == "7":
        c1 = choosex_o
    elif placeToPlay == "8":
        c2 = choosex_o
    elif placeToPlay == "9":
        c3 = choosex_o
    if placeToPlay in availableMoves:
        availableMoves.remove(placeToPlay)

    
def ComputerPlayer():
    global game
    global a1
    global a2
    global a3
    global b1
    global b2
    global b3
    global c1
    global c2
    global c3
    global gamePlaceToPlay 
    global lastPlayer
    placeToPlay ="0"
    if len(availableMoves) >0:
        gamePlaceToPlay = random.choice(availableMoves)
    if gamePlaceToPlay == "1":
        a1 = computertLetter = "o"

    elif gamePlaceToPlay == "2":
        a2 = computertLetter = "o"

    elif gamePlaceToPlay == "3":
        a3 = computertLetter = "o"

    elif gamePlaceToPlay == "4":
        b1 = computertLetter = "o"

    elif gamePlaceToPlay == "5":
        b2 = choosex_o
    elif gamePlaceToPlay == "6":
        b3 = computertLetter = "o"

    elif gamePlaceToPlay == "7":
        c1 = computertLetter = "o"

    elif gamePlaceToPlay == "8":
        c2 = computertLetter = "o"

    elif gamePlaceToPlay == "9":
        c3 = computertLetter = "o"
    if winAlgCounter==0:
        lastPlayer="Bilgisayar"
    if len(availableMoves) >0:
        availableMoves.remove(gamePlaceToPlay)

def humanPlayer():
    global availableMoves
    global gamePlaceToPlay 
    PrintBoard()
    spot()
    lastPlayer="Siz"

choosePlayer = input("""
1 - player vs player
2 - player vs computer
(1/2)
""")


lastPlayer = playerName

while choosePlayer == '2' and game == 0:
    
    if choosex_o == "x":
        lastPlayer = "Siz"
        humanPlayer()
        winAlg()
        ComputerPlayer()
        winAlg()
    elif choosex_o == "o":
        ComputerPlayer()
        winAlg()
        humanPlayer()
        winAlg()

if choosePlayer == '1' and game == 0:

    firstPlayer = input("x oyna başlar. İlk oyuncu ismi : ")
    secondPlayer = input("İkinci oyuncu ismi : ")

while (choosePlayer == '1') and (game == 0):

    if (choosePlayer == '1') and (game == 0):
        winAlg()
        humanPlayer()
        lastPlayer = firstPlayer
        choosex_o = "o"
        winAlg()
    if (choosePlayer == '1') and (game == 0):

        humanPlayer()
        lastPlayer = secondPlayer
        winAlg()
        choosex_o = "x"
PrintBoard()