#!/usr/bin/python3
#
#   Project:    CTFme
#   author:     SCAPE
#   Category:   cypto
#   Challenge:  What the rot
#   difficulty: very easy
#   Version:    1.0
#
#   Challenge Text: What the ROT ??? I mean really?
#
from codecs import encode
base_flag = "PGRzr{bxnl_gung_ebg_rnfl}"


def main():
    do_some_magic = encode(base_flag, "rot13")
    print("Here you will see the flag...")
    print(base_flag)
    print(do_some_magic)


def create_flag():
    flag_txt = "CTEme{create_your_own_flag_here}"
    flag = encode(flag_txt, "rot13")
    print("that will be your flag:")
    print(flag_txt)
    print(flag)


if __name__ == "__main__":
    print("")
    main()
    print("")
    # create_flag()
