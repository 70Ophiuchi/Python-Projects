import time
import random

i1 = random.choice(["hash browns", "milk with cookies", "omelette"])
i2 = random.choice(["banana pudding", "fried egg", "home style fries", "pancakes"])


def greeting():
    
    print("Hello, my name is Jack and "
        "I will be assisting you with your order today.\n")
    print("The two items on our menu today are: " + i1 + ' and ' + i2) 


def order():
    choice = input("What would you like to order? " + i1 + ' or ' + i2 + "\n: ")
    output = choice.casefold()
    item2 = i2.casefold()
    item1 = i1.casefold()
    while True:
        if output.find(item1) != -1:
            return i1 + "! Your order will be ready soon."
        
        if output.find(item2) != -1:
            return i2 + "! Your order will be ready soon."
        
        elif choice != i1 or choice != i2:
            del choice
            del output
            print("Please select an item from todays menu only.")
            choice = input("What would you like to order? " + i1 + ' or ' + i2 + "\n: ")
            output = choice.casefold()

def afterorder():
    choice2 = input("Would you like to order anything else? reply with 'yes' or 'no': ")

    output2 = choice2.casefold()
    item2 = i2.casefold()
    item1 = i1.casefold()

      
    while True:
        if output2.find("yes") == False or output2.find("no") == False:
            del choice2
            del output2
            choice2 = input("Please reply with 'yes' or 'no' only")
            output2 = choice2.casefold()  
        if output2 == "yes":
            del choice2
            del output2
            choice2 = input("Okay, what else would you like to order? (reply with no to cancel)" + " " + item1 + " or " + item2 + "\n:")
            output2 = choice2.casefold()
            if choice2.find(item1) != -1:
                return item1 + "! coming up!"
            elif choice2.find(item2) != -1:
                return item2 + "! coming up"
            elif choice2 != i1 or choice2 != i2:
                del choice2
                del output2
                print("Please select an item from todays menu only.")
                choice2 = input("What would you like to order? " + i1 + ' or ' + i2 + "\n: ")
                output2 = choice2.casefold()

        if output2 == "no":
            return "OK, bye"
    



greeting()
print(order())
print(afterorder())