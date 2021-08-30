import time 


def print_sleep(phrase):
    print(phrase)
    time.sleep(1)
    

def intro():
    print_sleep("You've arrived at your new job")
    print_sleep("You get familiar with your work environment and make your way to the elevator")
    print_sleep("You are now inside the elevator\n")




def floor1(list):
    print_sleep("You pushed the button for the 1st floor")
    print_sleep("You've arrived at the reception on floor 1\n")
    if "ID Card" in list:
        print_sleep("The clerk has given you your ID Card! There is nothing more left to do on this floor")
    else:
        print_sleep("The clerk greets you and gives you your ID Card")
        list.append("ID Card")
    print_sleep("Where would you like to go next?")


def floor2(list):
    print_sleep("You pushed the button for the 2nd floor")
    print_sleep("You've arrived at the managers office on floor 2\n")
    if "SUPER Secret book" in list:
        print_sleep("The manager already gave you your SUPER Secret book! There is nothing more left to do on this floor")
    elif "ID Card" in list:
        print_sleep("The manager greets you and gives you your SUPER Secret book!")
        list.append("SUPER Secret book")
    else:
        print_sleep("You need your ID Card to collect your SUPER Secret book")
    print_sleep("Where would you like to go next?")


def floor3(list):
    print_sleep("You pushed the button for the 3rd floor")
    print_sleep("You've arrived at your office on floor 3\n"
                "You find a locked door infront of you that requires a card to unlock")
    if "ID Card" in list:
        print_sleep("You unlock the door using your ID Card\n" 
                    "only to find yourself at another locked door")
        if "SUPER Secret book" in list:
            print_sleep("You unlock the door using your SUPER Secret book\n"
                        "You've finally arrived at your office, welcome to your first day of work!")
            response = input("Would you like to return to the elevator?\n").lower()
            if "no" in response:
                print_sleep("Okay, good luck with your new job!")
                exit()
            elif "yes" in response:
                print_sleep("Back to the elevator we go!")
        else:
            print_sleep("You have to get your SUPER Secret book from the manager to unlock this door!")
    else:
        print_sleep("You need your ID Card to unlock this door, please get it from the clerk\n")

    print_sleep("You head back to the elevator")


def error():
    print_sleep("Please choose from the following list only!")


def leave():
    print_sleep("Good bye, the elevator awaits your next visit!")


def inventory(list):
    if len(list) == 0:
        print_sleep("Your inventory is empty!\n")
    else:
        print_sleep(list)


def floor(list):

    response = input("Which floor would you like to go to?\n"
                                "1. Reception\n"
                                "2. Managers Office\n"
                                "3. Offices\n"
                                "Reply with 'leave' to exit the elevator\n"
                                "Reply with inventory to view the items you have\n")

    if "1" in response:
        floor1(list)
        floor(list)
    elif "2" in response:
        floor2(list)
        floor(list)
    elif "3" in response:
        floor3(list)
        floor(list)
    elif "leave" in response:
        leave()
    elif "inventory" in response:
        inventory(list)
        floor(list)
    else:
        error()
        floor(list)


def play_game():
    items = []
    intro()
    floor(items)

play_game()
