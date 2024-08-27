dic = {
    1 :"ishan sawarn",
    2 :"rahul sharma",
    3 :"kishan kumar",
    4 :"mukesh kumar",


}
print(dic[3]) #i can make a list of students then i can access them by their roll no
# print(dic[5]) it gives error
print(dic.get(5))# but it does't give error 
print(dic)
print(dic.keys()) #print all the keys of dictionary
print(dic.values()) #print all the values of dictionary
for abc in dic:
    print(f"the value of{abc} is {dic[abc]}")