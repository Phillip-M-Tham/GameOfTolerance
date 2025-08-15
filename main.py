import math
#Number of players int NumPlayers
#   ask player how many players to supply NumPlayers
#   Based on num players generate the number of deck of cards
#int[] for deck of cards
#Tracker for current round int CurrentRound
#
# Class objects for
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
#  4. The Dice
#class Deck:
#    deckOfCards =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48.49,50,51]

def initdecks():
    print("please enter how many players, max players is 10") #cap 2 decks for meow
    userinput = input()
    try:#try catch to cast user input string to int
        numOfPlayers = int(userinput)
    except ValueError:
        print("Invalid input, please enter a number")
        initdecks()
    if numOfPlayers > 10 or numOfPlayers <= 1: #check if user put in valid numbers if cast was successful
        print("Invalid input, please enter a valid number between 2 and 10")
        initdecks()
    print("number of players is "+str(numOfPlayers))
    decksNeeded = math.ceil(numOfPlayers/5)#we use the ceiling function to round up to the decks needed
    print("Number of decks is "+str(decksNeeded))

def startGame():
    initdecks()
    #playrounds()

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