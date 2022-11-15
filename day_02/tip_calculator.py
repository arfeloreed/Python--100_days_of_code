# Tip calculator

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage = float(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
percentage /= 100
tip = bill * percentage
total_bill = bill + tip
number_people = float(input("How many people to split the bill? "))
share_person = round(total_bill / number_people, 2)
share_person = "{:.2f}".format(share_person)
print(f"Each person should pay: ${share_person}")
