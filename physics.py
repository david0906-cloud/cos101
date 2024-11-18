# variables
first_name = "David"

# conditionals
# if the first name is david, welcome david
# else if the first name is daniel, welcome daniel
# else (if the first name is neither david nor daniel, say you are not authorised)
if first_name == "David":
    print("Welcome David")
elif first_name == "Daniel":
    print("Welcome Daniel")
else:
    print("You are not authorised")

# functions
def add_two_numbers():
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))

    sum = num1 + num2
    print(sum)

add_two_numbers()