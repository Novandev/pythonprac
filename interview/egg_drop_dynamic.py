'''
DYNAMIC PROGRAMMING
The egg drop problem states the following:

Given a certain number of eggs and a certain number of floors, what is the least amount of eggs we would
 need to drop to find the pivotal floor where right below it, the egg woulndt break.

 We want to minimixze the amount of eggs we want to break.

So find the wrost amount of eggs you need to drop.


Assume that you have 6 floors and a varibale number of eggs, starting with 1 egg.


Rules:
If you drop and egg and it breaks, you no longer have that egg to use.

Approach 1: Start with one egg from the bottom up

    Step 1: drop from flow zero, and if it doesnt break keep going. Kepp this up until the egg breaks, and the floor below it is the pivotal 'Safe' floor

'''




def eggdrop(num_eggs, num_floors):
    pass