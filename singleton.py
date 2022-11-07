import time



class Foo(object):
	def __new__(cls, *args, **kwargs):
		# print("__new__ in called")

		instance = super().__new__(cls)
		return instance

#클래스, 인스턴스(사례), 객체(오브잭트)

# obj = Class()
# 'obj'라는 객채는 'Class'라는 클래스의 인스턴스

#클래스는 무조건 설계

#인스턴스는 관계



#cls (클래스 설계)를 토대로 인스턴스 생성


	
	def __init__(self):
		# print("__init__ is called")
		pass
	# pass

s = Foo()
print(s)

class ClassVar():
	foo = 'foo'
	pass

print('ClassVar.foo: ', ClassVar.foo)

ClassVar.foo = 'foo2'
print('ClassVar.foo: ', ClassVar.foo)

cv = ClassVar()
print('cv.foo: ', cv.foo)

print(f'ClassVar.foo: {id(ClassVar.foo)}, cv.foo: {id(cv.foo)}')


class ClassMethod():

	count = 100
	_protectVar = 'protect'

	@classmethod
	def print_count(cls):
		print('print_count: ', cls.count)
		print('print_count _protectVar: ', cls._protectVar)
	pass

ClassMethod.print_count()


class Singleton(object):
	def __new__(cls, *args, **kwargs):

		if hasattr(cls,"_instance"):
			return cls._instance
		
		cls._instance = super().__new__(cls)
		return cls._instance 
		
		pass

	def __init__(self):
		self.figures = []
		pass

	def figure(self):
		fig = time.time()
		self.figures.append(fig)

		return fig

	def getfigures(self):
		return self.figures

s1 = Singleton()
s2 = Singleton()

print('s1: ', s1)
print('s2: ', s2)

s1Figure = s1.figure()
s2Figure = s2.figure()

print('s1 figures: ', s1.getfigures())
print('s2 figures: ', s2.getfigures())
