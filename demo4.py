class std:
    def name(self,name):
        self.name = name
        print(self.name)

    def course(self,course):    
        self.course = course
        print(self.course)

    def branch(self,branch):
        self.branch = branch
        print(self.branch)

s1 = std()
s1.name("Alice")
s1.course("Computer Science")
s1.branch("Software Development")