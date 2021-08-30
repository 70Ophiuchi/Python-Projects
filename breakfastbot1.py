# # # import time

# # # choice = input("Please place your order. Would you like waffles or pancakes?\n").lower()

# # # while True:
# # #     if choice == "waffles":
# # #         print("Waffles it is!")
# # #         break
# # #     elif choice == "pancakes":
# # #         print("Pancakes it is!")
# # #         break
# # #     else:
# # #         print("Sorry, that's not on our menu.")
# # #         del choice
# # #         choice = input("Please place your order. Would you like waffles or pancakes?\n").lower()


# # # # while True:
# # # #     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
# # # #     if response == "waffles":
# # # #         print("Waffles it is!")
# # # #         break
# # # #     elif response == "pancakes":
# # # #         print("Pancakes it is!")
# # # #         break
# # # #     else:
# # # #         print("Sorry, I don't understand.")

# # # # response = ""
# # # # while response != "waffles" and response != "pancakes":
# # # #     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
# # # #     if response == "waffles":
# # # #         print("Waffles it is!")
# # # #     elif response == "pancakes":
# # # #         print("Pancakes it is!")
# # # #     else:
# # # #         print("Sorry, I don't understand.")


# # # # flexible input

# # # while True:
# # #     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
# # #     if "waffles" in response:
# # #         print("Waffles it is!")
# # #         break
# # #     elif "pancakes" in response:
# # #         print("Pancakes it is!")
# # #         break
# # #     else:
# # #         print("Sorry, that's not on our menu.")


# # import time

# # print("Hello! I am Bob, the Breakfast Bot.")
# # time.sleep(2)
# # print("Today we have two breakfasts available.")
# # time.sleep(2)
# # print("The first is waffles with strawberries and whipped cream.")
# # time.sleep(2)
# # print("The second is sweet potato pancakes with butter and syrup.")
# # time.sleep(2)

# # while True:
# #     response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
# #     if "waffles" in response:
# #         print("Waffles it is!")
# #         time.sleep(2)
# #         break
# #     elif "pancakes" in response:
# #         print("Pancakes it is!")
# #         time.sleep(2)
# #         break
# #     else:
# #         print("Sorry, I don't understand.")
# #         time.sleep(2)
# # print("Your order will be ready shortly.")
# # time.sleep(2)

# # del response
# # while True:
# #     response2 = input("Would you like to order again? ").lower()
# #     if "yes" in response2:
# #         while True:
# #             response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
# #             if "waffles" in response:
# #                 print("Waffles it is!")
# #                 time.sleep(2)
# #                 print("Your order will be ready shortly")
# #                 time.sleep(2)
# #                 break
# #             elif "pancakes" in response:
# #                 print("Pancakes it is!")
# #                 time.sleep(2)
# #                 print("Your order will be ready shortly")
# #                 time.sleep(2)
# #                 break
# #             else:
# #                 print("Sorry, I don't understand.")
# #                 time.sleep(2)
# #     if "no" in response2:
# #         print("OK, Bye.")
# #         break
# #     else:
# #         print("Please reply with 'yes' or 'no'")


# import time

# def print_pause(phrase):
#     print(phrase)
#     time.sleep(2)

# print_pause("Hello! I am Bob, the Breakfast Bot.")
# print_pause("Today we have two breakfasts available.")
# print_pause("The first is waffles with strawberries and whipped cream.")
# print_pause("The second is sweet potato pancakes with butter and syrup.")

# while True:
#     while True:
#         response = input("Please place your order. "
#                          "Would you like waffles or pancakes?\n").lower()
#         if "waffles" in response:
#             print_pause("Waffles it is!")
#             break
#         elif "pancakes" in response:
#             print_pause("Pancakes it is!")
#             break
#         else:
#             print_pause("Sorry, I don't understand.")
#     print_pause("Your order will be ready shortly.")
#     while True:
#         order_again = input("Would you like to place another order? "
#                             "Please say 'yes' or 'no'.\n").lower()
#         if "no" in order_again:
#             print_pause("OK, goodbye!")
#             break
#         elif "yes" in order_again:
#             print_pause("Very good, I'm happy to take another order.")
#             break
#         else:
#             print_pause("Sorry, I don't understand.")
#     if "no" in order_again:
#         break
# import time

# def print_pause(message_to_print):
#     print(message_to_print)
#     time.sleep(2)
    
# def valid_input(prompt, options):
#     while True:
#         response = input(prompt).lower()
#         for n in options:
#             if n in response:
#                 return n + "!"
#         else:
#             print_pause("sorry I dont understand")

# def intro():
#     print_pause("Hello! I am Bob, the Breakfast Bot.")
#     print_pause("Today we have two breakfasts available.")
#     print_pause("The first is waffles with strawberries and whipped cream.")
#     print_pause("The second is sweet potato pancakes with butter and syrup.")

# def get_order():
#     while True:
#         print(valid_input("what would you like to order?\n", ["macaroni", "crepes", "pancakes", "oil"]))
#         print_pause("Your order will be ready shortly.")
#         while True:
#             order_again = input("Would you like to place another order? "
#                                 "Please say 'yes' or 'no'.\n").lower()
#             if "no" in order_again:
#                 print_pause("OK, goodbye!")
#                 break
#             elif "yes" in order_again:
#                 print_pause("Very good, I'm happy to take another order.")
#                 break
#             else:
#                 print_pause("Sorry, I don't understand.")
#         if "no" in order_again:
#             break

# import time


# def print_pause(message_to_print):
#     print(message_to_print)
#     time.sleep(2)


# def valid_input(prompt, option1, option2):
#     while True:
#         response = input(prompt).lower()
#         if option1 in response:
#             break
#         elif option2 in response:
#             break
#         else:
#             print_pause("Sorry, I don't understand.")
#     return response

# def intro():
#     print_pause("Hello! I am Bob, the Breakfast Bot.")
#     print_pause("Today we have two breakfasts available.")
#     print_pause("The first is waffles with strawberries and whipped cream.")
#     print_pause("The second is sweet potato pancakes with butter and syrup.")

# def get_order():
#     response = valid_input("Please place your order. "
#                            "Would you like waffles or pancakes?\n",
#                            "waffles", "pancakes")
#     if "waffles" in response:
#         print_pause("Waffles it is!")
#     elif "pancakes" in response:
#         print_pause("Pancakes it is!")

# intro()

# while True:

#     get_order()
#     print_pause("Your order will be ready shortly.")
#     order_again = valid_input("Would you like to place another order? "
#                               "Please say 'yes' or 'no'.\n",
#                               "yes", "no")
#     if "no" in order_again:
#         print_pause("OK, goodbye!")
#         break
#     elif "yes" in order_again:
#         print_pause("Very good, I'm happy to take another order.")

import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def get_order():
    response = valid_input("Please place your order. "
                           "Would you like waffles or pancakes?\n",
                           "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")
    order_again()

def order_again():
    response = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()

def order_breakfast():
    intro()
    get_order()

order_breakfast()

