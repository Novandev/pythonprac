import random
'''
integer guessing game
'''
answer = ""
while answer!= "exit":
    answer=input("Guess the magic number!")
    guess =random.randint(0, 9)

    if int(answer) > guess:
        print(" Too high!")
    elif int(answer) ==guess:
        print("bingo")
    else:
        print("too low")
