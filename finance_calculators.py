'''This Python script provides two financial calculators: an Investment Calculator and a
Bond Calculator. Users can choose between these options to calculate either the expected
return on an investment or the monthly repayment amount for a home loan.'''

import math

# Display options for the user and ask them to choose a calculator
print ('''Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a home loan
''')

calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")\
    .lower()

# When investment is selected
if calculator_type == "investment":
    print ("You selected the Investment Calculator")
    
    # Ask user for Loan details
    deposit_amount = float(input("Enter the Deposit Amount: "))
    interest_rate = float(input("What is the Interest Rate as %: "))
    interest_rate = interest_rate/100 #convert into decimal %
    investment_years =  int(input("Over how any Years? "))

    # User input and convert to lower case for error checking
    interest = input("Please choose between 'Simple' and 'Compound' Interest: ")
    interest = interest.lower()

    # Simple calculation and output
    if interest == "simple":
        simple_interest = deposit_amount*(1+interest_rate*investment_years)
        print(f"Your expected return will be £{simple_interest:.2f}.")
    
    # Compound calculation and output
    elif interest == "compound":
        compound_interest = deposit_amount* math.pow((1+interest_rate),investment_years)
        print(f"Your expected return will be £{compound_interest:.2f}.")
    
    # Message in case simple or compound is not entered
    else:
        print("Error, invalid response. You must select either'Simple' or 'Compound' interest type.")

# When bond is selected
elif calculator_type == "bond":

     # Ask user for bond details
    current_value_of_house = int(input("Enter Current House Value: "))
    monthly_interest_rate = float(input("What is the Interest Rate: "))
    monthly_interest_rate = (monthly_interest_rate/100)/12 #convert into decimal % then to monthly
    num_months =  int(input("Over how any Months? "))

    # Bond calculation
    monthly_user_payment = \
        (monthly_interest_rate*current_value_of_house)/(1-(1+monthly_interest_rate)**(-num_months))
    print (f"Your monthly repayment will be £{monthly_user_payment:.2f}.")

# Return if user didn't enter either investment or bond
else:
    print("Error, You must enter either 'Investment' or 'Bond'.")
