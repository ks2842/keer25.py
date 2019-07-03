ss=input()
tt=list(ss)
tt[::2],tt[1::2]=tt[1::2],tt[::2]
''.join(tt)
print(*tt,sep="")
