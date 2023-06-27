#!/usr/bin/python3
#
#   Project:    CTFme
#   author:     scapegrace13
#   Category:   cypto
#   Challenge:  You will never find me
#   difficulty: easy
#   Version:    1.0
#
#   Challenge Text: You have to find me, good luck rotating like a helicopter. pepehands
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
    do_some_magic = "magic init"
    for i in range(1, 26):
        do_some_magic = rot_alpha(i)(step_base64)
        ctf_string = "me"
        # print(do_some_magic)
        if ctf_string in do_some_magic:
            # print(do_some_magic)
            break

    # do_some_magic = encode(step_base64, "rot13")
    print("Here you will see the flag...")
    print(base_flag)
    print(step_base64)
    print(do_some_magic)


def create_flag():
    flag_txt = "CTEme{create_your_own_flag_here}"
    flag_rot = rot_alpha(4)(flag_txt)
    flag = flag_rot.encode("ascii")
    flag = base64.b64encode(flag)
    print("That will be your flag:")
    print(flag_txt)
    print(flag_rot)
    print(flag)


if __name__ == "__main__":
    print("")
    main()
    print("")
    # create_flag()
