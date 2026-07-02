unit = input("Enter current unit of temperature (C/F): ")
temp = float(input("Enter the temperature : "))

if unit =='C' or unit == 'c':
    temp=((temp*9/5)+32,2)
    print(f"Temperature in fahrenheit : {temp} F")
elif unit == 'f' or unit =='F':
    temp=round((temp-32)*5/9,2)
    print(f"Temperature in celsius : {temp} C")
else :
    print("Not a valid unit for temperature!")
