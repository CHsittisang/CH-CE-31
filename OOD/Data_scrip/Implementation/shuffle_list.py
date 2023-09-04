import random

def shuffle_item(lst):
    lst.insert(random.randint(0,len(lst)),lst.pop(-1))
    return 

def shuffle_list(lst, c):
    while c < 10:
        a1 = [] 
        a2 = []
        while len(lst) > 0:
            a1.append(lst.pop(0))
            if len(lst) > 0:
                a2.append(lst.pop(0))
        while len(a1) != 0 or len(a2) != 0:
            if c % 2 == 0:
                if len(a2) != 0:
                    lst.append(a2.pop(-1))
                lst.append(a1.pop(0))
            else:
                lst.append(a1.pop(0))
                if len(a2) != 0:
                    lst.append(a2.pop(-1))
        c += 1  
    print(lst)

slot = ['cherry','lemon','apple','banana','orange','grape','melon','bar','bell']
for i in range(len(slot)):
    shuffle_list(slot,i)