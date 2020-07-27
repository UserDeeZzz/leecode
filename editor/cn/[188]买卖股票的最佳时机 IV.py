# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。 
# 
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  示例 1: 
# 
#  输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#  
# 
#  示例 2: 
# 
#  输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 
# 。
#  
#  Related Topics 动态规划 
#  👍 255 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        if k > length // 2:
            return self.helper(prices)
        # 0 不持股 1持股
        dp = [[[0, 0] for _ in range(1 + k)] for _ in range(length)]
        for i in range(length):
            # n == 0时代表没交易过 所以全是0
            for n in range(1, k + 1):
                if i == 0:
                    dp[i][n][1] = -prices[i]
                else:
                    dp[i][n][0] = max(dp[i - 1][n][0], dp[i - 1][n][1] + prices[i])
                    dp[i][n][1] = max(dp[i - 1][n][1], dp[i - 1][n - 1][0] - prices[i])
        return dp[length - 1][k][0]

    def helper(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        sell = 0
        min_price = prices[0]
        for i in range(1, length):
            if prices[i] > min_price:
                sell += prices[i] - min_price
            min_price = prices[i]
        return sell

# leetcode submit region end(Prohibit modification and deletion)
