## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter the starting yearly salary: "))
portion_saved = float(input("Enter the portion of salary to be saved: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual salary raise: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
cost_down_payment = cost_of_dream_home * portion_down_payment
monthly_salary = yearly_salary / 12
monthly_saved_salary = monthly_salary * portion_saved
while(1):
    # If the money still not enough to pay the down payment
    if amount_saved < cost_down_payment:
        months = months + 1
        if months % 6 == 0:
            yearly_salary = yearly_salary + yearly_salary * semi_annual_raise
            monthly_salary = yearly_salary / 12
            monthly_saved_salary = monthly_salary * portion_saved
        amount_saved = (amount_saved + amount_saved * (r / 12)) + monthly_saved_salary
    else:
        break

print(f"Number of months: {months}")