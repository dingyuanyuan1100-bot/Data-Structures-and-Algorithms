"""
这里有n 个航班,它们分别从1到n 进行编号。

有一份航班预订表 bookings,表中第i 条预订记录 bookings[i]=[firsti, lasti,seatsi
意味着在从firsti到lasti
个座位。

请你返回一个长度为n的数组 answer,

(包含 firsti和 lasti)的每个航班 上预订了

seatsi

里面的元素是每个航班预定的座位总数。

示例1:

输入:bookings=[[1,2,10],[2,3,20],[2,5,25]], n=5
输出:[10,55,45,25,25]
解释:
航班编号
预订记录 1:
预订记录 2:
预订记录 3:
总座位数:
因此,answer=[10,55,45,25,25]

[]
"""
bookings=[[1,2,10],[2,3,20],[2,5,25]]
n=5

#暴力解法
def solution(n,bookings):
    con = len(bookings)
    answer = []
    for i in range(n):
        count = 0
        for j in range(con):
            if bookings[j][1] >= i+1 >= bookings[j][0]:
                count += bookings[j][2]
        answer.append(count)
    return answer

#插数法
def solution2(n,bookings)->list:
    con = [0]*(n+1)
    for left,right,seats in bookings:
        con[left-1]+=seats
        con[right]-=seats

    answer = [0]*n
    answer[0] = con[0]
    for i in range(1,n):
        answer[i]= answer[i-1]+con[i]
    return answer

#插数法(优化)
def solution3(n,bookings)->list:
    con = [0]*(n+1)
    for left,right,seats in bookings:
        con[left-1] += seats
        con[right] -= seats
    answer = []
    cur = 0
    for i in con[:n]:
        cur += i
        answer.append(cur)
    return answer


print(solution(n, bookings))
print(solution2(n, bookings))
print(solution3(n, bookings))
