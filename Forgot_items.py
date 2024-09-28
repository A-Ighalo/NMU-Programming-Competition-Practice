storeItems = []
c = int(input().strip())

for i in range(c):
    storeItems.append(input())

b = ["keys", "phone", "wallet"]

newc = " ".join(storeItems)

d = []
for i in range(len(b)):
    if b[i] not in storeItems:
        print(b[i])
    else:
        d.append(b[i])

if sorted(d) == sorted(b):
    print("ready")
