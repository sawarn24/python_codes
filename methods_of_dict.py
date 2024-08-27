name1={
    122 : "ishan",
    123 : "rahul",
    145 : "manish" 
}
name2={
    189 : "sahil",
    165 : "umesh"
}
name1.update(name2)
for abc in name1:
    print(f"{abc} is {name1[abc]}")
name2.clear() #delete all the items of a dict
print(name2)
name1.pop(123) #removes a particular item
print(name1)
name1.popitem() #remove the last item
print(name1)
del name2 #deletes the dict