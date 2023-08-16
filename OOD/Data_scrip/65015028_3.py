# def searching_num(dat, num):
#     first_num = 0
#     last_num = len(dat)-1
#     while first_num <= last_num:
#         mid = (first_num + last_num) // 2
#         if dat[mid] == num:
#             return mid
#         elif dat[mid] < num:
#             first_num = mid + 1
#         else:
#             last_num = mid - 1
#     return -1

# import random
# dat = list(range(1,100))
# num = int(input("Enter a number: "))
# print(searching_num(dat, num))
import random
print(random.randint(1, 38))