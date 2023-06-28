#!/usr/bin/python3.10
#
#   Project:    CTFme
#   author:     scapegrace13
#   Category:   cypto
#   Challenge:  A journey through our Windows
#   difficulty: medium
#   Version:    0.1 - work in progress
#
#   Challenge Text:
#
#
#

import base64


from passlib.hash import lmhash
from crypto.hash import md4
import hashlib
import binascii

base_flag = "TBDDTBDDTBDDTBDD"
hash = "password"


def do_lm(hash):
    #lm_hash = lmhash.hash(bytes(base_flag, "utf-16"))
    lm_hash = lmhash.hash("password")
    print(lm_hash)
    print(binascii.hexlify(lm_hash.encode()))


def do_ntlm(hash):
    hash_ntlm =  MD4.new()
    hash_ntlm.update(b"hash")
    print(hash_ntlm.hexdigest())
    # ntlm_hash = hashlib.new("md4", hash.encode("utf-16le")).digest()
    # print(binascii.hexlify(ntlm_hash))


def do_ntlmv2(hash):
    ntlmv2_hash = hashlib.new("md4", hash.encode("utf-16le")).digest()
    print(binascii.hexlify(ntlmv2_hash))


def main():
    do_some_magic = "magic init"

    do_lm(hash)
    do_ntlm(hash)
    #do_ntlmv2(hash)


    # do_some_magic = encode(step_base64, "rot13")
    print("Here you will see the flag...")
    print(base_flag)
    print(do_some_magic)


def create_flag():
    flag_txt = "CTEme{create_your_own_flag_here}"


if __name__ == "__main__":
    print("")
    main()
    print("")
    # create_flag()
