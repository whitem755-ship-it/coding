import random
"My rock, paper, scissors game should be able to be multiplayer"
"My rock, paper, scissors game should be able to us powers "
"My rock, paper, scissors game should be able to Play against CPU "

def rpsGame():
    rpsOptions = [rock, paper, scissor]
    print('welcome to RPS: the Game')
    print( '********************************')
    print('1. Start Game')
    print('2. Game Rules')
    print('3. Quit')
    selection = input()
    if int(selection) == 1:
        print('the game is starting...')
        print("please select a game mode: ")
        print('1. vs. human')
        print('2. vs. CPU')
        gamemode = input()
        if int(gamemode) == 1:
            print('Coming Soon. Sorry :(')
        else:
            print('Game is starting')
            print( '********************************')
            print('please make a selection:')
            print('1. rock')
            print('2. paper')
            print('3. scissor')
            Userselection = input()
            cpuSelection = random.choice(rpsOptions)
            print('user selected:' + userSelection)
            print('cpu selected :' +)


    elif int(selection) == 2:
        print(' Game rules')
    elif int(selection) == 3:
        print("Goodbye...")
    else:
        print("ERROR: Invalid selection. PLease select a listed option from the menu")


rpsGame()


