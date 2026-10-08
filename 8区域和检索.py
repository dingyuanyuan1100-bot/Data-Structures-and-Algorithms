"""
给定一个整数数组 nums,处理以下类型的多个查询:

1. 计算索引 left 和 right(包含 left 和 right)之间的 nums 元素的和,其
中 left <= right

实现 NumArray 类:

·NumArray(int[] nums)使用数组 nums 初始化对象

● int sumRange(int left, int right)返回数组 nums 中索引 left和 right 之间的
元素的 总和,包含left和right 两点(也就是 nums[left]+nums[left+1] +
... + nums [right] )

示例1:

输入:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出:
[null, 1, -1, -3]

"""
#前缀和解法
class NumArray:
    def __init__(self, nums):
        self.profits = [0] * len(nums+1)
        for i in range(len(nums)):
            self.profits[i+1] = self.profits[i]+nums[i]

    def sumRange(self, left, right):
        return self.profits[right+1] - self.profits[left]
