'''
this checks for a pallindrome
'''

def pallindrome(word):
    word = str(sys.argv[1])
    if word == word[::-1]:
        print("Issa pallendrome")
    else:
        print("it isnt one")



if __name__== "__main__":
    import sys
pallindrome(sys.argv[1:])
