"""
给你一个未排序的整数数组nums,请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 0(n)并且只使用常数级别额外空间的解决方案。
示例1:
输入:nums=[1,2,0]
输出:3
解释:范围 [1,2]中的数字都在数组中。

示例2:

输入:nums=[3,4,-1,1]
输出:2
解释:1 在数组中,但 2 没有。

示例3:

输入:nums=[7,8,9,11,12]
输出:1
解释:最小的正数 1 没有出现。

"""
nums=[7,8,9,11,12]
#暴力解法
def solution(nums:list[int])->int:
    cur = 1
    while True:
        if cur in nums:
            cur += 1
        else:
            return cur

#期望归位解法
def solution2(nums:list[int])->int:
    n = len(nums)
    for i in range(n):
        if 0<nums[i]<=n:
            nums[i-1]=i

    for index,i in enumerate(nums):
        if index+1!=i:
            return index+1



print(solution(nums))
print(solution2(nums))