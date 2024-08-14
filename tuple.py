# the major differnece between tuple and list is that you can't change tuple
tup=(1,2,3,4,"earth",12,56,78,34,23,)#you have to remember that what bracket you have used
print(type(tup),tup)
# tup[0]=9 This will give you error because you can't change tupple
list=[9,7,6,5]
list[0]=12 #but this will work because it is list (it is declared in square brackets)
print(type(list),list)
if "earth" in tup:
    print("yes,earth is in tuple")
print(tup[0:9:2])# sliceing
