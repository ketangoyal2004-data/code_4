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
    
    def age(self,age):
        self.age = age
        print(self.age)

    def specialization(self,specialization):
        self.specialization = specialization
        print(self.specialization)

s1 = std()
s1.name("Alice")
s1.course("Computer Science")
s1.branch("Software Development")
s1.age(20)
s1.specialization("Artificial Intelligence")