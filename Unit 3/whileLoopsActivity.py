def list():
    Numbers = []
    Numberlist = input("please put a number in:")
   
    while Numberlist != 'quit':
       tranformNumber = int(Numberlist)
       Numberlist = input("please put a number in:")
       Numbers.append( tranformNumber)
       print(Numbers) 
       Numberlist = input("please put a number in:")
    else:
        print('Stop')


def Numberlist():
    lists = []
    Numbers = input("enter a number:")

    while Numbers != 'quit':
        tranforNumber = int(Numbers)
        Numbers = input("enter a number:")
        lists.append


def Guessing():
    Number = 46
    UserNumber = int(input("Please make a guess:"))
    while UserNumber != Number:
        if UserNumber < Number:
            print('your number is to low')
            UserNumber = int(input("please make a guess:"))
        else:
            print('your number is to high') 
            UserNumber = int(input("please make a guess:"))
    else:
        print("congratulates you guessed the right number")
    

Guessing()