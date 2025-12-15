def GPA():
    print("Hello what class's grade would you like submit")
    print("1.Statistics")
    print("2.African american history")
    print("3.Choir")
    print("4.physic")
    print("5.Coding")
    select = int(input('Please select a class:'))
    if select == 1 :
        print("enter your statistics Grade:")
        print(("Week.1 ") +  str(input()))
        print(("Week.2 ") + str(input()))
        print(("Week.3 ") + str(input()))
        print(("Week.4 ") + str(input()))
        print(("Week.5 ") + str(input()))
        print(("Week.6 ") + str(input()))
        print(("Week.7 ") + str(input()))
        print(("Week.8 ") + str(input()))
        print(("Week.9 ") + str(input()))
        print(("Week.10 ") + str(input()))
        print(("Week.11 ") + str(input()))
        print(("Week.12 ") + str(input()))
        print(("Week.13 ") + str(input()))
        print(("Week.14 ") + str(input()))
        print(("Week.15 ") + str(input()))
        print(("Week.16 ") + str(input()))
        print(("Week.17 ") + str(input()))
        total = (Week1 + Week2 + Week3 + Week4 + Week5 + Week6 + Week7 + Week8 + Week9 + Week10 + Week11 + Week12 + Week13 + Week14 + Week15 + Week16 + Week17)
        average = total / 17
        print("your average grade is:" + str(average))


    elif select == 2:
         print("enter your African american history Grade:")
    elif select == 3:
         print("enter your Choir Grade:")
    elif select == 4:
         print("enter your physic Grade:")
    elif select == 5:
          print("enter your Coding Grade:")
    else:
        print("sorry dont understand your selection")

GPA()