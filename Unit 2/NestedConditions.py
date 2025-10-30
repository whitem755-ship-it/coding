# Nested conditions = Are if/else block of code that contain
# more if/else block of code- conditions that have conditions.

def coffeShop():
    print("Welcome to kimble Coffee. what would you like?")
    print('1. hot drinks')
    print('2. cold drink')
    print('3. snack')
    print('4. hot food')
    select = input('what would you like, please enter a number')
    if drink == 1:
        print("here is our hot drink menu")
        print("1. coffee")
        print('2. tea')
        print('3. latte')
        drink = int(input("select a drink"))
        if drink == 1:
            print("would you like a S, M, L, XL")
        if drink == 2:
            print("which flavor would you like?")
            print('ice coffee')
            print('ice tea')
            print('frappachino')
        

def atm():
    balance = 5000
    pin = 3245
    print("welcome, please type in your pin number: ")
    userPin = int(input())
    if userPin == pin:
        print("welcome what would you like to do? ")
        print("1. withdraw money")
        print("2.Deposit money")
        print("3. check balance")
        select = int(input("please select an option: "))
        if select == 1:
            print('How much would you like to withdraw?')
            amount = int(input())
            if amount > balance:
                print("overdraft alert")
                print("you dont  have enough to take out that, broke boy")
            else:
                newBalance = balance - amount
                print("you are taking out:" + str(amount))
                print("you have this amount left" + str(newBalance))
        elif select == 2:
            print("How much would you like deposit ")
            amount = int(input())
            newBalance = balance + amount 
            print("you New balance is |" + str(newBalance))

        elif select == 3:
            print("this is your current balance" + str(amount))
        else:
         print("sorry dont understand your selection")
    else:
        print("pin is incorrect ")

atm()