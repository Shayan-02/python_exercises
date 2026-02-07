# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# 5.8.2022
# 121. Best Time to Buy and Sell Stock
# Hard
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.


# @param {Integer[]} prices
# @return {Integer}
class Solution:
    def __init__(self, prices):
        self.prices = prices
        self.n = len(prices)

    def maxProfit(self):
        if not self.prices or self.n < 2:
            return 0

        # Initialize the dp arrays
        dp1 = [
            0
        ] * self.n  # dp1[i] is the max profit you can make from 0 to i with one transaction
        dp2 = [
            0
        ] * self.n  # dp2[i] is the max profit you can make from i to n-1 with one transaction

        # Calculate dp1: max profit for one transaction from start to i
        self.calculate_dp1(dp1)

        # Calculate dp2: max profit for one transaction from i to end
        self.calculate_dp2(dp2)

        # Calculate the maximum profit by combining dp1 and dp2
        return self.calculate_max_profit(dp1, dp2)

    def calculate_dp1(self, dp1):
        min_price = self.prices[0]
        for i in range(1, self.n):
            min_price = min(min_price, self.prices[i])
            dp1[i] = max(dp1[i - 1], self.prices[i] - min_price)

    def calculate_dp2(self, dp2):
        max_price = self.prices[-1]
        for i in range(self.n - 2, -1, -1):
            max_price = max(max_price, self.prices[i])
            dp2[i] = max(dp2[i + 1], max_price - self.prices[i])

    def calculate_max_profit(self, dp1, dp2):
        max_profit = 0
        for i in range(self.n):
            max_profit = max(max_profit, dp1[i] + dp2[i])
        return max_profit

n = int(input("enter a number: "))
print("yes" if n == n[::-1] else "no")