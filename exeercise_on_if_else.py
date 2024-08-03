import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamp=int(time.strftime('%H'))
# print(timestamp)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
if(timestamp<=11):
 print("GOOD MORNING SIR ")
elif(timestamp<=15):
 print("GOOD AFTRNOON SIR ")
elif(timestamp<=20):
 print("GOOD EVENING SIR ")
else:
 print("GOOD NIGHT SIR ")
 
 
 

 