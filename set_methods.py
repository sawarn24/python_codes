s1={3,8,3,8,0,4}
s2={5,9,3,7,0,3,2}
print(s2.union(s1))#print union of both the set
#but in this our original sets are untouched but if we want that our set 1 updates as union of both sets
s1.update(s2)
print(s1)
s3={3,8,3,8,0,4}
s4={5,9,3,7,0,3,2}
print(s4.intersection(s3))#prints intersection but original sets are untouched
s4.intersection_update(s3)#updates s4 as intersection of both sets
print (s4)
name={"ishan","rahul","sawarn","ayush"}
name2={"kishan","ishan","rahul","mohan"}
print(name.symmetric_difference(name2))#symmentric differens means that elements that are not in common
name.symmetric_difference_update(name2)#updating name as symmetric difference of both
print(name)
num={2,4,6,9,4,68}
num2={5,2,7,0,5,8,3,1,8}
print(num.difference(num2))# prints that are present in num1 but not in num2
num.difference_update(num2)
city={"delhi","pune","mumbai","kolkata"}
city2={"lucknow","kashmir","punjab"}
print(city.isdisjoint(city2))#this prints true if no element are common in both set
city3={"pune","mumbai","kolkata"}
print(city.issuperset(city3))#prints true if city contains all the elements of city3
print(city3.issubset(city))#prints true if all the elemts of city3 are in city
city.add("kerla")#add the element in set
print(city)
city.remove("kerla")
print(city)#remove the element from set
print(city.pop())#prints the random one from city set
city.clear()#deletes the all item of city set
print(city)
