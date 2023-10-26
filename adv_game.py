name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a empty highway, it has come to an intersection and and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a Stop with a forest and a river, you can walk around in the forest or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by a piranha .")
    elif answer == "walk":
        print("You walked for many miles, then sat down to take a risk and were bitten by a snake.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and he kills you.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)