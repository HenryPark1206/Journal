"""
At first it looked like a hard one, but it could be solved simply by union find,
"""
n = int(input())
robots = []
for _ in range(n):
    k, d = map(int, input().split())
    robots.append(tuple([k,d]))
robots.sort(key = lambda x:x[1], reverse=True)
di = dict()
def f(x):
    y = x
    path = []
    ret = int()
    while y in di and y >= 0:
        path.append(y)
        y = di[y]
    ret = y
    for val in path: di[val] = ret
    return ret
res = 0
for k, d in robots:
    val = f(k)
    if val >= 0:
        res += d
        di[val] = val-1
print(res)