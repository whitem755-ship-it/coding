def Submission():
    print("Have you submitted your class work ")

attempts = 0

def Guessing():
    Number = 46
    attempts = 0
    UserNumber = int(input("Please make a guess:"))
    while UserNumber != Number:
        if UserNumber < Number:
            print('your number is to low')
            UserNumber = int(input("please make a guess:"))
            attempts += 1
        else:
            print('your number is to high') 
            UserNumber = int(input("please make a guess:"))
            attempts += 1
    else:
        print("congratulates you guessed the right number")
        print (" attempts =" + str(attempts))
    

Guessing()