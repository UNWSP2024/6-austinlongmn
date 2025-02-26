# Programmer: Austin Long
# Date: 2025-02-26
# Program: Tax Rate

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

# Pseudocode:
# Input total_sales from user
# If user input is invalid then
#   Display error message
#   Repeat from "Input total_sales ..."
# Set county_tax_amount to total_sales * 0.025
# Set state_tax_amount to total_sales * 0.05
# Set total_tax_amount to county_tax_amount + state_tax_amount
# Display county_tax_amount, state_tax_amount, and total_tax_amount

# Get sales from user, with validation
def get_total_sales() -> float:
    try:
        # Prompt for input
        return float(input("Enter the total sales for the month: $"))
    except ValueError:
        # If input is bad, then display error message and prompt again
        print("Error: you must enter a number without currency characters.")
        return get_total_sales()


# Set tax rates
COUNTY_TAX_RATE = 0.025
STATE_TAX_RATE = 0.05

def main():
    # Get sales from user
    total_sales = get_total_sales()

    # Calculate tax amounts
    county_tax_amount = total_sales * COUNTY_TAX_RATE
    state_tax_amount = total_sales * STATE_TAX_RATE
    total_tax_amount = county_tax_amount + state_tax_amount

    # Display tax amounts to user
    print(f"County tax amount: ${county_tax_amount:,.2f}")
    print(f"State tax amount: ${state_tax_amount:,.2f}")
    print(f"Total tax amount: ${total_tax_amount:,.2f}")


# Run the program
if __name__ == "__main__":
    main()
