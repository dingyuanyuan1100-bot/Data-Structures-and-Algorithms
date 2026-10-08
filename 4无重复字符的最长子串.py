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
    max_len = 0
    n = len(s)
    # i：子串起点
    for i in range(n):
        seen = set()  # 保存当前子串已经出现过的字符
        # j：子串终点，从i向后扩展
        for j in range(i, n):
            if s[j] in seen:
                break  # 出现重复，停止向后扩展
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len


#滑动窗口（快慢指针）写法
def solution2(s):
    left = 0
    max_len = 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

#滑动窗口（跳跃 left）写法
def solution3(s):
    dic = dict()
    left = 0
    max_len = 0
    for right,value in enumerate(s):
        if value in dic and left < dic[value]:      #注意条件
            left = dic[value]+1
        dic[value] = right
        max_len = max(max_len, right - left + 1)
    return max_len



if __name__ == '__main__':
    print(solution1(s))
    print(solution2(s))
    print(solution3(s))
