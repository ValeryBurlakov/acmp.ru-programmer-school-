num = str(input())
if num == "5":
    print(25)
else:    
    numstr = str(num[:-1])
    preres = 0
    preres = int(numstr) * (int(numstr) + 1)
    preres = str(preres) + str("25")
    print(preres)