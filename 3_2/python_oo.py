
class person:

    def __init__(self, food, name):
        self.food = food
        self.name = name

    def eat(self):
        print("我是可爱的人类，我喜欢吃")

class police(person):

    def __init__(self, name, high, food, brave):
        self.brave = brave
        self.high = high
        super().__init__(food, name)

    def eat(self):
        print(f"我是一名警察{self.name}，身高{self.high},喜欢辣辣的食物{self.brave}")
# 需要继承父类
# class lawer(person):
#
#     def __init__(self, knowledge, food, name):
#         self.knowledge = knowledge
# 需要把父类中实例变量加入
#         super().__init__(food, name)
#
#     def eat(self):
#         print(f"我是一名律师{self.name}，我的特长是{self.knowledge}")
  
p1 = person("一切美食","人类")
p1.eat()
p2 = police("小王", "163", "炸鸡", "聪明智慧勇敢😂")
p2.eat()



