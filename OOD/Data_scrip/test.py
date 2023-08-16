# num,n = [int(x) for x in input("enter number").split()]
# num = 16
# n = 2
# x = 0
# i = 0
# while i < num :
#     i = n ** x 
#     x += 1



print("*** fibonacci sequence ***")
a0, a1, n = input("Enter a0 a1 n : ").split()
a0 = int(a0)
a1 = int(a1)
n = int(n)
s = f"{a0}"
count = 1   
while count < n:
    s += f", {a1}"
    sol = a0 + a1
    a0 = a1
    a1 = sol
    count += 1
print(s)
print("*** end of fibonacci sequence ***")