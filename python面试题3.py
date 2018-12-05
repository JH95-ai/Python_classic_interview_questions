class parent():
    x=1
class child1(parent):
    pass
class child2(parent):
    pass
print(parent.x,child1.x,child2.x)
child1.x=2
print(parent.x,child1.x,child2.x)
parent.x=3
#如果值在父类中进行了修改,这个改变将会影响那些还没有覆写子类的值,也就是child2
print(parent.x,child1.x,child2.x)
#为什么输出的是323,而不是3,2,1？
#在python中,类变量是以字典的形式进行传递
