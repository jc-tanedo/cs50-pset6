import cs50

QUARTERS = 25
DIMES = 10
NICKELS = 5
PENNIES = 1

while True:
    print("O hai! How much change is owed? ", end="")
    changeOwed = cs50.get_float()
    if changeOwed > 0:
        break
    print("Invalid.")

changeOwed *= 100;
coinCount = 0

while changeOwed:
    if changeOwed >= QUARTERS:
        coinCount += changeOwed // QUARTERS
        changeOwed = changeOwed % QUARTERS
    if changeOwed >= DIMES:
        coinCount += changeOwed // DIMES
        changeOwed = changeOwed % DIMES
    if changeOwed >= NICKELS:
        coinCount += changeOwed // NICKELS
        changeOwed = changeOwed % NICKELS
    if changeOwed >= PENNIES:
        coinCount += changeOwed // PENNIES
        changeOwed = changeOwed % PENNIES

print("{:.0f}".format(coinCount))