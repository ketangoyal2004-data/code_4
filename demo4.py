class std:
    def name(self,name):
        self.name = name
        print(self.name)

    def course(self,course):    
        self.course = course
        print(self.course)

s1 = std()
s1.name("Alice")
s1.course("Computer Science")