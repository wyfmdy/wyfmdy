class cup:
    __height = 0    #高度
    __volume = 0    #容积
    __color = ""    #颜色
    __texture = ""  #材质
    __liquids = ["水","饮料"]   #能存放的液体

    def setCup(self,height,volume,color,texture):
        self.setHeight(height)
        self.setVolume(volume)
        self.setColor(color)
        self.setTexture(texture)

    def setHeight(self,height):
        if height > 0:
            self.__height =  height
        else:
            print("水杯高度有误")

    def setVolume(self,volume):
        if volume > 0:
            self.__volume = volume
        else:
            print("水杯体积有误")

    def setColor(self,color):
        self.__color = color

    def setTexture(self,texture):
        self.__texture = texture

    def deposit(self,liquid):
        if liquid not in self.__liquids:
            print("对不起，不能存放该种液体")
        else:
            print("存放成功")

    def show(self):
        print("该水杯材质为",self.__texture,"颜色为",self.__color,"高度为",self.__height,"容积为",self.__volume,"的水杯")

c = cup()
c.setCup(10,20,"白色","不锈钢")
c.deposit("水")
c.show()


