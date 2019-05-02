import random
def passwordGen():
    let_and_num =[1,2,3,4,5,6,7,8,9,0,"!","@","#","$","%","^","*","(",")"]
    password=random.sample(let_and_num,8)
    password = "".join(str(i) for i in password)
    print(password)


passwordGen()
