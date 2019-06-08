n, m, k = map(int, input().split())
vec = []
ans = 0
for i in range(0, n):
    zero = 0
    for j in range(0, m):
        v = int(input())
        zero += (v == 0)
    if zero > 0:
        vec.append(zero)
    else:
        ans += 1
vec.sort()
for it in vec:
    k -= it
    if k >= 0:
        ans += 1
print(ans)
