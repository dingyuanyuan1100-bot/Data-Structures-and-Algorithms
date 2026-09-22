"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

"""
nums1 = [2,7,11,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

#1.暴力解法
def solution1(nums1,target1):
    for index, num in enumerate(nums1):
        con = target1-num
        for j in range(index+1,len(nums1)):
            if con ==nums1[j]:
                return [index,j]
    return []

#2.哈希表解法
def solution2(nums1,target1):
    dit={}
    for index,num in enumerate(nums1):
        need = target1-num
        if need not in dit:
            dit[num]=index
        else:
            return [dit[need],index]
    return []



if __name__ == '__main__':
    print(solution2(nums1, target1))