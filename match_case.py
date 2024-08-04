x=int(input("ENTER A NUMBER : "))
match x:
    case 1:
        print("1 CAN BE WRITTEN AS I")
    case 2:
        print("2 CAN BE WRITTEN AS II")
    case 3:
        print("3 CAN BE WRITTEN AS III")
    case 4:
        print("4 CAN BE WRITTEN AS IV")
    case 5:
        print("5 CAN BE WRITTEN AS V")
    case 6:
        print("6 CAN BE WRITTEN AS VI")
    case 7:
        print("7 CAN BE WRITTEN AS VII")
    case 8:
        print("8 CAN BE WRITTEN AS VIII")
    case 9:
        print("9 CAN BE WRITTEN AS IX")
    case 10:
        print("10 CAN BE WRITTEN AS X")
    case _ if x>10:
        print("INPUT IS MORE THAN 10")
    case _ if x<1:
        print("INPUT IS LESS THAN ONE")
    


