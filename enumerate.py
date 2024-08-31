list=[32,3424,56,232,4,3,756,34,6,43,24,4,63]
#i want to print something at specific index for this we have to do
abc=0
for i in list:
    print(i)
    if(abc==4):
        print("you are at fourth index")
    abc+=1
#this method is not so good that's why we use enumerarte function
marks=[23,34,32,56,29,2,6,3,7,33,6,89,24]
print("by using enumerate function")
for index,i in enumerate(marks):
    print(i) #this will print all elements
    print(index) #this will print index/
    print("sfegrdhtfj")
    print(marks[index])