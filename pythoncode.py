items = ["Rice", "Sambar", "Chicken", "Mutton"]
prices = [70, 20, 180, 250]
i = 0
total = 0

print("Index  Items       Prices")
print("-" * 25)
while i < len(items):
    print(f"{i:<6} {items[i]:<11} {prices[i]}")
    i += 1

print("-" * 25)

# Loop to allow purchasing multiple items
while True:
    choice = input("Enter item index to buy (or 'q' to finish): ")
    
    if choice.lower() == 'q':
        break
        
    if choice.isdigit():
        index = int(choice)
        if 0 <= index < len(items):
            qty = int(input(f"Enter quantity for {items[index]}: "))
            cost = prices[index] * qty
            total += cost
            print(f"Added {qty} x {items[index]} = {cost}")
        else:
            print("Invalid item index. Please try again.")
    else:
        print("Please enter a valid number or 'q'.")

print("-" * 25)
print(f"Total Bill: {total}")