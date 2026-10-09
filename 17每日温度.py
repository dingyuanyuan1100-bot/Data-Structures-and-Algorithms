"""
给定一个整数数组 temperatures,表示每天的温度,返回一个数组 answer,其中answer[i] 是指
对于第i天,下一个更高温度出现在几天后。如果气温在这之后都不会升高,请在该位置用0 来代
替。

示例1:
输入:temperatures = [73,74,75,71,69,72,76,73]
输出:[1,1,4,2,1,1,0,0]

示例 2:
输入:temperatures =[30,40,50,60]
输出:[1,1,1,0]

示例3:
输入:temperatures =[30,60,90]
输出:[1,1,0]
"""
temperatures = [73,74,75,71,69,72,76,73]
def solution(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx
        stack.append(i)
    return answer