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

#暴力哈希解法
def solution1(target,nums):
    dit = {}
    for index,num in enumerate(nums):
        for i in range(index+1,len(nums)):
            if num+nums[i]>=target:
                dit[i-index]=[num,nums[i]]
    if  dit == {}:
        return 0
    min_=min(dit.keys())+1
    return min_

#滑动窗口(快慢指针)
def solution2(target, nums):
    slow = 0
    fast = 0
    total = 0
    res = float('inf')
    while fast < len(nums):
        total+=nums[fast]
        while total>=target:
            res=min(res,fast-slow+1)
            total-=nums[slow]
            slow+=1
        fast+=1
    return 0 if res == float('inf') else res



if __name__=='__main__':
    print(solution1(target,nums))
    print(solution2(target,nums))