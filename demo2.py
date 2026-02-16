class cal:
    def add(self,a,b):
        self.a = a
        self.b = b
        print("The sum is ",self.a + self.b)

    def sub(self,a,b):
        self.a = a
        self.b = b
        print("The diff is",self.a - self.b)

    def mul(self,a,b):
        self.a = a
        self.b = b
        print(self.a * self.b)

    def div(self,a,b):
        self.a = a
        self.b = b
        print(self.a / self.b)

    def exp(self,a,b):
        self.a = a
        self.b = b
        print(self.a ** self.b)

    def mod(self,a,b):
        self.a = a
        self.b = b
        print(self.a % self.b)



obj = cal()
obj.add(10,5)   
obj.sub(10,5)
obj.mul(10,5)