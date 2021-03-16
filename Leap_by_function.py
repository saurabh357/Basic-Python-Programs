def is_leap(y):
    leap=False
    if(y%4)==0:
        if(y%100)==0:
            if(y%400)==0:
                leap=True
            else:
                leap=False
        else:
            leap=False
    else:
        leap=False
        
    return leap

year = int(raw_input())
print is_leap(year)