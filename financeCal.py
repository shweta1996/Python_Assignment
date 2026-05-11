#Calculate profit or loss percentage 
cost_price = 500
selling_price = 600 

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    
    print("Profit =", profit)
    print("Profit Percentage =", profit_percentage, "%")

elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    
    print("Loss =", loss)
    print("Loss Percentage =", loss_percentage, "%")

else:
    print("No Profit No Loss")

#Calculate simple interest 
principal = 10000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("\n")
print("Simple Interest =", simple_interest)

# Calculate Compound Interest
principal2 = 10000
rate2 = 5
time2 = 2
amount = principal2 * (1 + rate2 / 100) ** time2
compound_interest = amount - principal2
print("\n")
print("Compound Interest =", compound_interest)

# Calculate Tax on Income
income = 500000
tax_rate = 10
tax = (income * tax_rate) / 100
print("\n")
print("Tax =", tax)

# Calculate Percentage Increase or Decrease
initial_value = 200
final_value = 250
percentage_change = ((final_value - initial_value) / initial_value) * 100
if final_value > initial_value:
    print("Percentage Increase =", percentage_change, "%")
elif initial_value > final_value:
    print("Percentage Decrease =", abs(percentage_change), "%")
else:
    print("No Change")