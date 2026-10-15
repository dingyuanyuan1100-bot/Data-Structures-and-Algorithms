"""
给定两个整数 n和k,返回范围[1,n]中所有可能的k 个数的组哈。
你可以按 任何顺序 返回答案。

示例1:
输入:n=4,k=2
输出:
[
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
[2,4],
]
"""
def combine(n,k):
    res = []

    def backtrack(start,path):
        if len(res) == k:
            res.append(path.copy())
            return

        for i in range(start,n-(k-len(path))+2):
            path.append(i)
            backtrack(i+1,path)
            path.pop()

    backtrack(1,[])
    return res

print(combine(4,2))
