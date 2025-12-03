def Quiz():
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
    else:
        print("Incorrect")

    print("Question.3 is this this a boolean (9034<15904)")
    print(" 1. true")
    print(" 2. flase")
    select = int(input("choose an anwer:"))
    if select == 1:
        print("correct")
    else:
        print("Incorrect")

    print("Question.4 what method would we use to add something to a list")
    print("1. append()")
    print("2. reverse()")
    print("3. count()")
    print("4.copy()")

    


    
 

Quiz()