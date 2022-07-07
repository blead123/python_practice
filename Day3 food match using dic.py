foods ={
    "떡복이":"오뎅",
    "짜장면":"단무지",
    "피자":"피클",
    "맥주":"땅콩"
}

while(True):
    my_food = input(str(list(foods.keys()))+"중 좋아하는 음식은")

    if my_food in foods:
        print("<%s> 궁합음식은 <%s>입니다" %(my_food, foods.get(my_food)))
    elif my_food == "z" :
        break
    else :
        print("음식이 없읍니다")
