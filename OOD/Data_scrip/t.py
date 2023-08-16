n = 3

# for i in range(n + 1):  
#     for j in range(n + 1):
#         if i <= j:
#             print(i, end=' ')
#         elif j < i:
#             print(j, end=' ')
#     for j in range(n - 1, -1, -1):
#         if i <= j:
#             print(i, end=' ')
#         elif j < i:
#             print(j, end=' ')
#     print()


# for i in range(n - 1, -1, -1):
#     for j in range(n + 1):
#         if i <= j:
#             print(i, end=' ')
#         elif j < i:
#             print(j, end=' ')
#     for j in range(n - 1, -1, -1):
#         if i <= j:
#             print(i, end=' ')
#         elif j < i:
#             print(j, end=' ')
#     print()


# for i in range(1,4):
#     print("loop" ,i )
#     print()

#     for j in range(1,4):
#         print("  loop#",j)
#         print()

#         for x in range(1,4):
#             print("    -",x)
#         print()



s = 3
s = s * 2 + 1

for i in range(s):
    for j in range(s):
        minnum = i 
        if j < minnum:
            minnum = j
        if s - 1 - i < minnum:
            minnum = s - 1 - i
        if s - 1 - j < minnum:
            minnum = s - 1 - j
        value = str(minnum)
        print(value, end='')
    print()