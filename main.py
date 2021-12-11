import random
import os

### global variables
minBet = 10
startingMoney = 200
###

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def pause():
  input("Press enter to continue...")

rules = "insert rules"

roundOver = False
gameOver = False

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

def menu():
  print ("-h for the rules\n")
  if bet != '':
    print ("/n  current bet: {}".format(bet))
  if players != []:
    for data in players:
      if roundOver:
        print (" -{} {}$ {}/21".format(data.name, data.money, data.int))
      else:
        print (" -{} {}$".format(data.name, data.money))
  


def askInput(str, msg="", displayRules=False):
    clearConsole()
    if displayRules: 
      print (rules)
      input ("\n\nPress enter to leave")
      clearConsole()
    
    menu()

    print ("\n")
    if msg != '':
      print (msg)

    inp = input(str)
    if inp.lower() == "--help" or inp.lower() == "-h":
        askInput(str, "", True)
    else:
        return inp

def newPlayer():
    class Player:
        def __init__ (self, name, money):
            self.name = name
            self.money = money
            self.alive = True
            self.win = False
            self.int = 0
    name = askInput("name: ")
    players.append(Player(name, startingMoney))
    restart = askInput("Add a player? (y/n): ")
    #restart = restart.lower() ?Doesn't work for some reason?
    if restart == "y":
      newPlayer()

def newRound():
        global roundOver
        global gameOver
        roundOver = False
  
        deck = createDeck()

        def askBet(error=''):
            bet = int(askInput("Decide on a bet (>{}$): ".format(minBet),error))
            if (bet < minBet):
                error = "bet too small"
                askBet(error)
            for data in players:
                if data.alive:
                  if data.money < bet:
                    error = "{} doesn't have enough money".format(data.name)
                    askBet(error)
            else:
              return bet
            
        bet = askBet()

        for player in players:
          player.money -= bet
          player.int = 0
        
        for player in players:
          def subRound(player):
            card = random.choice(deck)
            if isinstance(card.int, int):
              player.int += card.int
            else:
              player.int += 10

            if player.int > 21:
              print ("busted :(")
              pause()
            elif player.int == 21:
              print ("blackjack!")
              pause()
            elif askInput("Stand or hit? (s/h): ", "{}'s turn with a score of {}".format(player.name, player.int)) == 'h':
              subRound(player)

          subRound(player)
        
        roundOver = True
        alive = 0
        max = 0
        winnerCount = 0
        for data in players:
          if data.int <= 21 and data.int > max:
            max = data.int
        
        if max != 0:
          for data in players:
            if data.int == max:
              winnerCount += 1
              data.win = True
            else:
              data.win = False
          
          winAmnt = bet * len(players) / winnerCount

          for data in players:
            if data.win:
              data.money += winAmnt 

        for player in players:
            if player.money <= 0:
              player.alive = False
            else:
              alive += 1
              print(player.name, player.money)
        if alive <= 1:
          gameOver = True
          endGame()
          if askInput("Play again? (y/n): ", "foo won!!") == "y":
            startGame

        else:
          askInput("Press enter to continue to next round...","foo won the round")
          newRound()
          

    
        

def endGame():
  print("foo won!!")   
                    



def startGame():
    global players
    global bet
    global deck
    bet = ''
    players = []
    newPlayer()
    newRound()

startGame()

