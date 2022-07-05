aa= []
for i in range(0,4):
    aa.append(0)
sum = 0

for i in range(0,4):
    aa[i] = int(input(str(i+1)+"번째 값:"))
for i in aa:
    sum=sum+i
print("sum=%d" %sum)

