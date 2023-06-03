X, Y, Z = map(int, input().split())
S = input()

ans = 0
mode = 'a'
count = 0
mode_list = [mode]
long = []
for s in S:
    if s != mode: 
        long.append(count)
        mode = 'A' if mode == 'a' else 'a'
        mode_list.append(mode)
        count = 1
    else: count += 1
long.append(count)
print(long)
print(mode_list)
for i in range(len(long)):
    l = long[i]
    if mode_list[i] == 'a': ans += min(l*X, Z+Y*l)
    else: ans += min(l*Y, Z+X*l) 
    print(i, ans)

print(ans)