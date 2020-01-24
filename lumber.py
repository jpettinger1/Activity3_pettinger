# Lumber price calculator: A basic python program which asks the user to input two numbers for quantity of lumber
# and the grade of lumber desired and returns the final price following a simple calculation.

# repeat is the value that determines is the calculator is rerun, 'y' for yes 'n' for no
repeat = "y"
# total is the total price of the lumber which is calculated then returned to the user
total = 0
# lumberAmount specifies how many feet of lumber the user wants, initialized to -1 to ensure proper input
lumberAmount = -1
# lumberGrade specifies the type of lumber the user wants, initialized to 0 to ensure proper input
lumberGrade = 0
# valid is used as boolean logic to ensure that the value of repeat is proper
valid = 0

print("ISQA 3900 Lumber Price Calculator")
print()

# while loop allows the entire price calculator to be rerun if the user inputs a 'y'
while repeat == "y":
    print("You will be asked for the number of boards in feet you want to purchase as well as the type of lumber "
          "(common or select)")

    while lumberAmount < 0:
        lumberAmount = int(input("Enter number of boards desired in feet:    "))
        if lumberAmount < 0:
            print("Please enter a positive number.")

    while lumberGrade != 1 and lumberGrade != 2:
        lumberGrade = int(input("Enter a 1 for select lumber or a 2 for common lumber: "))
        if lumberGrade != 1 and lumberGrade != 2:
            print("Please enter either a 1 or a 2")

    if lumberGrade == 1:
        total = lumberAmount * 2
    else:
        total = lumberAmount

    if total > 49999:
        total *= .8
    elif total > 9999:
        total *= .9

    print("Total price for the lumber is: {:0.2f}".format(total))
    print()

    while valid == 0:
        repeat = input("continue (y/n)?:  ")
        if repeat != "y" and repeat != "n":
            print("Please enter either a 'y' or a 'n'.")
        else:
            valid = 1

    # values are reset so the calculator can be rerun
    total = 0
    lumberAmount = -1
    lumberGrade = 0
    valid = 0

print("Exiting Calculator.")
