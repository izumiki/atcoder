N = int(input())
S = input()
T = input()

ans = 'Yes'
for i in range(N):
    s = S[i]
    t = T[i]
    if(s != t):
        if(s == '1' and t == 'l'): continue
        elif(s == 'l' and t == '1'): continue
        elif(s == 'o' and t == '0'): continue
        elif(s == '0' and t == 'o'): continue
        else: ans = 'No'
print(ans)