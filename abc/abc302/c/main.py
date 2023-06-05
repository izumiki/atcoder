import itertools

N, M = map(int, input().split())
S = [str(input()) for _ in range(N)]
T = permutations = list(itertools.permutations(S))

for t in T :
    S = t
    flag = True
    for i in range(N-1) :
        count = 0
        for j in range(M) :
            if t[i][j] != S[i+1][j] : count += 1
        if count != 1 : 
            flag = False
    if flag == True : break
        
print('Yes') if flag == True else print('No')            
    