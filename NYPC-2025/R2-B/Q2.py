"""
0-->k^0(1)
1-->k^1
2-->k^2

k^x * x (x-->max) and +N

it is just a math problem. You can figure out the formula.
"""
def f(N, K, P):
    depth = 0
    val = 0
    remain = N
    power = 1
    if P == 1: return 0
    if K == 1:
        val = N*(N-1) //2 #gauss
        ret = (N+val) % P
        return ret

    def cal(v, t):
        return (v + (depth%P) * (t%P)) % P
    while remain > 0:
        t = int()
        if power <= remain: t = power
        else: t = remain
        val = cal(val, t)
        remain -= t
        depth += 1
        power *= K
        if power > N: power = N
    ret = (val + N%P) % P
    return ret
for _ in range(int(input())):
    n, k, p = map(int, input().split())
    print(f(n, k, p))
