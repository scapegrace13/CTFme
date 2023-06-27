#!/usr/bin/python3
#
#   Project:    CTFme
#   author:     scapegrace13
#   Category:   cypto
#   Challenge:  Wifi since 1999
#   difficulty: medium
#   Version:    0.3
#
#   Challenge Text:
#   I mean, the challenge name...do it via python, the pcap will come later.
#   I maybe lost a keychain in here. I remember nothing and numeric leet, then there was the answer to everything and FF
#
#   When you DO understand the hints and DO know what you are looking for:      Key found!: XXX at No. 7.140.608 after 18.0s
#   When you DO understand the hints and DONT know what you are looking for:    Key found!: XXX at No. 34.238.208 after 326.0s
#   When you DONT understand the hints and DONT know what you are looking for:  Key found!: XXX at No. 220.539.648 after 2072.0s
#
import random
import timeit
import math

start = timeit.default_timer()

base_flag = [72, 66, 103, 65, 154, 112, 117, 83, 73, 158, 127, 115, 126, 85, 144, 126, 100, 126, 67, 136, 101, 73, 71, 64, 158, 108, 73, 73, 73, 141, 110, 107]
# base_flag = [67, 89, 99, 71, 154]



def main():
    counter = 0
    ciphertext = base_flag
    for a in range(0, 12, 1):
        key_a = a
        for b in range(10, 25, 1):
            key_b = b
            for c in range(30, 35, 1):
                key_c = c
                for d in range(40, 50, 1):
                    key_d = d
                    for e in range(210, 256, 1):
                        key_e = e

                        counter += 1
                        key = [key_a, key_b, key_c, key_d, key_e]
                        # print("KEY: ", key)
                        decrypt(ciphertext, key)

                        # Decryption
                        decrypted_plaintext = decrypt(ciphertext, key)
                        readable_plaintext = ""
                        for y in decrypted_plaintext:
                            readable_plaintext += chr(y)

                        ctf_string = "CTFme"
                        parse_plaintext = ("LF string: " + ctf_string + " == " + (str(readable_plaintext))[:5])
                        # print(parse_plaintext)
                        if ctf_string == (str(readable_plaintext))[:5]:
                            stop = timeit.default_timer()
                            print("Key found!: " + ctf_string + " at No. " + str(counter) + " after " + str(math.floor(stop - start)) + "s")
                            print("Key was:", key)
                            print("Flag is: " + str(readable_plaintext))
                            # when you play and dont know the keychain, you should use exit here
                            # exit(1)

                        if False:
                            print("Decrypted Plaintext:")
                            print(decrypted_plaintext)
                            print("Did you found the flag? ")
                            print(str(readable_plaintext))
                            print("")


def decrypt(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        keystream = ciphertext[i] ^ key[i % len(key)]
        plaintext.append(keystream)
    return plaintext


def create_flag():
    # WEP crypto starting here
    def generate_key():
        key = []
        for _ in range(5):
            key.append(random.randint(0, 255))

        # maybe you want to hardcode funny numbers 0-255
        key = [11, 22, 33, 44, 255]
        return key



    def encrypt(plaintext, key):
        ciphertext = []
        for i in range(len(plaintext)):
            keystream = plaintext[i] ^ key[i % len(key)]
            ciphertext.append(keystream)
        return ciphertext



    # Example usage
    flag_txt = "CTFme{create_your_own_flag_here}"
    plaintext = [ord(c) for c in flag_txt]
    # plaintext = [65, 66, 67, 68, 69]  # ASCII values of 'ABCDE'

    # Generate key
    key = generate_key()
    print("Key: ")
    print(key)
    print("")
    # Encryption
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext: ")
    print(ciphertext)
    print("")
    print("That will be your flag:")
    print(flag_txt)
    print(ciphertext)


if __name__ == "__main__":
    print("")
    main()
    print("")
    create_flag()
