#we cant store duplicates in set 
s={2,2,6,2}
print(s) #it will not give any error but it prints only 2,6
a=[4,6,87,3,8,2,9,4,0,4,8,5,8,2,9] #we have created a list that have many duplicATES
b=set(a)# we make a copy of that list but as a set so now we have dont have any duplicate in our variable
print(b)
ishan={}#here we tried to make a empty set but it creates as a dict
print(type(ishan))
#for a empty set we need to declare as
sawarn=set()
print(type(sawarn))