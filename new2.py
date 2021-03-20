class Employee:
    empCount=0
    def __init__(self,name,desig,salary):
        self.name=name
        self.desig=desig
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("There are %d employees" %Employee.empCount)
    def displayinfo(self):
        print("name is ", self.name, "desingnation is:",self.desig,"and atlast salary is", self.salary)
e1=Employee("Saurabh","manager",20000)
e2=Employee("Shaurya","developer",50000)
e3=Employee("Harsh","HR",200000)
e1.displayCount()
e1.displayinfo()
e2.displayinfo()
e3.displayinfo()