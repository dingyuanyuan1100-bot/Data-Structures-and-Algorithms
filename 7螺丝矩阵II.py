"""
题目：给定正整数 `n`，生成一个包含 `1 ~ n²` 所有元素，顺时针螺旋排列的 `n×n` 正方形矩阵
"""
from itertools import count

n=3
def solution1(n):
    mat = [[0]*n for _ in range(n)]
    count = 1
    #初始化位置
    start_index = 0
    while True:
        for i in range(start_index,n-start_index-1):
            mat[0][i] = count
            count+=1
        for i in range(start_index,n-1-start_index):
            mat[i][n-1] = count
            count+=1
        for i in range(n-1-start_index,0,-1):
            mat[n-1][i] = count
            count+=1
        for i in range(n-1,0,-1):
            mat[i][0] = count
            count+=1

        start_index+=1
if __name__=='__main__':
    print(solution1(n))