def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return round(discounted_price, 2)
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price == original_price:
    print(f"No discount applied. The price remains ${final_price:.2f}")
else:
    print(f"The discounted price is ${final_price:.2f}")