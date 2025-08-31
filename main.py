import math
import random
import time
import os
#Number of players int NumPlayers
#   ask player how many players to supply NumPlayers
#   Based on num players generate the number of deck of cards
#int[] for deck of cards
#Tracker for current round int CurrentRound
#
#
#  1. The players
#     a. Every player has a name
#     b. Every player has Totalfunds
#     c. Every player has an assigned seat
#     d. Every player has a point tracker
#     e. Every player has a currentToleranceNumber
#        -Can be determined if they choose to roll or not
#     f. Players have the ability to roll the dice during rolling phase
#     h. Players have the ability to check, call, raise or fold during betting phase
#     i. Every player has an age to determine who is the eldest
#  2. The Game
#     a. Every game has rounds
#     b. Every game has a designated Starter
#     c. Every game has two dice to access
#     d. Every game has a deck of cards TBD by number of players
#     e. Every game has a game ID (GID)
#     f. Every game has a current pot tracker
#     g. Every round has:
#        I. shuffle cards phase
#       II. Dealing 2 cards to each player phase
#      III. Blind Bet phase
#       IV. Player Card Reveal Phase
#        V. Betting phase
#       VI. Rolling phase
#  3. Deck of Cards
#       A list that is determined by number of players
#  4. The Dice
def peakCards(listOfPlayers):
    #clearTerminal()#clear the screen
    print("Each player is now allowed to look at thier own cards")
    #clearTerminal()
    for player in listOfPlayers: #iterate through the list of players
        print("Player "+player.Name+" press Enter when ready to look at your cards")

def initPot(listOfPlayers,smallBlind,bigBlind):
    thePot=0
    for player in listOfPlayers:
        #print("Player "+player.Name+" status: CurrentSmall: "+str(player.CurrentSmall)+" CurrentBig: "+str(player.CurrentBig))
        if(player.CurrentSmall == True):
            print("Player "+player.Name+" is the small blind")
            player.CurrentFunds -= smallBlind
            print("Player "+player.Name+" deducted $"+str(smallBlind)+" from their current funds")
            thePot += smallBlind
        elif(player.CurrentBig == True):
            print("Player "+player.Name+" is the big blind")
            player.CurrentFunds -= bigBlind
            print("Player "+player.Name+" deducted $"+str(bigBlind)+" from their current funds")
            thePot += bigBlind
        else:
            pass
    print("Initialized pot is $"+str(thePot))
    return thePot

#Might have to create a updateBlindBet function when players decrease down to two and increase back up past two players
def setBlindBets(listOfPlayers):
    bigBlind =-1
    smallBlind =-1
    if(len(listOfPlayers) ==2):
        print("Only 2 players found, setting only one blind. Press Enter to continue")
        input()
        print("Enter a value to set blind")
        userInput = input()
        try:#casting user input to a float as input is taken as a string by defualt
            smallBlind = float(userInput)
        except ValueError:
            print("Invalid input, please enter a number")
            setBlindBets(listOfPlayers)
        for player in listOfPlayers:
            if(player.CurrentFunds - smallBlind <= 0.0):
                print("Not all players can afford blindbet, please pick a smaller blind")
                setBlindBets(listOfPlayers)
    else:
        print("More than 2 players found. Setting up big and small blinds. Press Enter to continue")
        input()
        print("Enter a vlue to set small blind")
        userInput = input()
        try:
            smallBlind = float(userInput)
        except ValueError:
            print("Invalid input, please enter a number")
            setBlindBets(listOfPlayers)
        for player in listOfPlayers:
            if(player.CurrentFunds - smallBlind <=0.0):
                print("Not all players can afford the small blind, please pick a smaller blind")
                setBlindBets(listOfPlayers)
        print("Enter a value to set big blind")
        userInput= input()
        try:
            bigBlind = float(userInput)
        except ValueError:
            print("Invalid input, please enter a number")
            setBlindBets(listOfPlayers)
        for player in listOfPlayers:
            if(player.CurrentFunds - bigBlind <=0.0):
                print("Not all players can afford the big blind, please pick a smaller blind")
                setBlindBets(listOfPlayers)
    return smallBlind, bigBlind

