s=input()
d=s.split()
for i in range(len(d)):
    d[i]=d[i][::-1]
print(" ".join(d))    