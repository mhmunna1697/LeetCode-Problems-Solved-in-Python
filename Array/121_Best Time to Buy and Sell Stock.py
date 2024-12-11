# def buySellStock(prices):

#     profit = 0
#     for i in range(0, len(prices)-1):
#         for j in range(i+1, len(prices)):
#             if prices[j] > prices[i] and prices[j] - prices[i] > profit:
#                 profit = prices[j] - prices[i]
#     return profit

# prices = [1,2,4]
# print(buySellStock(prices))
# above code runs in O(n^2)

def buySellStock(prices):
    min_price = float('inf')
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        elif i - min_price > max_profit:
            max_profit = i - min_price
    return max_profit

prices = [1,2,4]
print(buySellStock(prices))