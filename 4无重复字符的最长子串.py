"""
给定一个字符串s,请你找出其中不含有重复字符的最长子串 的长度。

示例1:

输入:s="abcabcbb"
输出:3
解释:因为无重复字符的最长子串是“abc”,所以其长度为 3。注意"bca”和
“cab”也是正确答案。

示例2:

输入:s="bbbbb"
输出:1
解释:因为无重复字符的最长子串是“b",所以其长度为 1。

示例3:

输入:s="pwwkew"
输出:3
解释:因为无重复字符的最长子串是“wke",所以其长度为 3。

"""
s = "abba"
#暴力解法
def solution1(s):
    a=[]
    max_=0
    for i in s:
        while i in a:
            del a[0]
        if i not in a:
            a.append(i)
            max_ = max(max_,len(a))
    return max_

#滑动窗口（快慢指针）写法
def solution2(s):
    a=set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in a:
            a.remove(s[left])
            left += 1
        a.add(s[right])
        max_len = max(max_len, len(a))
    return max_len

#滑动窗口（跳跃 left）写法
def solution3(s):
    char_index = dict()
    max_len = 0
    left = 0
    for right, c in enumerate(s):
        if c in char_index and char_index[c] >= left:
            left = char_index[c] + 1
        char_index[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == '__main__':
    print(solution1(s))
    print(solution2(s))
    print(solution3(s))