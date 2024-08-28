a=(input("Enter a number : "))
print(f"MULTIPLICATION TABLE OF{a} is ")
try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print(e)
#in this program if we give wrong input like if we give char input then the program will not stop because of an error
#we can also handle the specific error
try:
   b=int(input("Enter a number: "))
except ValueError:
    print("Input is not an integer")
finally:
    print("its done")


