aa=[]
bb=[]
val = 0

for i in range (0,100):
    aa.append(val)
    val=val+2
for i in range (0,100):
    bb.append(aa[99-i])

print("aa=" , aa)
print("bb=" , bb)