def createDeck():
    class Card:
        def __init__(self, int, suit):
            if int == 1:
                self.int = "A"
            elif int == 11:
                self.int = "J"
            elif int == 12:
                self.int = "Q"
            elif int == 13:
                self.int = "K"
            else:
                self.int = int

            if suit == 0:
                self.suit = "clubs"
            elif suit == 1:
                self.suit = "hearts"
            elif suit == 2:
                self.suit = "spades"
            elif suit == 3:
                self.suit = "diamonds"

    deck = []
    for i in range(1,14):
        for j in range(0,4):
            deck.append(Card(i,j))
    
    return deck

def rules():
    print ("insert rules:")

def askInput(str):
    inp = input(str)
    if inp == "help":
        rules()
        askInput()
    else:
        return inp

def newPlayer():
    class Player:
        def __init__ (name, money):
            self.name = name
            self.money = money
    name = askInput("name: ")
    return Player(name, 120)

# def newRound(players):
#         for player of players:
#             print(player.name, player.money)
#         def askBet(players):
#             bet = askInput("Decide on a bet (>10$): ")
#             if
        



def startGame():
    players = []
    rules()
    deck = createDeck()
    players.append(newPlayer())
    askPlayer = askInput("Add a player? (Y/n)")
    if askPlayer.lower() == "y":
        players.append(newPlayer())


    

    
