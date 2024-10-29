
# create a program that encrypts and decrypts a message using RSA
# 1. convert the message to ascii digits and back to
# 2. encrypts the converted ascii using rsa public key
# 3. decrypt the encrypted message and convert it back to the main message

# 1

# create a function that converts letters, numbers and symbols to their ascii numerics
def convert_to_ascii(message):
    converted = [ord(i) for i in message]
    return converted

def revert_ascii(message):
    # takes ascii numerics and converts back to their character representation
    converted_message = "".join([chr(i) for i in message])
    return converted_message

# 2
def encrypt(m, e, n):
    # to convert m^e mod n
    # convert all the information in the message to ascii
    converted = convert_to_ascii(m)
    # perform RSA encryption conversion
    cipher_text = [str((i ** e) % n) for i in converted]

    return " ".join(cipher_text)


def find_d(e, r):
    # d.3 == 1 mod 40
    for i in range(r):
        x = (i * e) % r
        y = (x // r)
        if x == 1 and (r * y + 1) == x:
            d = i
            break
    print(d)
    return d

def is_prime(num):
    for i in range(1 ,num):
        if num % i == 0 and i != num and i != 1:
            return False
        else:
            return True



def decrypt(cipher_text, d, n):
    #  to decipher cipher_text ^ d mod n
    # convert each message in the cipher_text back to the original ascii numerics
    decipher_text = [((int(i) ** d ) % n) for i in cipher_text.split()]
    # convert decipher_text ascii back to original message
    original_message = revert_ascii(decipher_text)
    return original_message

def main():
    print("Welcome to simple RSA encryption")
    while True:
        print("1. Encrypt a file\n2. Decrypt a file\n3. Quit")
        p = 1099503947
        q = 53
        n = p * q
        phi_n = (p - 1) * (q - 1)
        e = 17
        d = find_d(e, phi_n)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("1. Encrypt from file path\n2. Enrypt via text input")
            option = input("Enter an option: ")
            if option == "1":
                file_path = input("Enter file path: ")
                with open(fr"{file_path}", "r", encoding="utf-8") as file:
                    encoded_message = encrypt(file.read(), e, n)
                    print(encoded_message)
                with open(fr"{file_path}", "w+", encoding="utf-8") as file:
                    encoded_message_str = "".join(map(str, encoded_message))

                    file.write(encoded_message_str)

            return  0
        if choice == "2":
            print("1. Decrypt from file path\n2. Decrypt via text input")
            option = input("Enter an option: ")
            if option == "1":
                file_path = input("Enter file path: ")
                with open(fr"{file_path}", "r", encoding="utf-8") as file:
                    decoded_message = decrypt(file.read(), d, n)

                    print(decoded_message)

                with open(fr"{file_path}", "w+", encoding="utf-8") as file:
                    decoded_message
                    file.write(decoded_message)




print(main())


#
