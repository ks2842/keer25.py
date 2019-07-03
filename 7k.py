ss=input()
tt=list(s)
tt[::2],tt[1::2]=tt[1::2],tt[::2]
''.join(tt)
print(*tt,sep="")
