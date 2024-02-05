import math

# Display Options for the user to ask them to Choose a calculator
print ('''investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
''')

calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
calculator_type = calculator_type.lower() # Convert user entry to lower to account for capitalisation

# When Investment is selected
if calculator_type == "investment":
    print ("You selected the Investment Calculator")
    
    # Ask user for Loan details
    deposite_amount = float(input("Enter the Deposite Amount: "))
    interest_rate = float(input("What is the Interest Rate as %: "))
    interest_rate = (interest_rate/100) #convert into decimal %
    invetment_years =  int(input("Over how any Years? "))

    # User input and convert to lower case for error checking
    interest = input("Please choose between 'Simple' and 'Compound' Interest: ") ##### NEED TO ADD AN ERROR FOR IF THEY INPUT SOMTHING WRONG
    interest = interest.lower()

    # Simple Calculation and output
    if interest == "simple":
        simple_interest = deposite_amount*(1+interest_rate*invetment_years)
        print(f"Your expected return will be {simple_interest}.")
    
    # Compound Calculation and output tdh
    elif interest == "compound":
        compound_interest = deposite_amount* math.pow((1+interest_rate),invetment_years)
        print(f"Your expected return will be {compound_interest}.")
    
    # Messsage incase Simple or Compound is not entered
    else:
        print("Error, invalid responce. You must select either'Simple' or 'Compound' interest type.")

# When Bond is selected
elif calculator_type == "bond":

     # Ask user for Bond details
    current_value_of_house = int(input("Enter Current House Value: "))
    monthly_interest_rate = float(input("What is the Interest Rate: "))
    monthly_interest_rate = ((monthly_interest_rate/100)/12) #convert into decimal % then to monthly
    num_months =  int(input("Over how any Months? "))

    # Bond calculation
    monthly_user_payment = (monthly_interest_rate*current_value_of_house)/(1-(1+monthly_interest_rate)**(-num_months))
    print (f"Your monthly replayment will be {monthly_user_payment}.")

#Return if user didn't enter either investment or bond
else:
    print("Error, You must enter either 'Investment' or 'Bond'.")
