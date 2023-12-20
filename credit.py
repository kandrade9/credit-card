amex = ['34', '37']  # first 2 digits for amex
master = ['51', '52', '53', '54', '55']  # first 2 digits for mastercard

def checksum(card_number):
    """
    Determine whether card number is valid
    :param card_number: str
    :return: bool
    """
    card_len = len(card_number)
    reversed_card = card_number[::-1]

    products = []
    for i in range(1, card_len, 2):
        product = str(int(reversed_card[i]) * 2)

        # split any products longer than 1 digit
        if len(product) > 1:
            for digit in product:
                products.append(digit)
        else:
            products.append(product)

    products = [int(product) for product in products]
    product_sum = sum(products)

    for j in range(0, card_len, 2):
        product_sum += int(reversed_card[j])

    if product_sum % 10 == 0:
        return True
    else:
        return False


user_input = input("Card Number: ")
while not user_input.isdigit():
    user_input = input("Card Number: ")
result = checksum(user_input)

if result:
    if user_input[:2] in amex:
        print("AMEX")
    elif user_input[:2] in master:
        print("MASTERCARD")
    elif user_input[0] == '4':
        print("VISA")
    else:
        print("VALID")
else:
    print("INVALID")
