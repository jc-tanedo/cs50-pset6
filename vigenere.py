import sys
import cs50

if len(sys.argv) != 2:
    print("Usage: python vigenere.py <key>")
    exit(1)

key = sys.argv[1]
keyOrd = []
for i in range(len(key)):
    if key[i].isalpha():
        keyOrd.append(ord(key[i])%32 - 1)
    else:
        print("Key must be alphabetic")
        exit(1)

print("plaintext: ", end="")
plainText = cs50.get_string()

for x in range(len(plainText)):
    i = plainText[x]
    j = keyOrd[x % len(key)]
    if i >= "A" and i <= "Z":
        i = chr((ord(i) - 64 + j)%26 + 64)
    if i >= "a" and i <= "z":
        i = chr((ord(i) - 96 + j)%26 + 96)
    print(i, end="")

print()