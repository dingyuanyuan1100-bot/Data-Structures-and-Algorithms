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
    con =len(nums)
    left = 0
    right = len(nums)-1
    mid = (right+left)//2
    while left < right:
        if nums[mid]> target:
            right = mid-1
        elif nums[mid]< target:
            left = mid+1
        else:
            return mid
        mid = (left+right)//2
    return -1
if __name__ == '__main__':
    print(solution1(nums, target))
2
