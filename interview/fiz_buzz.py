'''
Fizz-buzz


On mulitples of 3 print fizz
On mulpltes of 5 print buzz,

On multuples of both print fizz buzz

'''


def fizz_buzz(n):
    if n == 0: return
    for i in range(1,n+1):
        # print(i)
        if i % 3 ==0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 ==0:
            print('fizz')
        


fizz_buzz(15)