import random

numbers = []
for num in range(0, 10):
    numbers.append(random.randrange(0, 10))
print("List = ", numbers)

for num in range(0, 10):
    if num not in numbers:
        print("number %d is not available" %num)

