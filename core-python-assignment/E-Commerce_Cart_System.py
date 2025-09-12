def calculate_total(cart):
    if not cart:
        return 0
    total=sum(cart.values())
    if len(cart)>5:
        total*=0.9
    return total
cart_items={}
n=int(input("Enter number of items in cart: "))
for _ in range(n):
    item=input("Enter item name: ")
    price=int(input(f"Enter price of {item}: "))
    cart_items[item]=price
print("Total Price:", calculate_total(cart_items))
