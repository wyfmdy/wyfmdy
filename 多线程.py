from threading import Thread #导入thread类
import time #导入时间模块
egg_tart_num = 0 #蛋挞的总量
sur = 0


class person (Thread):
    name = ""
    count = 0

    def run(self) -> None:
        global egg_tart_num
        global sur
        while True:
            if egg_tart_num < 500:
                egg_tart_num += 1
                print(self.name,"生成1个蛋挞","篮子有",egg_tart_num,"个蛋挞")
            if egg_tart_num >= 500:
                time.sleep(2)
            if sur == 6:
                return


class customer(Thread):
    username = ""
    count = 0

    money = 3000
    def run(self) -> None:
        global egg_tart_num
        global sur
        while True:
            if self.money >= 3 and egg_tart_num>=1:
                egg_tart_num -= 1
                self.money -= 3
                print(self.name,"购买1个蛋挞","蛋挞篮有",egg_tart_num,"剩余金额为",self.money)

            if egg_tart_num <= 0:
                time.sleep(3)
            if self.money < 3:
                sur += 1

                return 1

def user():
    c1=person()
    c1.name = "厨师1"
    c2=person()
    c2.name = "厨师2"
    c3=person()
    c3.name = "厨师3"
    c1.start()
    c2.start()
    c3.start()


    p1=customer()
    p1.name = "顾客1"
    p2=customer()
    p2.name = "顾客2"
    p3=customer()
    p3.name = "顾客3"
    p4=customer()
    p4.name = "顾客4"
    p5=customer()
    p5.name = "顾客5"
    p6=customer()
    p6.name = "顾客6"
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()


user()