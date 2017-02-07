positive = open("positive-words.txt", "r")

str = positive.readlines()
str = [x.strip("\n") for x in str]

for i in str:
    if i == "tops":
        print(i)
        break