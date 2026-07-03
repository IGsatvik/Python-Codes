#Interest generator
p=0
f=0
r=0
t=0
while p<=0 :
    p=float(input("Enter the principle amount :"))
    if p<=0 :
        print("Enter a valid amount!")

while r<=0 :
    r=float(input("Enter the rate of interest :"))
    if r<=0 :
        print("Enter a valid amount!")

while t<=0 :
    t=float(input("Enter the time period :"))
    if t<=0 :
        print("Enter a valid amount!")

print(f"Final amount will be {p*(1+(r/100)**t)}")
