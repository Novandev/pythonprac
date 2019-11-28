def yell(text):
    return f'{text.upper()}!'
    
bark = yell

del yell # this wil delete yell and the pointers for it


if __name__=="__main__":
    print(yell('hello'))
    print(bark("yell"))
    
    print(bark("puppy"))