def initBettingPhase(listOfPlayers,theStarter,smallBlind,bigBlind,currentPot):
    #find the starters index in the list of players
    starterIndex = -1
    currIndex = 0
    #currentPot= 0.0
    #This does not account for list of players with the same name
    for player in listOfPlayers:
        if(player.Name == theStarter.Name):
            starterIndex = currIndex
            break
        else:
            currIndex +=1
    if starterIndex != -1:
        if len(listOfPlayers) == 2:
            for playerIndex in range(0,len(listOfPlayers)):
                currentIndex = (starterIndex + playerIndex) % len(listOfPlayers)
                activePlayer = listOfPlayers[currentIndex]
                if(activePlayer.CurrentStarter == True and activePlayer.CurrentSmall == True):
                    print("Player "+activePlayer.Name+" is the current Starter")
                    print("player "+activePlayer.Name+" press any key to initialize blind bet")
                    input()
                    print("Player "+activePlayer.Name+" deducted $"+str(smallBlind)+" from current funds")
                    activePlayer.CurrentFunds -= smallBlind
                    currentPot += smallBlind
                    print("Current Pot is "+str(currentPot))
                else:
                    pass
        else:
           #more than 2 players puts both blinds in play
            for playerIndex in range(0, len(listOfPlayers)): 
                currentIndex=(starterIndex + playerIndex) % len(listOfPlayers)
                activePlayer = listOfPlayers[currentIndex]
                if(activePlayer.CurrentStarter == True and activePlayer.CurrentSmall ==True):
                    print("Player "+activePlayer.Name+" is the current Starter")
                    print("Player "+activePlayer.Name+" press any key to initialize blind bet")
                    input()
                    print("Player"+activePlayer.Name+" is the current Small Blind")
                    print("Player "+activePlayer.Name+" deducted $"+str(smallBlind)+" from current funds")
                    activePlayer.CurrentFunds -= smallBlind
                    currentPot += smallBlind
                    print("Current Pot is $"+str(currentPot))
                elif(activePlayer.CurrentBig == True):
                    print("Player "+activePlayer.Name+" is the current Big Blind")
                    print("Player "+activePlayer.Name+" deducted $"+str(bigBlind)+" from current funds")
                    activePlayer.CurrentFunds -=bigBlind
                    currentPot += bigBlind
                    print("Current Pot is $"+str(currentPot))
                else:
                    pass
                    #print("Player "+activePlayer.Name+" press enter to start betting phase")
                    #input()
    else:
        print("Error, unable to find matching name between list of players and set Starter Player name")  

def updateThePlayers(listOfPlayers,dealer,starter,bigBlind):
    if bigBlind == None:
        for player in listOfPlayers:
            if(player.Name == dealer.Name or player.Name == starter.Name):
                if player.Name == dealer.Name:
                    player.CurrentDealer=True
                else:
                    player.CurrentStarter=True
                    player.CurrentSmall=True
            else:
                pass
    else:
        for player in listOfPlayers:
            if(player.Name == bigBlind.Name or player.Name == dealer.Name or player.Name == starter.Name):
                if player.Name == dealer.Name:
                    player.CurrentDealer = True
                elif player.Name == starter.Name:
                    player.CurrentStarter = True
                    player.CurrentSmall = True
                else:
                    player.CurrentBig = True
            else:
                pass
    return listOfPlayers

def dealerShuffleDealCards(theCards,theDealer,thePlayers,startingIndex):
    print(theDealer.Name+" is the current rounds Dealer. Press any button to shuffle deck")
    input()
    print(theDealer.Name+" is shuffling cards.")
    theCards = shuffleDeck(theCards)
    cardsPostDeal,thePlayers=dealCards(theCards,thePlayers,startingIndex)
    return cardsPostDeal, thePlayers

