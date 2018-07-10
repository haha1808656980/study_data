'''
__slots__
当一个类需要创建大量实例时，可以通过__slots__声明实例所需要的属性，
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
优点：更快的属性访问速度
	 减少内存消耗
'''
#例如

class MyClass(object):
	'''原始方法'''
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()

class MyClass(object):
	'''使用__slots__可以限制可以添加的属性，减少内存消耗'''
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()
