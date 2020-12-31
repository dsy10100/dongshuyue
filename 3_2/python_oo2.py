'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''


class Tonglao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if name == "WYZ" or name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我砍了你")
        else:
            print("呸 你是谁")

    def fight_zms(self, enemy_hp, enemy_power):
        self.power *= 10
        self.hp /= 2
        print(f"现有攻击力是{self.power}")
        print(f"现有血量是{self.hp}")
        while True:
            self.hp = self.hp - enemy_power
            self.enemy_hp = enemy_hp - self.power
            if self.hp <= 0:
                print("翻倍都没打赢你")
                break
            elif enemy_hp <= 0:
                print("我赢了 贱人！")
                break


class XuZhu(Tonglao):
    def __init__(self, hp, power):
        super().__init__(hp, power)

    def read(self):
        print("罪过罪过")


tl = Tonglao(1000, 20)
tl.see_people("WYZ")
print()
tl.see_people("丁春秋")
print()
# 对战多局，比较血量谁先小于0
tl.fight_zms(500, 200)

xz = XuZhu(888, 50)
xz.read()
xz.fight_zms(500, 50)

# class XuZhu(Tonglao):
#     def __init__(self, hp, power):
#         super().__init__(hp, power)