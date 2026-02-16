class std:
    def name(self,name):
        self.name = name
        print("my name is ",self.name)

    def course(self,course):
        self.course = course
        print("my course is ",self.course)

s1 = std()
s1.name("Alice")
s1.course("Computer Science")