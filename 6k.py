lp,lk=map(str,input().split())
if(len(lp)!=len(lp)):
  print("no")
c1=[lp.count(i) for i in lp]
c2=[lk.count(i) for i in lk]
if c1==c2:
  print("yes")
else:
  print("no")
