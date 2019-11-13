"""
This is a short program that uses decorators yeah

"""
from decorators import new_decorator


@new_decorator
def print_me(name):
    print('I am {}'.format(name))



if __name__=="__main__":
    print(print_me("Novan Adams"))