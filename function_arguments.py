def average(a=3,b=9):# here it is called default arguments
    print("AVERAGE IS ",(a+b)/2)

average() #here it goes without argument and gives result with 3 and 9
average(4,10) #here function ignores the default arguments and gives result according to required arguments
average(b=7,a=1)#here we can give arguments in any order by telling their name it is called keyword argument


