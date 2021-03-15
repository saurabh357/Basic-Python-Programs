year=int(input("enter a year"))
if year%100==0:
    if year%400==0:
        print("it's an leap year bro")
    else:
        print("sorry bro it's not an leap year")
else:
    if year%4==0:
        print("yup it's an leap year")
    else:
        print("OOps Sorry Not an leap year")
        
        