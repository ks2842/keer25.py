n=int(input())
ls=list(map(int,input().split()))
for i in range (len(ls)):
  if(ls[i]>ls[i+1]):
    break
print(i)
