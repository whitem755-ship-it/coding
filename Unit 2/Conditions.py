# Conditional Statements = code instructions that
# have different outcomes based on the inputted data.
# input --> output

# Conditional Statement Syntax
# if keyword - controls the condition we want to satisfy.

# else keyword - Our default outcome. The thing that
# happens when our conditions are NOT satisfied


Weather = input('what is the weather like today?')
if Weather == 'sunny':
    print("It is beautiful outside. Bring sunglasses.")
elif Weather == 'rainy':
    print(" Remember to bring an umbrella.")
elif Weather == 'windy':
    print("Wear heavy boots")
elif Weather =='chilly':
    print("bring a jacket.")
else:
    print("I cant tell you the weather, but have a good day.")


Password = input('please enter password:')
if Password == 'Boyslatin203':
    print("Welcome you are logged in.")
else:
    print("Sorry try again")

down = input('What down is it?')
yards = input('How many yards do you need to get another first down?')

if down == 1 and yards <= 5:
    print("run it")
elif down == 2 and yards <= 5:
    print("run it")
elif down == 3 and yards <= 5:
    print("play action")
else:
    print("punt")

def testTakerPermit(age):
  if age > 16:
      print("Congratulation you are old enough for your permit")
  else:
      print("You are not old enough for your permit")

testTakerPermit(17)

def etheirOr(Number):
    if Number >= 0:
        print("this is positive")
    else:
        print("this number is negative")

etheirOr(18)

def  letterGrades(Grade):
    if Grade <= 70:
        print("Your grade is an F")
    elif Grade >= 70  <= 80:
        print("Your grade is an C")
    elif Grade >= 80  <= 90:
        print("Your grade is an B")
    elif Grade >= 90:
        print("Your grade is an A")
    else:
        print("Your grade is an F")

letterGrades()