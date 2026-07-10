menu={"Pizza":1.09,
      "Cake":2.35,
      "Ice-cream":3.54,
      "Pop-corn":2.34,
      "Soda":5.67,
      "Chips":3.45,
      "Nachos":4.34}
cart=[]
total=0

print("-------Menu--------")
for key,value in menu.items():
    print(f"{key:12}: ${value:.2f}")
print("-------------------")

while True:
    food=input("Select an item (q to quit) :").capitalize()
    if food=='Q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total+=menu.get(food)
    else :
        print("Not in menu!")
print()
print("Thanks for your purchase!")
print("---Your items are---")
for x in cart:
    print(x,end=", ")
print()
print(f"Your total : ${total}")
