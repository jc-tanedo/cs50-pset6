import crypt
import cs50

buffer = list("A")

def next_letter(buffer, n):
    if buffer[n] == "z":
        #print("".join(buffer))
        if n == 0:
            for i in range(len(buffer)):
                buffer[i] = "A"
            buffer.append("A")
            return
        buffer[n] = "A"
        next_letter(buffer, n-1)
        return
    while True:
        buffer[n] = chr(ord(buffer[n]) + 1)
        if buffer[n].isalpha():
            break
    return

def main():
    inputHash = cs50.get_string()
    salt = inputHash[:2]
    while True and len(buffer) <= 4:
        testString = "".join(buffer)
        if inputHash == crypt.crypt(testString, salt):
            print(testString)
            exit(0)
        next_letter(buffer, len(buffer) - 1)
    print("Not found")

if __name__ == "__main__":
    main()