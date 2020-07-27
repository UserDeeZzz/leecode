# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ] 
#  Related Topics 数组 回溯算法 
#  👍 278 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0, [])
        return self.res

    def backtrack(self, nums, index, curr):
        self.res.append(curr)
        for i in range(index, len(nums)):
            # 选择
            if i > index and nums[i] == nums[i-1]:
                continue
            self.backtrack(nums, i + 1, curr + [nums[i]])

# leetcode submit region end(Prohibit modification and deletion)
