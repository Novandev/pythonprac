import random
'''
Simple game of rOck paper scissors
'''
again = ""
while again != "n":
    user_choice=input("Pick a choice: /n for rock press 1 /n for paper press 2 for scissors press 3")
    if int(user_choice[0]) > random.randint(0, 3):
        print("you won!!")
    else:
        print ("nope, you lost!")

    again=input("would you like to play again?")
