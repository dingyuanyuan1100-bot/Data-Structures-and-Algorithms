"""
给定一个经过编码的字符串,返回它解码后的字符串。
编码规则为:k[encoded_string],表示其中方括号内部的 encoded_string正好重复k次。注意k
保证为正整数。
你可以认为输入字符串总是有效的;输入字符串中没有额外的空格,且输入的方括号总是符合格式要
求的。
此外,你可以认为原始数据不包含数字,所有的数字只表示重复的次数k,例如不会出现
像3a 或2[4]的输入。
测试用例保证输出的长度不会超过 105。

示例1:
输入:s ="3[a]2[bc]"
输出:"aaabcbc"
"""

#只能浅层嵌套
def solution(s):
    stock = []
    num = 0
    result = ""
    for index,vur in enumerate(s):
        if vur == "[":
            stock.append(num)
            num = 0
            stock.append(index)
        elif vur == "]":
            left = stock.pop()
            num = stock.pop()
            result += s[left+1:index]*num
            num = 0
        elif vur.isdigit():
            num = num*10+int(vur)

    return result


#深层嵌套
def solution1(s):
    stack = []
    res = ""
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            stack.append((res, num))
            res = ""
            num = 0
        elif c == ']':
            prev_str, k = stack.pop()
            res = prev_str + res * k
        else:
            res += c
    return res

def solution2(s):
    char = ""
    stock = []
    num = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        if c == "[":
            stock.append((char, num))
        if c == "]":
            prev_str, k = stock.pop()
            char = prev_str * k+char
            num = 0
        char = char + c
    return char

print(solution(s))
print(solution1(s1))