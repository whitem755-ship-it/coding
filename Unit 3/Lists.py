#Lists - a system for collecting and organizing multiple pieces
# of data

# List sytax (how it is written)
# when we want to create a list, we first create a variable name
# and assign it to the square brackets[].
# we then put the data we want to collect inside of 
# the square brackets

ShoppingCart = ['water','ice','cereal','apples']

# Accessing items in a list-
# when we want to  access an item in a list we write the variable name
# and then use the square brackets and pass in the item position in 
# the brackets

#python is a zero-based index language. meaning; when counting
# items, zero is  treated as an actual numbes and is counted.

#print(ShoppingCart[2])

ShoppingCart.append("orange")




def addItemToCart():
    bestBuyCart = ['8k moniter','Graphics Card','Speakers','Pro controller']

    item = input("please add new item:")

    bestBuyCart. append(item)

    print(bestBuyCart)

addItemToCart()

def removeItemformCart():
    bestBuyCart = ['8k moniter','Graphics Card','Speakers','Pro controller']
    
    item = input("please remove an item:")

    bestBuyCart. remove(item)

    print(bestBuyCart)

removeItemformCart()


def numberList():
    List = [100, 23, 450, 63, 1, 6, 19, 1000]

    number = input("please add a number:")

    List .append(number)

    List. sort()
    print(List)


numberList()
