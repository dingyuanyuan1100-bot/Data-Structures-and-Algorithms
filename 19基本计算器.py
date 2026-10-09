"""
给你一个字符串表达式s,请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
你可以假设给定的表达式总是有效的。所有中间结果将在[-231,231-1]的范围内。
注意:不允许使用任何将字符串作为数学表达式计算的内置函数,比如eval()

示例1:
输入:s="3+2*2"
输出:7

3 2 2
+ +
示例2:
输入:s="3/2"
输出:1
"""


def computer(s):
    num = 0
    number = []
    pre_op = "+"
    for idx, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        if char in "+-*/" or idx == len(s) - 1:
            if pre_op == "+":
                number.append(num)
            elif pre_op == "-":
                number.append(-num)
            elif pre_op == "*":
                number[-1] = number[-1] * num
            elif pre_op == "/":
                number[-1] = int(number[-1] / num)
            pre_op = char
            num = 0
    return sum(number)


print(computer("3+2*2"))