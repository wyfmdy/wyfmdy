class computer():
    __screen_size = 0
    __price = 0
    __cpu = ''
    __momory_size = 0
    __standby_duration = 0

    def setComputer(self,screen_size,price,cpu,momory_size,standby_duration):
        self.setScreen_size(screen_size)
        self.setPrice(price)
        self.setCpu(cpu)
        self.setMomory_size(momory_size)
        self.setStandby_duration(standby_duration)

    def setScreen_size(self,screen_size):
        if screen_size > 0:
            self.__screen_size = screen_size
        else:
            print("屏幕大小设置错误")

    def setPrice(self,price):
        if price > 0:
            self.__price = price
        else:
            print("价钱设置错误")

    def setCpu(self,cpu):
        self.__cpu = cpu

    def setMomory_size(self,momory_size):
        if momory_size > 0:
            self.__momory_size = momory_size
        else:
            print("内存大小设置有误")

    def setStandby_duration(self,standby_duration):
        if standby_duration > 0 :
            self.__standby_duration = standby_duration
        else:
            print("待机时长设置有误")

    def show(self):
        print(self.__screen_size,"英寸",self.__price,"元",self.__cpu,"型号",self.__momory_size,"内存大小",self.__standby_duration,"待机时长")

    def type(self):
        print("我现在在打字")

    def playGame(self):
        print("我现在在打游戏")

    def video_clip(self):
        print("我现在在看视频")
s = computer()
s.setComputer(16,200,"英特尔",8,20)
s.type()
s.playGame()
s.video_clip()
s.show()