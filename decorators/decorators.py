
def new_decorator(func):
    def return_function(*args, **kwargs):
        func(*args, **kwargs)
        print("Functon one ran!")
    return return_function