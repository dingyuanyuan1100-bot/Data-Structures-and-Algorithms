"""
给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列。

请你从数组中找出满足相加之和等于目标数 target 的 两个 数。令这两个数分别是 numbers[index1] 和 numbers[index2] ，其中 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

你所设计的解决方案必须只使用常数级的额外空间。


示例 1：

输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
示例 2：

输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
示例 3：

输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

"""
numbers1 = [2,7,11,15]
target1 = 9

#暴力解法
def solution1(numbers1,target1):
    for index,k in enumerate(numbers1):
        need = target1 - k
        for i in range(index+1,len(numbers1)):
            if numbers1[i] == need:
                return [index+1,i+1]
    return []

#哈希解法
def solution2(numbers1,target1):
    dit={}
    for index,k in enumerate(numbers1):
        need = target1 - k
        if need not in dit:
            dit[k]=index
        else:
            return [dit[need]+1,index+1]
    return []

#双指针（首尾）写法
def solution3(numbers1,target1):
    left=0
    right=len(numbers1)-1
    while left<right:
        if numbers1[left]+numbers1[right]>target1:  # right-=1 if numbers1[left]+numbers1[right]>target1
            right-=1
        elif numbers1[left]+numbers1[right]<target1:  # left+=1  if numbers1[left]+numbers1[right]<target1:
            left+=1
        else:
            return [left+1,right+1]
    return []

#双指针（快慢针）写法
def solution4(numbers1,target1):
    left=0
    right=1
    while left<right:
        if numbers1[left]+numbers1[right]<target1:
            right+=1
        elif numbers1[left]+numbers1[right]<target1:
            left+=1
        else:
            return [left+1,right+1]
    return []



if __name__ == '__main__':
    print(solution1(numbers1,target1))
    print(solution2(numbers1,target1))
    print(solution3(numbers1,target1))
    print(solution4(numbers1,target1))