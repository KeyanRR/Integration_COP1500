# Keyan Ridgeway
# Tacos & Tequila menu calculator
# ** is the exponent operator, and I could not find any use for it in this program yet.
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
# The + string operator concatenates strings (joins them together without a space)
# end= joins the end of the line it's on with the next line.
def main():
    print("Hello Guest!")
    print("Tacos!" * 10)

    def choose_taco():  # Lists all taco options
        price = 0.0
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
        user_input = int(input("Enter desired item number:\n"))
        # print(user_input)
        if user_input == 1 or user_input == 5 or user_input == 6:
            price = 4.25
        elif user_input == 2 or user_input == 9:
            price = 4.50
        elif user_input == 3:
            price = 4.75
        elif user_input == 4 or user_input == 7 or user_input == 11 or user_input == 12:
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
            print("invalid input")
        return price

    total = 0.0
    keep_going = True
    while keep_going:
        total += choose_taco()
        print("Add another item?")
        input2 = input("y or n:\n")  # asking yes or no to another taco,
        if input2 != "y" and keep_going == True:  # if no, it will stop and tell you your total.
            keep_going = not True
    print("Your total is $", total, sep="")
    print("Would you like to add a tip?")
    tip = input("y or n:\n")
    def gratuity(total):
        if tip == "y" or tip == "Y":
            print("15% = ", .15 * total)
            print("18% = ", .18 * total)
            print("20% = ", .20 * total)
            tip_amount = int(input("Please Enter desired tip:\n"))
            if tip_amount >= 5:
                print("Thank you for the generous tip!")
                print("Your new total is: ", total + tip_amount)
        else:
            print("Oh ok...")
    gratuity(total)
    for x in range(1):
        print(":)")
    print("Thank you, enjoy!")

main()
