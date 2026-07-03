#Timer
import time
print("Enter time to start timer : ")
a=int(input("Enter hours : "))
b=int(input("Enter minutes : "))
c=int(input("Enter seconds : "))

t=a*3600+b*60+c
for x in reversed(range(0,t)) :
    print(f"{x} seconds remaining")
    time.sleep(1)
print("Times up!")
