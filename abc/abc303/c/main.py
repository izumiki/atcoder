N, M, H, K = map(int, input().split())
S = input()
x = [0]*M
y = [0]*M
items = dict()
for i in range(M):
    x[i], y[i] = map(int, input().split())
    items[(x[i], y[i])] = True

# print(N, M, H, K)
# print(x, y)
now = [0, 0]
for i in range(N):
    if S[i] == 'R': now[0] += 1 
    elif S[i] == 'L': now[0] -= 1 
    elif S[i] == 'U': now[1] += 1 
    elif S[i] == 'D': now[1] -= 1 
    H -= 1
    # print(now)
    if (H < 0): break
    item = tuple(now)
    if item in items and H < K: 
        H = K
        del(items[item])
print('Yes') if H >= 0 else print('No')