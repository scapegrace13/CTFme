#!/usr/bin/python3
#
#   Project:    CTFme
#   author:     SCAPE
#   Category:   cypto
#   Challenge:  The base
#   difficulty: very easy
#   Version:    0.1
#
import base64

base_flag = "Q1RFbWV7d2VsY29tZV90b190aGVfYmFzZV9mbGFnfQ=="

def main():
    do_some_magic = base_flag.encode('ascii')
    do_some_magic = base64.b64decode(do_some_magic)
    print("Here you will see the flag...")
    print(base_flag)
    print(do_some_magic)

if __name__ == "__main__":
    main()



