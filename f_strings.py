line="MY NAME IS {} AND I AM FROM {}"
name=input("ENTER YOUR NAME: ")
place=input("BIRTH PLACE: ")
print(line.format(name,place)) #this is usual way but it is confusing
father=input("ENTER YOUR FATHERS NAME: ")
profession=input("ENTER YOUR FATHERS PROFESSION: ") 
line2=f"MY FATHERS NAME IS{father} AND HE IS{profession}"
print(line2)


