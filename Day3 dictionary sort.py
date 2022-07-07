import operator

train_dic, train_list = {},[]

train_dic={'thomos':'토마스','hennery':'헨리','james':'james'}

train_list=sorted(train_dic.items(),key=operator.itemgetter(0))

print(train_list)
