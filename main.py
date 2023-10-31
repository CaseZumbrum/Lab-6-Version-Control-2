
'''
Written by: Case Zumbrum

encode() encodes an integer password by increasing each integer by 3

Input:
    password (String): password to be encoded, all characters must be integers and there should be 8 digits

Return:
    encoded_password (String): encoded password
'''
def encode(password):
    encoded_password = ''
    for char in password:
        if char == '7':
            encoded_password += str(0)
        elif char == '8':
            encoded_password += str(1)
        elif char == '9':
            encoded_password += str(2)
        else:
            encoded_password += str(int(char)+3)
    return encoded_password


# Decode function
def decoder(password):
    list_password = list(password)  # Turns the string into a list
    for i in range(0, len(list_password)):
        list_password[i] = int(list_password[i])  # Turns all the items into integers so 3 can be subtracted
    for i in range(0, len(list_password)):  # Check for special cases
        if list_password[i] == 0:
            list_password[i] = 7
        if list_password[i] == 1:
            list_password[i] = 8
        if list_password[i] == 2:
            list_password[i] = 9
        else:
            list_password[i] = int(list_password[i]) - 3 # Subtract 3 if not a special case
    for i in range(0, len(list_password)):
        list_password[i] = str(list_password[i])  # Turn the list items back into a string

    return "".join(list_password)  # Combine all the items of the list into one string

'''
Written by: Case Zumbrum
'''
if __name__ == "__main__":
    while True:
        choice = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option:"))
        if choice == 1:
            password = input("Please enter your password to encode:")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
        else:
            exit()
