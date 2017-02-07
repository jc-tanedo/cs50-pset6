import sys
import cs50

if len(sys.argv) != 2:
    print("Usage: python caesar.py <key>")
    exit(1)

key = int(sys.argv[1])
print("plaintext: ", end="")
plainText = cs50.get_string()

for i in plainText:
    if i >= "A" and i <= "Z":
        i = chr((ord(i) - 64 + key)%26 + 64)
    if i >= "a" and i <= "z":
        i = chr((ord(i) - 96 + key)%26 + 96)
    print(i, end="")

print()