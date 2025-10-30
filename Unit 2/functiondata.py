# how to create a function that passes data

# step 1. create a function definition
def bnbRefund(username, refundAmount):
    print('sorry' +  username  + 'for your cancellation')
    print('we will refund $'+ str(refundAmount) +' to your bank.')

 # step 2. Call the function/ execute instruction
bnbRefund('jaden', 3000)



def bdayMsg(name, bday):
    print("My name is" + name + "and my brithday is" + bday)
    
bdayMsg('Micah', 'Jan 13')

def dollarConverter(dollar):
    
    pennies= dollar + 100
    print('My' + str(dollar) + 'dollar(s) is equal to' + str(pennies) + 'pennies')

dollarConverter(4765)

def tringle(length, width):
    area = length * width * 0.5
    
    print('the area of a tringle' + str(area) )

tringle(20, 15)



