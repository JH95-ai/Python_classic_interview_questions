#给定以下字典的子类,下面代码能够运行么？为什么？
class DefaultDict(dict):
    def __missing__(self, key):
        return []
d=DefaultDict()
d['florp']=127

#当key缺失时,执行DefaultDict类,字典的实例将自动实例化这个数列
