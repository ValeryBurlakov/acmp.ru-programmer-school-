# from datetime import datetime
# import time
# start_time = datetime.now()
a, b, c = list(map(int, input().split()))
# возможности питона
f = max(a, b, c)
d = min(a, b, c)
print(f - d)
# мой код
# if a > b and a > c:
#     if b > c:
#         print(a - c)
#     else:
#         print(a - b)
# elif b > c and b > a:
#     if a > c:
#         print(b - a)
#     else:
#         print(b - c)
# else:
#     if a > b:
#         print(c - b)
#     else:
#         print(c - a)
# time.sleep(0)

# print(datetime.now() - start_time)