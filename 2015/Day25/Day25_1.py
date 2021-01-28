s=open('input.txt').read()
ans=20151125
col=s[93:97]
row=s[80:84]
row=int(row)
col=int(col)
k=1-row
row+=col-1
while row>0:
    k+=row
    row-=1
while k>1:
    ans=(ans*252533)%33554393
    k-=1
print(ans)
