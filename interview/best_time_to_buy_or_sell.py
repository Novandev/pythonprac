'''

Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.


Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


'''

def best_time_to_buy_my_attempt(stocks):

    '''
    This uses a shortened version of the peaks and valley approach n the following manner

    We start off at position 1,and if the current sale price is more than the previous, the profit is the change in prices, which is defined as
    current = previous, this get added to the total profit
    '''
    profit = 0
    i = 0
    for j in range(1,len(stocks)): # we start out at 1 to have access to the previous
        # print(stocks[j], stocks[j-1])
        if stocks[j] > stocks[j-1]: # if the current price is more than the previous buy price, then your profit went up!
            # print(stocks[j-1], stocks[j])
            profit += stocks[j]-stocks[j-1] # add the remainder of these two to the total profit
    print(profit) #print the total profit





best_time_to_buy_my_attempt([7,1,5,3,6,4])


best_time_to_buy_my_attempt([1,2,3,4,5])