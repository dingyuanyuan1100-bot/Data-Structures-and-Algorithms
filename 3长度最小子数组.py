"""
给定一个含有n 个正整数的数组和一个正整数 target。

找出该数组中满足其总和大于等于target 的长度最小的子数组 [numsl, numsl+1, ·· )
numsr-1,numsr],并返回其长度。如果不存在符合条件的子数组,返回0。

示例1:

输入:target=7, nums =[2,3,1,2,4,3]
输出:2
解释:子数组 [4,3]

示例2:

输入:target =4, nums =[1,4,4]
输出:1

示例3:

输入:target =11, nums=[1,1,1,1,1,1,1,1]
输出:0

是该条件下的长度最小的子数组。
"""
target = 7
nums = [2,3,1,2,4,3]

#暴力解法
def solution1(target,nums)->int:
    lst = []
    for index,num in enumerate(nums):
        for i in range(index+1,len(nums)):
            if num+nums[i] >= target:
                lst.append(i-index+1)


    return 0 if len(lst)==0 else min(lst)

#滑动窗口(快慢指针)
def solution2(target,nums)->int:
    left = 0
    totle = 0
    min_ = float('inf')
    for right in range(len(nums)):
        totle += nums[right]
        while totle >= target:
            min_ = min(min_,right-left+1)
            totle -= nums[left]
            left += 1
    return 0 if min_ == float('inf') else min_





if __name__=='__main__':
    print(solution1(target,nums))
    print(solution2(target,nums))