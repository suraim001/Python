# Shopping cart program

item = input("What would you like to buy? : ")
price = float(input(f"What is the price of a/an {item}? : "))
quantity = int(input(f"How many {item}s would you like to purchase? : "))

total = quantity * price
print(f"\nYou have bought {quantity} {item}/s.")
print(f"And yu have to pay a total of {total} TK for your purchase.")