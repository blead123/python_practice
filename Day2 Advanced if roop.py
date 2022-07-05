select, answer = 0 ,0
numString = ""
num1, num2 =0 ,0

select = int(input("1.cal, 2 sum"))
if select==1:
    numString = input("input formula")
    answer = eval(numString)
    print("answer= %f" % answer)

elif select == 2:
    num1 = int(input("first number"))
    num2 = int(input("second number"))
    for i in range (num1, num2) : ## num1 부터 num2 의 값 계산
        answer = answer + i
    print ("answer=%d" % answer)

else:
    print("press 1 or 2")