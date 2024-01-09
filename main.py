from treasure import treasure


def treasure_island_game():
    """
    This function is a script that runs the popular treasure island game.
    Happy playing!
    :return: A string, the end result.
    """

    # Prints the treasure island ascii art
    print(treasure)

    # Prints the welcome message
    print("Welcome to Treasure Island.\nYour mission is to find the Treasure.")

    # Stores the inputted direction
    left_right = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")
    if left_right.lower() == 'left':

        # Stores the inputted decision, if is to wait or swim
        lake = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a "
                     "boat Type 'swim' to swim across\n")
        if lake.lower() == 'wait':

            # Stores the colour of the door chosen
            door = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and "
                         "one blue. Which colour do you choose?\n")
            if door.lower() == 'blue':
                print("You got the Treasure. You Won!!")
                return "You got the Treasure. You Won!!"
            else:
                print("It's a room full of sharks. Game Over!")
                return "It's a room full of sharks. Game Over!"

        else:
            print("You got swallowed by the Sharks, Game Over!")
            return "You got swallowed by the Sharks, Game Over!"

    else:
        print("Wrong Direction. Game Over!")
        return "Wrong Direction. Game Over!"


if __name__ == '__main__':
    treasure_island_game()
