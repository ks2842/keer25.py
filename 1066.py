n1,n2=map(int,input().split())
lis=input().split()
ll=[]
for i in lis:
  if int(i)%2!=0:
    ll.append(i)
print(ll[n2-1])
