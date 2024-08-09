def factorial(n):
    result=1
    while(n>0):
       result*=n
       n-=1
    return result

n=int(input("ENTER A NUMBER: "))
print(factorial(n))
