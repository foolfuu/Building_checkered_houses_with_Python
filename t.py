m = int(input(""))
n = int(input(""))

for i in range(n): print(" ---",end = "")
print()
for i in range(m):
    for i in range(n+1):
        if i == 0:print("|",end = "")
        else:print("   |",end = "")
    print()
    for i in range(n): print(" ---",end = "")
    print()


