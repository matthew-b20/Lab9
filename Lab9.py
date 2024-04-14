
#Lab 9 Git

def encode(password):
    menu()
    for int in password:
        new_number = str(int(digit) + 3)
        encode_pass += new_number
    return encoded_pass

print(encode("1234555"))

def menu():
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

