"""ASSIGNMENT #4: YOU HAVE BEEN HIRED FINALLY BY THE 21 Century as a Senior Programmer and you've been tasked to help
in revamping their credit rating system and loan issuing system. Just remember, your job is to make things happen.
As a Sr. Developer in Python Programming, all the lights and attention are turned towards you and there is a job to be
done to deliver this critical system on time.

Your job is to design a simple program to allow the loan officer(s) to enter the customer particulars at the terminal
and determine if a customer is credit worthy.

Based on their loan officer's entry, your system is required to get the best desired OUTPUT.

Please design a program to do the input entry, do the desired calculations and come up with the needed requirements and
output them as needed. Please consider all the needed variable. If you need to add any, please do add if need is there.
Good luck."""

# Enter the price of the House you wish to Buy
print("Enter the house price: ")
price = float(input())

# Enter the first name
first_name = input("Enter the First Name: ")

# Enter the last name
last_name = input("Enter the Last Name: ")

fullname = f"{first_name} {last_name}"

# Enter the email
email = input("Enter email address: ")

# Enter the phone number
phone = input("Enter the phone number: ")

# Enter the mailing
physical_address = input("Enter the physical address")

# Enter the city
print("Enter the City")
city = input()

# Enter the zip code
print("Enter the zip code")
zipcode = input()


# Qualify for loans with the best interest rates

credit_score = int(input("Enter credits score: "))
down_payment = 0
status = " "
if credit_score in range(780, 851):
    status = "Excellent Credit"
    down_payment = 0.10 * price

# Usually qualify for loans with the best interest rates
elif credit_score in range(740, 780):
    status = "Very Good"
    down_payment = 0.2 * price

# May face slightly higher loan Interest rates
elif credit_score in range(720, 740):
    status = "Above Average"
    down_payment = 0.3 * price
# May qualify for most loans of higher interest rates
elif credit_score in range(680, 720):
    status = "Average"
    down_payment = 0.4 * price

# May qualify for most loans at significant higher Interest rates
elif credit_score in range(620, 680):
    status = "Below Average"
    down_payment = 0.5 * price

# Usually has some credit issues; will probably not qualify for most loans
elif credit_score in range(580, 620):
    status = "Poor Credit Score"
    down_payment = 0.6 * price

# Facing extreme credit issue
elif credit_score in range(521):
    status = "Poor Credit Score"
    down_payment = 0.7 * price
else:
    print("invalid")


print("OUTPUT OF THE PROGRAM".center(60, "="))
print(f"Full Names: {fullname}")
print(f"Physical Address: {physical_address}")
print(f"City: {city}")
print(f"New House Price: {price}")
print(f"Down Payment: {down_payment}")
print(f"Credit Score: {credit_score}")
print(f"Credit Status: {status}")
print(f"CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOME - {fullname}")
print("=".center(60, "="))
