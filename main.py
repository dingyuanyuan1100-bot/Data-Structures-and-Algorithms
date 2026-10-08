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



if __name__=='__main__':
    print(solution1())