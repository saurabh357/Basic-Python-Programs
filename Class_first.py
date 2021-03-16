

''' Write a Program that uses class to Store Name and marks of the students.
Use list to store the marks in three subjects'''
class students:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def enterMarks(self):
        for i in range(3):
            m=int(input("enter the marks %s in subject %d :" %(self.name, i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name, "achieve", self.marks)
        
#objects
s1 = students("Saurabh")
s1.enterMarks()
s2 = students("Shaurya")
s2.enterMarks()
s1.display()
s2.display()
            
            
            