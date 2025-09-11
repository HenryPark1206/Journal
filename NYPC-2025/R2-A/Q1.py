"""
Yeah you know, it is just a general algorithmic problem ( I used binary search)
"""
n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
M = 10 ** 20
table = [0] * (n+1)
for x in range(n):
    s = table[x] + a[x]
    table[x+1] = s
res = M
for left in range(0, n - k + 1):
    right = left + k - 1
    middle = (left + right)//2
    y = a[middle]
    l_cnt = middle-left
    l_sum = table[middle]-table[left]
    l_cost = y * l_cnt - l_sum
    r_cnt = right - middle
    r_sum = table[right + 1] - table[middle + 1]
    r_cost = r_sum - y*r_cnt
    tot_cost = l_cost + r_cost
    if tot_cost < res: res = tot_cost
print(res)