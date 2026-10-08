"""
题目：给定正整数 `n`，生成一个包含 `1 ~ n²` 所有元素，顺时针螺旋排列的 `n×n` 正方形矩阵
"""

#我的解法（每条边不填充终点角落，把角落交给下一条边处理，避免重复赋值）
def solution1(n):
    mat = [[0] * n for _ in range(n)]
    left = 0
    right = n-1
    count = 1
    while left < right:
        for i in range(left,right):
            mat[left][i] = count
            count += 1
        for i in range(left,right):
            mat[i][right] = count
            count += 1
        for i in range(right,left,-1):
            mat[right][i] = count
            count += 1
        for i in range(right,left,-1):
            mat[i][left] = count
            count += 1
        left += 1
        right -= 1
    if left == right:
        mat[left][right] = count
    return mat

#方向数组法(重点看)
def solution2(n):
    mat = [[0] * n for _ in range(n)]
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]   # 右→下→左→上
    r = c = d = 0
    for num in range(1, n*n + 1):
        mat[r][c] = num
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < n and 0 <= nc < n and mat[nr][nc] == 0):
            d = (d + 1) % 4                 # 越界或撞到已填数 → 右转
            nr, nc = r + dr[d], c + dc[d]
        r, c = nr, nc
    return mat



if __name__=='__main__':
    print(solution1(4))
    print(solution2(4))