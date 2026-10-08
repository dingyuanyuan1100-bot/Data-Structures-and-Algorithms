"""
给你一个整数数组 nums
的个数。

子数组是数组中元素的连续非空序列。

和一个整数k,请你统计并返回 该数组中和为k 的子数组

示例1:

输入:nums=[1,1,1],k=2
输出:2
0 1 2 3
示例2:

输入:nums=[1,2,3], k=3
输出:2
0 1 3 6
"""
nums= [1,2,3,4]
k=3
nums1 = [1,-1,0]
k1 = 0

#前缀和解法
class Solution:
    def solution1(self, nums: list[int], k: int) -> int:
        pre_dic={0:1}
        count = 0
        sum_ = 0
        for num in nums:
            sum_ += num
            if sum_ -k in pre_dic:
                count += pre_dic[sum_ - k]

            pre_dic[sum_] = pre_dic.get(sum_ - k, 0) + 1

        return count

s = Solution()
print(s.solution1(nums, k))
s1 = Solution()
print(s1.solution1(nums1, k1))