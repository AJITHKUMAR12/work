class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):
        print("hello world",self.name)
    def vote(self):
        if self.age>18:
            print("you are eligible")
        else:
            print("you are not eligible")
obj=person("aj",12)
obj1=person("ak",18)
print(obj1.name,obj.name)
obj.talk()
obj.vote()
obj1.talk()
obj1.vote()



class car:
    def __init__(self,year,speed):
        self.year=year
        self.speed=speed
    def getspeed(self):
        print(self.speed)
    def setspeed(self,speed):
        print(speed)

obj=car(2100,121)
obj.getspeed()
obj.setspeed(100)

obj1=car(2104,190)
obj1.getspeed()


