#!/usr/local/bin/python
'''
this is a program that takes the users age and via the comand line willtell them when they turn 100

'''
def years100(age):
    age = int(sys.argv[1])
    year = 2017
    add_to_year = 100 - age
    year_turn_100 = year +  add_to_year
    print(year_turn_100)


if __name__ == "__main__":
    import sys
    years100(sys.argv[1:])
