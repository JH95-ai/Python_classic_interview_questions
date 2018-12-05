def extendList(val,list=[]):
    list.append(val)
    return list
list1=extendList(10)
list2=extendList(123,[])
list3=extendList('a')
print("list1=",list1)
print("list2=",list2)
print("list3=",list3)
#1以为每次extendList被调用时,列表参数的默认值都被设置为[],但实际上的情况是,新的
#默认列表只在函数被定义的那一刻创建一次
#2当extendList被没有指定特定参数list调用时,这组list的值随后将被使用,这是因为
#带有默认参数的表达式在函数被定义的时侯被计算,不是在调用的时候被计算.
#3因此list1和list3是在同一个默认列表上进行操作的.而list2是在一个分离的列表
#上进行操作的
