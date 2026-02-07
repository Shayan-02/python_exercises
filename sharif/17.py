def ham_price_calculator(chicken_price, meat_price, other_ingredients_price, meat_type, percentage):
    # Calculate the price based on the chosen meat type and percentage
    if meat_type == "chicken":
        print("mixing and packing")
        total_price = (chicken_price * percentage / 100) + other_ingredients_price
        print(f"The final price of the ham: {total_price} dollars")
    elif meat_type == "meat":
        print("mixing and packing")
        total_price = (meat_price * percentage / 100) + other_ingredients_price
        print(f"The final price of the ham: {total_price} dollars")
    else:
        print("Invalid meat type selected.")


# Prices
chicken_price = 5  # Price per unit of chicken
meat_price = 10  # Price per unit of meat
other_ingredients_price = 2  # Price of other ingredients (fixed)

# Get user input
meat_type = input("Enter the type of meat (chicken or meat): ")
percentage = float(input(f"Enter the percentage of {meat_type} in the ham: "))

# Calculate and display the price
price = ham_price_calculator(chicken_price, meat_price, other_ingredients_price, meat_type, percentage)
