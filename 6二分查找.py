"""
给定一个n 个元素有序的(升序)整型数组 nums 和一个目标值 target,写一个函数
索 nums 中的 target,如果 target 存在返回下标,否则返回-1。

你必须编写一个具有0(log n)时间复杂度的算法。

示例1:

输入:nums=[-1,0,3,5,9,12], target = 9
输出:4
解释:9 出现在 nums 中并且下标为 4

示例2:

输入:nums =[-1,0,3,5,9,12], target = 2
输出 :- 1
解释:2 不存在 nums 中因此返回 -1
"""
nums = [-1,0,3,5,9,12]
target = 9
#二分查找
def solution1(nums,target):
    right = len(nums)-1
    left = 0
    while left <= right: #注意思考为什么是小于等于
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    print(solution1(nums, target))