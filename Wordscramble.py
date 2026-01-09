import random


def wordScramble():
    words = ["japanese","mississippi","psyscosis","psycheldelic"]
    correctWord = ""
    attempt = 0
    print("Welcome to Word Scramble! ")
    randomSelect = random.randint(0,3)
   
    if randomSelect == 0:
        correctWord = words[0]
    elif randomSelect == 1:
        correctWord = words[1]
    elif randomSelect == 2:
        correctWord = words[2]
    elif randomSelect == 3:
        correctWord = words[3]
    
    convertedstring = list(correctWord)
    random.shuffle(convertedstring)
    scrambled = "".join(convertedstring)
    print(scrambled)
    print("please guess the correct word: ")
    userGuess = input()
    while userGuess != correctWord:
        print("incorrect, please try again: ")
        attempt += 1
        print("attempts left: " + str(attempt) + "/3")
        if attempt == 3:
            print(" sorry your out of Attempts, heres the correct word:" + correctWord)
            break
        userGuess = input()
    if userGuess == correctWord:
        print("correct!")
    else:
        print("oh sorry your wrong")
wordScramble()