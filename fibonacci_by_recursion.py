def fibonacci(first,second,n):
    if(n==1 or n==0):
        return 0;
    else:
     print(first+second)
     fibonacci(second,first+second,n-1)
n=int(input("ENTER THE TERMS UPTO YOU WANT TO PRINT FIBONACCI SERIES: "))
print("0\n1")
fibonacci(0,1,n)