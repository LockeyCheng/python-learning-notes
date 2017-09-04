# -*- coding: UTF-8 -*-
'''
Created on 2017��9��3��

@author: Lockey
'''
class Person():
    def __init__(self, name,age):
      self.name = name
      self.__age = age
      
    def selfIntro(self):
        print('My name is {}, I am {} years old!\n'.format(self.name,self.__age))   
    def getAge(self):
        return self.__age   
    def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, " has been destroyed!")
    
class Teacher(Person):
    def selfIntro(self):
        print('I am a teacher, my name is {}, I am {} years old!\n'.format(self.name,self.getAge()))
    
person1 = Person('hi',20)
person1.selfIntro()
print(person1.getAge())
teacher1 = Teacher('laoli','18')
teacher1.selfIntro()


'''
print("Person.__doc__:", Person.__doc__)
print("Person.__name__:", Person.__name__)
print("Person.__module__:", Person.__module__)
print("Person.__bases__:", Person.__bases__)
print("Person.__dict__:", Person.__dict__)

print(hasattr(person1, 'age'))   # 如果存在 'age' 属性返回 True。
print(getattr(person1, 'age'))    # 返回 'age' 属性的值
setattr(person1, 'age', 8) # 添加属性 'age' 值为 8
person1.selfIntro()
delattr(person1, 'age')    # 删除属性 'age'
print(hasattr(person1, 'age')) # 如果存在 'age' 属性返回 True。
person1.selfIntro()
'''
