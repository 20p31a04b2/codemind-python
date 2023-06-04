s=input()
flag=0
out=' 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'
for d in s:
    if d=='6'and flag==0:
        out=out+'9'
        flag=1
    else:
        out=out+d
print(out)        