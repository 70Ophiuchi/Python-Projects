import time
import random


def print_pause(phrase):
    print(phrase)
    time.sleep(2)


def main():
    inventory = []
    choice = random.choice(["Moon", "Hilly", "Dungeon"])  # CHOOSE SCENARIO
    if choice == "Moon":
        surroundings = ("on the darkside of the moon, to your left is the D" +
                        "eep Crater and your Landing Rover on the right side.")
        place1 = "The Deep Crater"
        place2 = "The Landing Rover"
        Monster = "Moon Monster"
    elif choice == "Hilly":
        surroundings = ("in a grassy area surrounded by hills, to your left" +
                        " is the Dark Cave and an Eerie Cabin to your right.")
        place1 = "The Dark Cave"
        place2 = "The Eerie Cabin"
        Monster = "Scary Giant"
    elif choice == "Dungeon":
        surroundings = ("in a dark dungeon with a Dark Room to " +
                        "your left and the Dragons lair to your right!")
        place1 = "The Dark Room"
        place2 = "The Dragons Lair"
        Monster = "Dragon"
    surrounding = str(surroundings)

    def intro():  # INTRODUCTION
        print_pause("You wake up confused from a very deep sleep, " +
                    "you have no memory of what happened to you.")
        print_pause("You find yourself stranded " + surrounding +
                    "\nYou hear a " + Monster +
                    " nearby! The sound seems to be coming from your right")

    def input_validation(choices, prompt):
        while True:
            options = input(prompt).lower()
            if options in choices:
                return options
            print_pause("Please enter a valid choice")

    def main_plot():  # MAIN STORY
        user_input = input_validation(
                            ["1", "2", "inventory"],
                            "\nWhere would you like to go?\nEnter '1'" +
                            "to go to the " + place1 + "\nEnter" +
                            " '2' to go to the " + place2 + "\n" +
                            "Enter 'inventory' to check your items\n"
                                    )

        if user_input == "1":
            random_item = random.choice([
                                        "a Laser Blaster!",
                                        "Nothing Unfortunately",
                                        "an Unbreakable Obsidian Sword",
                                        "a Shiny Golden Apple"
                                        ])
            print_pause("\nYou make your way to " + place1)
            if len(inventory) == 0:
                print_pause(
                            "Upon entering the " + place1 + " you " +
                            "find " + random_item
                            )
                if random_item == "Nothing Unfortunately":
                    print_pause("Well, thats unfortunate. Look closer" +
                                " next time and maybe you'll find something!")
                    main_plot()
                else:
                    inventory.append(random_item)
                print_pause("You make your way back outside")
                main_plot()
            elif len(inventory) > 0:
                print_pause("There is nothing more for you in " + place1)
                print_pause("Disappointed, you make your way back outside")
                main_plot()

        elif user_input == "2":
            print_pause("You make your way to " + place2)
            if len(inventory) == 0:
                print_pause(
                            "This is the " + Monster + "'s hideout! " +
                            "You don't " +
                            "feel prepared for this fight! " +
                            "What would you like to do?\n"
                            )
                user_input = input_validation(
                                        ["1", "2"],
                                        "Enter '1' to run away\nEnter " +
                                        "'2' to fight the " + Monster + "\n"
                                                )
                if user_input == "1":
                    print_pause(
                                "You manage to escape and" +
                                "make your way outside"
                                )
                    main_plot()
                elif user_input == "2":
                    print_pause("You weren't prepared for th" +
                                "e fight, the " + Monster + " " +
                                "demolished you in seconds, " +
                                "better luck next time!"
                                )
                    play_again()
            elif len(inventory) > 0:
                if "a Shiny Golden Apple" in inventory:
                    print_pause("Confused, you eat the weird apple and" +
                                "get ready to fight the " + Monster)
                    time.sleep(2)
                    print_pause("The apple gave you superpowers! you get a" +
                                "great hit on the " + Monster)
                    time.sleep(3)
                    print_pause(
                                "The " + Monster + " is no match for" +
                                " your superpowers," +
                                " you win the fierce fight " +
                                "easily and destroy the threat!"
                                )
                    play_again()
                else:
                    print_pause("THIS IS THE " + Monster + "'s HIDEOUT")
                    print_pause("You get ready to fight the " + Monster)
                    print_pause("You get a great hit on the " + Monster)
                    time.sleep(3)
                    print_pause(
                                "The " + Monster + " is no match" +
                                " for your skills, " +
                                "you win the fierce fight" +
                                "easily and destroy the threat!"
                                )
                    play_again()

        elif "inventory" in user_input:
            if len(inventory) == 0:
                print("Your inventory is empty!")
                main_plot()
            else:
                print(inventory)
                main_plot()

        else:
            print_pause("Please choose a valid option")
            main_plot()

    def play_again():
        answer = input_validation(
                                ["yes", "no"],
                                "Would you like to play again?" +
                                " Reply with 'Yes' or 'No'\n"
                                ).lower()
        if "yes" in answer:
            main()
        elif "no" in answer:
            print_pause("Okay, thanks for playing. Good bye!")
            exit()

    intro()
    main_plot()


main()
