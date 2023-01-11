m,n=map(int,input().split())
M=[]
s=0
for i in range(m):
  row=list(map(int,input().split()))
  M.append(row)
for i in range(m):
  for j in range(n):
     s=s+M[i][j]
print(s)