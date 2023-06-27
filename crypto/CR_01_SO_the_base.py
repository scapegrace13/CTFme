#!/usr/bin/python3
#
#   Project:    CTFme
#   author:     SCAPE
#   Category:   cypto
#   Challenge:  The base
#   difficulty: very easy
#   Version:    1.0
#
import base64

base_flag = "Q1RFbWV7d2VsY29tZV90b190aGVfYmFzZV9mbGFnfQ=="


def main():
    do_some_magic = base_flag.encode('ascii')
    do_some_magic = base64.b64decode(do_some_magic)
    print("Have fun searching the flag...")
    print(base_flag)
    print(do_some_magic)


def create_flag():
    flag_txt = "CTEme{create_your_own_flag_here}"
    flag = flag_txt.encode('ascii')
    flag = base64.b64encode(flag)
    print("that will be your flag:")
    print(flag_txt)
    print(flag)


if __name__ == "__main__":
    print("")
    main()
    print("")
    # create_flag()


