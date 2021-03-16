class Myinfo:
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.Last_name=lname
        self.AGE=age
    def ShowInfo(self):
        print("Fname is ",self.first_name,  "last name is ", self.Last_name,"and age is " ,self.AGE )

m1=Myinfo("Saurabh", "Kamra", 23)
m1.ShowInfo()
  
    
'''
Fn=input("My first Name is: ")
Ln=input("My last name is: ")
A=int (input("Age is: "))
'''
