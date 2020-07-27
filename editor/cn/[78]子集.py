# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法 
#  👍 674 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums):
        # 结果集
        self.res = []
        self.backtrack(nums, 0, [])
        return self.res

    def backtrack(self, nums, index, curr):
        # 从index处开始选择 选择集是nums 上一步的缓存是curr
        # 将上一步缓存结果加入结果集
        self.res.append(curr)
        for i in range(index, len(nums)):
            # 选择index
            self.backtrack(nums, i + 1, curr + [nums[i]])
            # 不选择index那么继续执行循环

# leetcode submit region end(Prohibit modification and deletion)
