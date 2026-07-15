print("Welcome to the Tip Calculator")

# Use float for bills so people can enter decimals (like 150.50)
total_bill = float(input("What was the total bill?\nPKR "))
tip = float(input("How much tip would you like to give?\nPKR "))
split = int(input("How many people are splitting the bill?\n"))

# Calculate the final amounts
final_total_bill = total_bill + tip
bill_per_person = final_total_bill / split

# Round to 2 decimal places using standard parentheses
final_amount = round(bill_per_person, 2)

print(f"Every person should pay: PKR {final_amount}")
