#!/usr/bin/env python3
import math

N, M = map(int, input().split())
A = [list(map(int, input().split())) for l in range(M)]

num = int(N * (N-1) / 2)
s = set()

for m in range(M):
    a = A[m]
    for n in range(N-1): 
       large = max(a[n], a[n+1])
       smalle = min(a[n], a[n+1])
       s.add((smalle, large))

print(num - len(s))
    