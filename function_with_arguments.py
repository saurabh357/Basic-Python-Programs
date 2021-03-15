sis=int(input("Tell me amount you have"))
def moneycheck(x):
    if x<7000:
        print("Ahm can you rethink")
    elif x>10000:
        print("Wow sis! You are a Queen")
    elif x in range(7000,10000):
        print("Cool Thanks")
        return
    

moneycheck(sis)