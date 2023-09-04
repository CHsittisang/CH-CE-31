mony = 3550
lst = []
for i in range(1,17):
    if mony % i == 0:
        lst.append(i)
print(max(lst))
