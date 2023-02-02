# five = 5
# res = 0
# for i in range(five + 1):
#     res =  res + i
#     print(res)

n = int(input())
sum = 0
if n > 0:
    for i in range(1, n + 1):
        sum += i
else:
    for i in range(n, 2):
        sum += i
print(sum)
