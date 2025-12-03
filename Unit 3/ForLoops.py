# A loop is a construct in programming that allows us to repeat a process until
# a certain condition is met

# For Loops - A type of construct that runs  code instructions
# a finite amount of times over a group of data.

halloweenBag = ['snickers','Hershy Bar', 'Twizzler', 'Candied Apple','candy corn', 'Twix', 'Nerds']

count = len(halloweenBag)
print(count)

# i is a variable and is short for iterator.
for candy in halloweenBag:
    print(candy)
    print('i got this candy in my bag ' + candy) 

# Use a for loop to ask a user to type in 5 words andd print each word out in
# the terminal. Once the user has finished typing 5 words
# the for loop should end.

def Letter():

    for x in range(5):
        word = input("Type in a word ")
        print(word)

Letter()

def checkout():
    groceryBag = [1, 20, 3, 6, 7]
    Total = 0



