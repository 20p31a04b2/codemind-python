m,n=map(int,input().split())
M=[]
for i in range(m):
    row=list(map(int,input().split()))
    M.append(row)
es=0
os=0
for i in range(m):
    for j in range(n):
        if M[i][j]%2==0:
            es=es+M[i][j]
        else:
            os=os+M[i][j]
print(es,os)  