def findCurrentBigBlind(currentDealerIndex, listOfPlayers):
    bigBlindIndex = (currentDealerIndex +2) % len(listOfPlayers)
    bigBlindPlayer = listOfPlayers[bigBlindIndex]
    for player in listOfPlayers:
        if player.Name == bigBlindPlayer.Name:
            player.CurrentBig = True
            break
        else:
            pass
    return bigBlindIndex, bigBlindPlayer, listOfPlayers

def findCurrentDealerStarter(currentRound,thePlayers,theDealerIndex):
    theBigBlind = None
    if currentRound == 1:
        theDealer = thePlayers[len(thePlayers)-1]
        theStarter = thePlayers[0]
        theDealerIndex = len(thePlayers)-1
        if len(thePlayers) >2:
            theBigBlindIndex,theBigBlind,thePlayers =findCurrentBigBlind(theDealerIndex, thePlayers)
    else:
        #update logic for updating dealer and starter might need additional parameter for recursive logic
        theDealer = thePlayers[theDealerIndex]
        #setting starter tracker for round
        if theDealerIndex +1 >= len(thePlayers):
            theStarter = thePlayers[0]
        else:
            theStarter = thePlayers[theDealerIndex +1]
        if len(thePlayers) >2:
            theBigBlindIndex,theBigBlind,thePlayers =findCurrentBigBlind(theDealerIndex, thePlayers)
    theDealer.CurrentDealer=True
    theStarter.CurrentStarter=True
    theStarter.CurrentSmall=True
    #function to actually update the list of players being passed around each round's phase functions
    thePlayers=updateThePlayers(thePlayers,theDealer,theStarter,theBigBlind)
    #test the updated player list
    #for player in thePlayers:
    #    print(player.Name+" current status: "+"Dealer: "+str(player.CurrentDealer)+"Starter: "+str(player.CurrentStarter))
    return theDealer,theStarter,theDealerIndex,thePlayers

