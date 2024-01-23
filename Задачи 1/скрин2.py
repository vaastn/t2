a=10
b=500
c=[]
v=[]
for i in range(b+1):
    if i>=a:
        c.append(i)
for i in c:
    for j in range(2, i):
        if(i%j==0):
            break;
        if(j==i-1):
            v.append(i)
print(v)
s=sum(v) 
print(s)