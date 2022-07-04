money, c500, c100 , c10 , c50 = 0, 0, 0, 0, 0

money = int(input("얼마를 교환하실래용?"))

c500 = money//500
money %= 500

c100 = money//100
money %= 100

c50 = money//50
money %= 50

c10 = money//10
money &= 10

print("500 -> %d" % c500)
print("100 -> %d" % c100)
print("50 -> %d" % c50)
print("10 -> %d" % c10)
print("나머지-> %d" % money)