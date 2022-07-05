myList=[30,10,20]
print(myList)

myList.append(40)
print(myList)

myList.pop(
)
print(myList)

myList.sort()
print(myList)

myList.reverse()
print(myList)

print("20 index pos =", myList.index(20))

myList.insert(2, 222)
print("insert(2,222)->",myList)

myList.remove(222)
print("remove 222->", myList)

myList.extend([77,88,99])
print("Extended->", myList)

## 원본 데이터 유지시 sorted 사용
newList = myList
newList=sorted(myList)
print("mylist->", myList)
print("sorted new list->",newList)