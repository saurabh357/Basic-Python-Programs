import datetime
class Person:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def check(self):
        today = datetime.date.today()
        age=today.year-self.dob.year
        if today<datetime.date(today.year,self.dob.month,self.dob.day):
            age=age-1
        if age>=18:
            print(self.name,",Congrats You are eligible")
        else:
            print(self.name,",Sorry You are Not eligible")
P1=Person("Saurabh", datetime.date(1999,8,28))
P1.check()