#Shopping cart program
items=[]
prices=[]
quantities=[]
x=0
total=0

while True:
    item=input("Enter item to buy('e' to exit) : ")
    item=item.capitalize()
    if item == 'E':
        print("Thanks for purchase!")
        break
    items.append(item)
    x+=1
    price=float(input("Enter price of the item : "))
    prices.append(price)
    quantity=int(input("Enter quantity of the item : "))
    quantities.append(quantity)


print(" ")
print("Your bill :")
print(" ")
print(" Items    |    Quantity    |    Price(per unit)    |    Final price")
print("--------------------------------------------------------------------")
for i in range(0,x) :
    print(f" {items[i]:<14}{quantities[i]:<17}{prices[i]:<24,.2f}{quantities[i]*prices[i]:.2f}")
    total+=quantities[i]*prices[i]
print("--------------------------------------------------------------------")
print(f"                                        Your total :    {total:>4.2f}")
