import cs50

def check_valid(cardNumber):
    sum = 0
    odd = True
    
    while True:
        # print("{} - {}", cardNumber, sum, end="")
        i = cardNumber % 10
        cardNumber //= 10
        if odd:
            sum += i
        elif i < 5:
            sum += 2*i
        else:
            sum += ((2*i) % 10) + 1
        if cardNumber <= 0:
            break
        odd = not odd
    if (sum % 10) == 0:
        return True
    else:
        return False

def identify_card(cardNumber):
    while(cardNumber > 100):
        cardNumber //= 10
        
    if cardNumber in (34, 37):
        return "AMEX"
    elif cardNumber in (51, 52, 53, 54, 55):
        return "MASTERCARD"
    else:
        cardNumber /= 10
        if cardNumber == 10:
            return "VISA"
    
    return "ERROR"
    
def main():
    print("Number: ", end="")
    cardNumber = cs50.get_int()
    
    if (check_valid(cardNumber)):
        print(identify_card(cardNumber))
    else:
        print("INVALID")

if __name__ == "__main__":
    main()