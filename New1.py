class Students:
    def __init__(self,name):
        self.name= name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input("Enter the marks of %s in subject %d:" %(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got", self.marks)
s1=Students("Saurabh")
s1.entermarks()
s2=Students("harsh")
s2.entermarks()
s1.display()
s2.display()
    