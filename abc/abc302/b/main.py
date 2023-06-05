H, W = map(int, input().split())
S = [input() for _ in range(H)]
# S = [[S[i][j] for j in range(W)] for i in range(H)]
R = [0]*5
C = [0]*5
for i in range(H) :
  for j in range(W) :
        if i+4 < H : 
          s = S[i][j] + S[i+1][j] + S[i+2][j] + S[i+3][j] + S[i+4][j]
          if s == 'snuke': 
              R = [i+1, i+2, i+3, i+4, i+5]
              C = [j+1, j+1, j+1, j+1, j+1]
              break
        if 0 <= i-4 : 
          s = S[i][j] + S[i-1][j] + S[i-2][j] + S[i-3][j] + S[i-4][j]
          if s == 'snuke': 
              R = [i+1, i, i-1, i-2, i-3]
              C = [j+1, j+1, j+1, j+1, j+1]
              break
        if j+4 < W : 
          s = S[i][j] + S[i][j+1] + S[i][j+2] + S[i][j+3] + S[i][j+4]
          if s == 'snuke': 
              R = [i+1, i+1, i+1, i+1, i+1]
              C = [j+1, j+2, j+3, j+4, j+5]
              break
        if 0 <= j-4 : 
          s = S[i][j] + S[i][j-1] + S[i][j-2] + S[i][j-3] + S[i][j-4]
          if s == 'snuke': 
              R = [i+1, i+1, i+1, i+1, i+1]
              C = [j+1, j, j-1, j-2, j-3]
              break
        if i+4 < H and j+4 < W : 
          s = S[i][j] + S[i+1][j+1] + S[i+2][j+2] + S[i+3][j+3] + S[i+4][j+4]
          if s == 'snuke': 
              R = [i+1, i+2, i+3, i+4, i+5]
              C = [j+1, j+2, j+3, j+4, j+5]
              break
        if 0 <= i-4 and 0 <= j-4 : 
          s = S[i][j] + S[i-1][j-1] + S[i-2][j-2] + S[i-3][j-3] + S[i-4][j-4]
          if s == 'snuke': 
              R = [i+1, i, i-1, i-2, i-3]
              C = [j+1, j, j-1, j-2, j-3]
              break
        if i+4 < H and 0 <= j-4 : 
          s = S[i][j] + S[i+1][j-1] + S[i+2][j-2] + S[i+3][j-3] + S[i+4][j-4]
          if s == 'snuke': 
              R = [i+1, i+2, i+3, i+4, i+5]
              C = [j+1, j, j-1, j-2, j-3]
              break
        if 0 <= i-4 and j+4 < W : 
          s = S[i][j] + S[i-1][j+1] + S[i-2][j+2] + S[i-3][j+3] + S[i-4][j+4]
          if s == 'snuke': 
              R = [i+1, i, i-1, i-2, i-3]
              C = [j+1, j+2, j+3, j+4, j+5]
              break

for i in range(5) : print(f'{R[i]} {C[i]}')