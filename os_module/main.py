import os
if(not os.path.exists("data")): # if the folder named data is not exist
  os.mkdir("data")              # makes a folder named data
for i in range(1,50):           
  os.mkdir(f"data/day{i}")      #creates a folder in data named day1...
for i in range(1,50):
  os.rename(f"data/day{i}",f"data/DAY {i}") #rename the folder
if(not os.path.exists("oslisy.py")):
  os.mkdir("oslisy.py")
folder=os.listdir("data")              #gives the list of folders that are present in data folder
print(folder)
print(os.getcwd())                     # tells us that we are in which directory