def printCard(theCard):
    suites = ["clubs", "diamonds", "hearts", "Spades"]
    values = [ "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen", "King", "Ace" ]
    suit = suites[theCard//13]
    value = values[theCard%13]
    print(f"{value} of {suit}")

def dealCards(theCards, thePlayers, CurrentIndex):
    ActiveDeck = theCards
    cardIndex=0
    #for loop that iterates through the shuffled deck starting at the beggining and copies the shuffled deck to a temp deck that removes the "dealt" cards and returns the deck to be played and populates each players class card one and two to populate
    for playerIndex in range(0,len(thePlayers)):
        currentIndex = (CurrentIndex + playerIndex) % len(thePlayers)
        activePlayer = thePlayers[currentIndex]
        activePlayer.CurrentCardOne = ActiveDeck[cardIndex]
        ActiveDeck.pop(cardIndex)
        activePlayer.CurrentCardTwo = ActiveDeck[cardIndex]
        ActiveDeck.pop(cardIndex)
    return ActiveDeck, thePlayers

def startRound(roundNumber,seatedPlayers,cards,dice,currentDealerIndex, bigBlind, smallBlind):
    print(f"Welcome to round "+str(roundNumber))
    currentPot=0
    #set the currentDealerIndex, first round hard codes the startRound call length of player list -1 to pass last index of list
    #Finds current dealer to shuffle deck and deal two cards face down to each player, finds current starter
    #We should check if seatedPlayers length is below 2 meaning all players left, should not be possible on first round but will be possible if turning this function recursive
    if(roundNumber != 1):
        currentDealer,currentStarter,startingIndex,seatedPlayers=findCurrentDealerStarter(roundNumber,seatedPlayers,currentDealerIndex)
    else:
        currentDealer,currentStarter,startingIndex,seatedPlayers=findCurrentDealerStarter(roundNumber,seatedPlayers,-1)
    cardsPostDeal,seatedPlayers=dealerShuffleDealCards(cards,currentDealer,seatedPlayers,startingIndex)
    #Init the pot with blind bets
    currentPot=initPot(seatedPlayers,bigBlind,smallBlind)
    #Let Players look at thier cards
    peakCards(seatedPlayers)
    #Start Betting Phase
    currentPot=initBettingPhase(seatedPlayers,currentStarter,bigBlind,smallBlind,currentPot)
    #print("Current Starter is "+currentStarter.Name)
    #for playerIndex in range(0,len(seatedPlayers)):
    #    currentIndex = (startingIndex + playerIndex) % len(seatedPlayers) 
    #    activePlayer = seatedPlayers[currentIndex]
    #    print("Is player "+activePlayer.Name+" ready? Press any button to continue")
    #    input()

    #Increment Round after the end of all phases in a round
    roundNumber+=1

#TODOS:
#***create a function that resets all players currentDealer boolean after each round
#***create a function that updates the currentDealerIndex
def shuffleDeck(cards):
    current_time = time.time()
    random.seed(current_time)
    random.shuffle(cards)
    #printDeck(cards, len(cards))
    return cards
#This does not take into account for ties
def findEldest(players):
    players.sort(key=lambda Player: Player.Age)
    eldest_Player = players[-1]
    eldest_Player.IsEldest = True
    print("Eldest player is "+eldest_Player.Name)
    return players

def playGame(ListofCards,ListofPlayers,Dice):
    roundNumber =1
    ListofPlayers =findEldest(ListofPlayers)
    ListofCards =shuffleDeck(ListofCards)
    bigBlind, smallBlind =setBlindBets(ListofPlayers)
    startRound(roundNumber,ListofPlayers,ListofCards,Dice,len(ListofPlayers)-1,bigBlind,smallBlind)
    
class Dice:
    def __init__(self):
        self.diceOne = [1,2,3,4,5,6,7,8,9,10]

class Player:
    def __init__(self,Name,Age,Funds):
        self.Name = Name
        self.Age = Age
        self.CurrentTolerance = -1
        self.CurrentPoints = 0
        self.CurrentFunds = float(Funds)
        self.IsEldest = False
        self.CurrentDealer = False
        self.CurrentStarter = False
        self.CurrentCardOne = -1
        self.CurrentCardTwo = -1
        self.CurrentSmall = False
        self.CurrentBig = False
    
    def RollPhase():
        pass
    def BettingPhase():
        pass

def printDeck(deckOfCards, numberOfCards):
     suites = ["Clubs", "Diamonds", "Hearts", "Spades"]
     values = [ "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "Jack", "Queen", "King", "Ace" ]
     for cards in deckOfCards:
        if cards < 52:
            value = values[cards %13]
            suit = suites[cards//13]
            if 0 <= len(suites):
                print(f"{value} of {suit}")
            else:
                print(f"IndexError for card {cards}: suit index {suit}")

def rollDice(dice):
    current_time = time.time()
    random.seed(current_time)
    pickedSideOne = random.choice(dice.diceOne)
    print(f"Rolled dice one:{pickedSideOne}")

def initDice():
    theDice = Dice()
    return theDice

def initPlayers(playerCount):
    #We might need to add a check here for duplicate names and force different names ie: Dre1 and Dre2
    players = []
    for number in range(playerCount):
        print("Enter name")
        temp_name = input()
        print("Enter age")
        temp_age = input()
        print("Enter funds")
        temp_funds = input()
        person= Player(temp_name, temp_age,temp_funds)
        players.append(person)
    return players

def initDecks():
    print("please enter how many players, max players is 10") #cap 2 decks for meow
    userinput = input()
    try:#try catch to cast user input string to int
        numOfPlayers = int(userinput)
    except ValueError:
        print("Invalid input, please enter a number")
        initDecks()
    if numOfPlayers > 10 or numOfPlayers <= 1: #check if user put in valid numbers if cast was successful
        print("Invalid input, please enter a valid number between 2 and 10")
        initDecks()
    print("number of players is "+str(numOfPlayers))
    decksNeeded = math.ceil(numOfPlayers/5)#we use the ceiling function to round up to the decks needed
    print("Number of decks is "+str(decksNeeded))
    cardsNeeded = decksNeeded * 52
    print("Number of cards is "+str(cardsNeeded))
    totalCardsList = [i % 52 for i in range(cardsNeeded)] # creates the list but in loop 0-51 based on how many decks are in use to represent 52 cards per deck
    printDeck(totalCardsList, cardsNeeded)
    return totalCardsList, numOfPlayers

def startGame():
    theCards, numberOfPlayers = initDecks()
    thePlayers = initPlayers(numberOfPlayers)
    theDice = initDice()
    playGame(theCards, thePlayers, theDice)

def printRules():
    print("Welcome to the game of tolerance")
    print()
    print("The eldest player is the first round Dealer. The Dealer position, from then on, rotates clockwise after each round. The player that is next in rotation to be Dealer, shall be the called the Starter. If using multiple decks of cards, they should be combined")
    print()
    print("A blind bet amount shall be per-determined by those playing. When betting, players may Check, Call, Raise, or Fold just as in the classic game of Texas Hold’em Poker.")
    print()
    print("Each round is won by the player that ends the round with the most points. If there is a point during a round where every player except one folds, the last player standing is declared the Winner.")
    print()
    print("Cards numbered two through ten are worth an equal number of points to their number. Face cards are worth the following number of points; a Jack is worth eleven points, a Queen is worth twelve points, a King is worth thirteen points, and lastly, an Ace is worth one point. Joker cards shall not be used.")
    print()
    print("1. The cards are shuffled by the Dealer.")
    print("2. Two cards are dealt face down to each player in a clockwise order. Do not view the cards.")
    print("3. A blind bet of the per-determined amount shall be made by the Starter.")
    print("4. Each player may now view their cards privately.")
    print("5. Beginning with the Starter, complete the first round of betting.")
    print("6. Beginning with the Starter, complete the first round of rolls. ")
    print()
    print("During a round of rolls, each player must first decide if they wish to roll or not. Choosing not to role the die, also known as 'choosing to pass', will not effect the player’s point count. If the player chooses to roll the die, they have the potential to gain or lose points.")
    print()
    print("The first step to rolling is the player deciding their Tolerance number, which is a possible number to be rolled with the die. In a game that is using a ten sided die, the player may choose a number one through ten as their Tolerance number. The Tolerance number is equal to the number of points the rolling player will receive if they roll a number greater than or equal to said Tolerance number. If the player roles below said Tolerance number, they will lose the number of points equal to said Tolerance number. ")
    print()
    print("For example, a player may choose to roll and choose five as their Tolerance number. If the player rolls a six. The player would then add five points to their hand’s total. If the player instead rolled a three, they would subtract five points from their hand’s total. Lastly, if the player chose ten as their Tolerance and then rolled a ten, they would add ten points to their hand’s total. ")
    print()
    print("7. Beginning with the Starter, complete the second round of betting.")
    print("8. Beginning with the Starter, complete the second round of rolls.")
    print("9. Beginning with the Starter, complete the third and final round of betting.")
    print("10. Every player that has not yet folded must now show their hand publicly.")
    print("11. The Dealer should tally up each player’s points and declare the round’s Winner.")
    print("12. The Winner receives the total amount of money previously bet by the players of the round")
    print()
    print("Repeat the game loop until the game is over. The game can be played similarly to Texas Hold ‘Em Poker styles of play. For example, a Tournament style is where player’s enter the game with equal sums of money and play until only one player has money, automatically declaring them the Winner. Tolerance could also be played as a No-Limit Cash Game where players can join or leave the game between rounds as they please with any amount of money they wish to play with. There are many other styles of play that work with Tolerance.")

def main():  
    print ("Press 1 to enter how many players, Press 2 to read rules, Press 3 to Quit")
    x = input()
    if x =="1":
        print ("User choose 1")
        startGame()#WE WILL UPDATE THIS TO A FUNCTION THAT RUNS THE GAME
    elif x =="2":
        printRules()
        main()
    elif x =="3":
        print ("Have a nice day!!!")
    else:
        print ("Please choose 1 or 2 or 3")
        main()
main()