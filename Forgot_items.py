# This script checks if you forgot any essential items (keys, phone, wallet) before heading out.
# Input:
#   The first line contains a single integer c (number of items grabbed).
#   The next c lines each contain a single nonempty string of lowercase letters indicating an item grabbed.
# Output:storeItems = []
#   Each of "keys", "phone", and "wallet" that does not appear in the input, one per line in alphabetical order.c = int(input().strip())
#   If none of these items are missing, print "ready".

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
