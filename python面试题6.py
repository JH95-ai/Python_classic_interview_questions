list=[[]]*5
#第一行不是创造了一个包含五个独立列表的列表,而是它是一个创建
#了包含对同一个列表五次引用的列表
print(list)
list[0].append(10)
#将10附加在第一个列表上,但由于所有5个列表是引用的同一个列表
#所以每个列表都被加了10
print(list)
list[1].append(20)
print(list)
list.append(30)
#是将整个新的元素附加在外列表上
print(list)



#