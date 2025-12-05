def Quiz():
    score = 0
    print("Start Quiz")
  
    print("Question.1 What Operator family does this = belong to. ")
    print(" 1. Arithmetic")
    print(" 2. Comparison")
    print(" 3. Logical")
    print(" 4. Assignment")
    print(" 5. None of the above ")
    select = int(input("choose an anwer:"))
    if select == 4:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")
    
    print("Question.2 What datatype is 670.257")
    print("1. float ")
    print("2. Integer ")
    print("3.boolean ")
    print("4. Strings ")
    select = int(input("choose an anwer:"))
    if select == 1:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")

    print("Question.3 is this this a boolean (9034<15904)")
    print(" 1. true")
    print(" 2. flase")
    select = int(input("choose an anwer:"))
    if select == 1:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")

    print("Question.4 what method would we use to add something to a list")
    print("1. append()")
    print("2. reverse()")
    print("3. count()")
    print("4.copy()")
    select = int(input("choose an anwer:"))
    if select == 1:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")

    print("Question.5 what symbol would you use to make a comment")
    print(" 1. =")
    print(" 2. +")
    print(" 3. #")
    print("4. ==")
    select = int(input("choose an anwer:"))
    if select == 3:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")

    print("Question.6 what does this == symbol")
    print ("1. Comaring if the values are  The SAME")
    print("2. Checks and compares if certain code condition are true or false")
    print("3. Assign value to variables ")
    print("4. None of the above")
    select = int(input("choose an anwer:"))
    if select == 1:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")
    print("Question.7 what symbol do we use to multiply two or more numbers")
    print("1. #")
    print("2. !=")
    print("3. *=")
    print("4. /=")
    select = int(input("choose an anwer:"))
    if select == 3:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")

    print("Question.8 what is the definition of a Syntax error")
    print("1. The computer has detected an issue with how your code is written.")
    print("2. The computer has detected an issue with a function, specifically how the function is")
    print("3. An issue with how you using data type")
    print("4. The computer has detected a math issue")
    select = int(input("choose an anwer:"))
    if select == 1:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")
    print("Question.9 what symbol do we use to subtract")
    print("1. !=")
    print("2. #")
    print("3. -=")
    print("4.==")
    select = int(input("choose an anwer:"))
    if select == 3:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")
    print("Question.10 what is the definition of Data casting")
    print("1. Changing one data type to another data type")
    print("2. Pre-written code that is stored in the programming language.")
    print("3. Users to type data into a program and assign it to a variable")
    print("4. Combine 2 or more string together using the plus symbol.")
    select = int(input("choose an anwer:"))
    if select == 1:
        print("correct")
        score = score + 1
    else:
        print("Incorrect")
print("The final score of correct answers is:" + str(score))

Quiz()