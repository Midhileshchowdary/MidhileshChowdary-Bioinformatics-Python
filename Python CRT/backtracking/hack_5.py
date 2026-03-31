s = input("Enter the Sequence :").lower()
seen = set()
repeated = set()
for char in s:
    if char in seen:
        repeated.add(char)
    else:
        seen.add(char)

print(len(repeated))