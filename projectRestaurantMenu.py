# Define the menu of restaurant

restaurantMenu={
    "pizza":350,
    "Pasta":200,
    "Burger":190,
    "Salad":120,
    "Coffee":150
}
# customer greet to Binod restaurant
print("Welcome to Newar Restaurant")
print("Pizza:RS 350\nPasta:RS 200\nBurger:RS 190\nSalad:RS 120\nCoffee:RS 150")
# 550+200=750
total_order=0
item_1=input("Enter the name of item that you want to order:")
if item_1 in restaurantMenu:
    total_order+=restaurantMenu[item_1] #0+350
    print(f"Your items {item_1} has been added to your order")
else:
    print(f"the items{item_1} you have order is not available.sorry")

another_order=input("Do you want to add another items? (Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of second item:")
    if item_2 in restaurantMenu:
        total_order+=restaurantMenu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")
print(f"The total amount you have to to Newar reataurant is {total_order}")

