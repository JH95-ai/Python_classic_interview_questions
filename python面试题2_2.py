#用python生成器解决
def multipliers():
    for i in range(4):
        yield lambda x:i*x
#一个带有yield的函数就是一个generator,它和普通函数不同,
#生成一个generator看起来像函数调用,但不会执行任何函数代码
#直到对其调用next()(在for循环中会自动调用next())才开始执行.
#虽然执行流程仍按函数的流程执行,但每执行到一个yield语句就会中断,
#并返回一个迭代值,下次执行时间从yield的下一个语句继续执行.
#看起来就像一个函数在正常执行的过程中被yield中断了数次,每次中断都会
#通过yield返回当前的迭代值
for m in multipliers():
    print(m(2))