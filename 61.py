# a1, b1, b2, b3, b4 = input().split()
# a = 0
# b = 0
# a1 = int(a1)
# b1 = int(b1)
# a2 = int(input())
# b2 = int(b2)
# a3 = int(input())
# b3 = int(b3)
# a4 = int(input())
# b4 = int(b4)
# a = a1 + a2 + a3 + a4
# b = b1 + b2 + b3 + b4
# if a > b:
#     print('1')
# elif a < b:
#     print('2')
# else:
#     print('DRAW')

with  open('INPUT.txt') as inp:
    sa = 0
    sb = 0
    for a,b in map(str.split,inp.readlines()):
        sa += int(a)
        sb += int(b)
if sa > sb:
    print("1")
elif sa == sb:
    print("DRAW")
else:
    print("2")



        # if a > b:
        #     sm = 0
        #     sm += int(a)
        #     print(sm)
        #     # out.write('1' + '\n') # запись в файл
        # elif a < b:
        #     # print(b)
        #     print(a)
        #     # out.write('2' + '\n')
        # else:
        #     print("DRAW")
        #     # out.write('DRAW' + '\n')