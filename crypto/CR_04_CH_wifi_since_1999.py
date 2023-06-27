#!/usr/bin/python3
#
#   Project:    CTFme
#   author:     scapegrace13
#   Category:   cypto
#   Challenge:  Wifi since 1999
#   difficulty: medium
#   Version:    0.2
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

base_flag = [67, 89, 99, 71, 154, 123, 110, 74, 71, 154, 95, 98, 75, 117, 136, 101, 125, 122, 93, 158, 115, 82, 82, 79, 158, 107, 82, 73, 69, 147, 125]



def main():
    counter = 0
    ciphertext = base_flag
    for a in range(0, 100, 1):
        counter += 1
        keychain = [0, 0, 0, 0, 0]

    print("Your counter is at: " + str(counter))


if __name__ == "__main__":
    print("")
    main()
