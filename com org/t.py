w = input("Enter a word: ")
o = ""
for i in w[::-1]:
    o += i
print(o)
print(o.upper())