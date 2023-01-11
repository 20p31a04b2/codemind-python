r,c=map(int,input().split())
mat=[]
for i in range(r):
    row=list(map(int,input().split()))
    mat.append(row)
ers=0
ors=0
for i in range(r):
  if i%2==0:
    ers+=sum(mat[i])
  else:
    ors+=sum(mat[i])
print(ers,ors)        