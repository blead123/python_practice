## 4행 5열 리스트를 만들고
## 0에서 3의 배수를 입력하고 출력
list1 = []
list2 = []
val = 0

for i in range(0, 4):
    for k in range(0, 5):
        list1.append(val)
        val = val+3
    list2.append(list1)
    list1 = []

for i in range(0, 4):
    for k in range(0, 5):
        print("%3d" %list2[i][k], end="")
    print("")

