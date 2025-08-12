# 121 Best Time to Buy and Sell Stock
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
def maxProfit(prices):
    i = 0
    j = 1
    max = 0
    if len(prices) == 1:
        return 0
    while j <= len(prices) - 1:
        if prices[j] >= prices[i]:
            if prices[j] - prices[i] > max:
                max = prices[j] - prices[i]
            j += 1
        elif prices[j] < prices[i]:
            i = j
            j = i + 1
    return max
'''
def maxProfit(prices):
    # define a empty list to store the profit of each transaction
    dict = {'buy': [float('inf'), float('inf')],
            'sell': [0, 0]}
    if len(prices) == 1:
        return 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            if prices[i] <= dict['buy'][1] and i <= dict['buy'][0]:
                dict['buy'][0] = i
                dict['buy'][1] = prices[i]
            if prices[i + 1] >= dict['sell'][1] and i >= dict['sell'][0]:
                dict['sell'][0] = i + 1
                dict['sell'][1] = prices[i + 1]
    if dict['sell'][1] > dict['buy'][1]:
        return dict['sell'][1] - dict['buy'][1]
    else:
        return 0
'''
prices = [2, 1, 2, 0, 1, 2]
print(maxProfit(prices))