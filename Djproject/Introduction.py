//class Introduction:
    a = ''
    b = ''
    c = ''

    def __init__(self, pri, time, rate):
        self.a = int(pri)
        self.b = int(time)
        self.c = int(rate)

    def fun(self):
        x = self.a * self.b * self.c * 0.001
        return (x)


obj = Introduction(10000, 2, 8)
print(obj.fun())
