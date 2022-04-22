"""Tacos & Tequila menu Calculator"""
__author__ = "Keyan Ridgeway"


# Tacos & Tequila menu calculator
# ** is the exponent operator, and I could not find any use for it in
# this program yet.
# Ex: 2**3 = 8
# / is the division operator, and I will use it in the next part.
# Ex: 6/2 = 3
# % is the modulus operator which gives the remainder of the two number divided
# Ex: 5%2 = 1
# // is the floor division operator, which divides,
# then gives the quotient without a remainder.
# Ex: 9//2 = 4
# - is the subtraction operator, and I will use it in the next part.
# Ex: 5-2 = 3
# The + string operator concatenates strings (joins them together
# without a space)
# end= joins the end of the line it's on with the next line.
def main():
    """ The Main function is the interface of the menu, and does everything
    except choosing items and tip.

    :return: The main function returns your total, unless you add a tip, then
    the gratuity function will tell you the new total.
    """
    print("Hello Guest!")
    print("Tacos!" * 10)
    total = 0.0
    keep_going = True
    while keep_going:
        total += choose_taco()
        print("Add another item?")
        input2 = input("Please enter y for yes or n for no:\n")
        # asking yes or no to another item,
        if not input2.isalpha():  # Makes sure the input is a string for
            # yes or no
            print("That is not a y or n, please try again.")
            keep_going = True  # If the input is not a string,
            # it will ask the user again
            input2 = input("Please enter y for yes or n for no:\n")
        if input2 != "y" and keep_going == True:  # if no, it will stop and
            # tell the user their total.
            keep_going = not True
    print("Your total is $", total, sep="")
    print("Would you like to add a tip?")
    tip = input("Please enter y for yes or n for no:\n")
    if not tip.isalpha():  # Makes sure the input is a string for yes or no
        print("That is not a y or n, please try again.")
        tip = input("Please enter y for yes or n for no:\n")
    gratuity(total, tip)
    for x in range(1):
        print(":)")
    print("Thank you, enjoy!")


def choose_taco():  # Lists all taco options
    """ The choose taco function lists all of the menu items with their
     corresponding item number and asks for your selection. Once you select an
     item it will ask if you'd like another item with y or n.

    :return: The choose taco function returns the price of the item chosen.
    """
    price = 0.0
    user_input = 0
    print("Select item number:")
    print("1 signature - $4.25")
    print("2 buff - $4.5")
    print("3 cali - $4.75")
    print("4 pancake - $5.0")
    print("5 sunday - $4.25")
    print("6 backyard - $4.25")
    print("7 cuban - $5.0")
    print("8 korean_s - $5.5")
    print("9 cheeseburger - $4.50")
    print("10 moms - $3.75")
    print("11 south - $5.0")
    print("12 baja - $5.0")
    print("13 po_boy - $5.0")
    print("14 firecracker - $5.0")
    print("15 wellfit_c - $5.75")
    print("16 wellfit_s - $6.5")
    print("17 side_rice - $3.0")
    print("18 side_refried_beans - $3.0")
    print("19 side_black_beans - $3.0")
    print("20 side_rice & side_beans combo - $5.0")
    print("21 fountain_drink - $2.75")
    try:
        user_input = int(input("Enter desired item number:\n"))
    except:
        print("Please try again with the item number you would like")
    # Makes sure that the input is an item number
    # print(user_input)
    if user_input == 1 or user_input == 5 or user_input == 6:
        price = 4.25
    elif user_input == 2 or user_input == 9:
        price = 4.50
    elif user_input == 3:
        price = 4.75
    elif user_input == 4 or user_input == 7 or user_input == 11 or \
            user_input == 12:
        price = 5.00
    elif user_input == 13 or user_input == 14:
        price = 5.00
    elif user_input == 8:
        price = 5.50
    elif user_input == 10:
        price = 3.75
    elif user_input == 15:
        price = 5.75
    elif user_input == 16:
        price = 6.50
    elif user_input == 17 or user_input == 18 or user_input == 19:
        price = 3.00
    elif user_input == 20:
        price = 5.00
    elif user_input == 21:
        price = 2.75
    else:
        print("invalid input. Please try again with desired item number")
        # if the user enters a number that is greater
        # than the largest item number it will tell them it is
        # invalid and ask if they would like to add an item.
    return price


def gratuity(total, tip):
    """ The gratuity function is used when the user says yes to tip, it will
    list common tip percentages with their equivalent dollar value beside it.

    :param total: The total is the total price of all items selected before
     adding a tip.
    :param tip: Tip is determining whether or not the user would like to tip
    with a y or n.
    """
    tip_amount = 0
    if tip == "y" or tip == "Y":
        print("15% = ", .15 * total)
        print("18% = ", .18 * total)
        print("20% = ", .20 * total)
        try:
            tip_amount = float(input("Please Enter desired tip as a floating"
                                     " integer:\n"))
        except:
            print("Please try again with a floating integer Ex. 2.0")
            gratuity(total, tip)
        # Makes sure that the tip amount input is a number
        # It asks for a float, but it will also accept integers.
    if tip_amount >= 2:
        print("Thank you for the generous tip!")
        print("Your new total is: ", total + tip_amount)
    else:
        print("Oh ok...")


if __name__ == "__main__":
    main()
