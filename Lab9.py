
#Lab 9 Git

def encode(password):
    menu()
    encode_pass = []
    for digit in password:
        new_number = str(int(digit) + 3)
        encode_pass.append(new_number)
    return ''.join(encode_pass)

def decode(password):
    menu()
    decode_pass = []
    for digit in password:
        new_number = str(int(digit) - 3)
        decode_pass.append(new_number)
    return ''.join(decode_pass)


def menu():
    while True:
        print("Menu")
        print("____________")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        dec = input("Please enter an option:")
        if dec == "1":
            password = input("Please enter your password to encode:")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif dec == "2":
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
            pass
        elif dec == "3":
            break

