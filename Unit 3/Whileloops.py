# While loop definition - a while loop is a type of construct
#where code instructions will keep on running so
# long as a condition is TRUE (boolean)

# Note - In order to stop a loop (or any program) from running
# in your treminal, click + c at same time.

# while loop syntax

def ageCheck():
    ageVerification = 18
    purchaserAge = int(input("please enter your age:"))

    while ageVerification >= purchaserAge: # 17 >= 15 TRUE: 17 is larger than 15
        print("Sorry your not old enough")
    else:
        print('Enjoy your collectors edition of DOOM')

def password():
    savePassword = '123abc'
    userPassword = input("please type in your password: ")
    attempts = 0
    while savePassword != userPassword:
        print('incorrect password')
        attempts += 1
        print('number of attempts left: '+ str(attempts) +'/ 3')
        userPassword = input ('please try again: ')
        if attempts == 3:
            print('You made too many incorrect attempts. your account has been locked')
            break
    else:
        print('welcome to your account')

password()

number = 0
while number < 10:
    number += 1
    print(number)
else:
    print("done counting")


timer = 30
while timer > 0:
    timer -=  1
    print(timer)
else:
    print("done counting")
    

