#!/usr/bin/python3
#
#   Project:    CTFme
#   author:     SCAPE
#   Category:   cypto
#   Challenge:  You will never find me
#   difficulty: easy
#   Version:    0.1
#
from codecs import encode
import base64
import string

base_flag = "WVBBaWF7aGtrZ19wZHdwX25rcF9lb19pa25hX3BuZXlndX0="

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = string.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


def main():
    step_base64 = base_flag.encode("ascii")
    step_base64 = base64.b64decode(base_flag)
    for i in range(1, 26):
        do_some_magic = "not found"
        do_some_magic = rot_alpha(i)(step_base64)
        ctf_string = "me"
        # print(do_some_magic)
        if ctf_string in do_some_magic:
            #print(do_some_magic)
            break

    # do_some_magic = encode(step_base64, "rot13")
    print("Here you will see the flag...")
    print(base_flag)
    print(step_base64)
    print(do_some_magic)

if __name__ == "__main__":
    main()