#!/bin/bash
#
#   Project:    CTFme
#   author:     scapegrace13
#   Category:   cracking
#   Challenge:  Lets start with an easy one
#   difficulty: easy
#   Version:    0.1
#
#   Challenge Text:
#   Hey, can you help me recovering my password? John said maybe some rocks could help?
#   And I want to mention, I really don't support nor like cats. But "thread-10219-2" will explain you why.
#
mkdir CRA_01
echo "CTEme{create_your_own_flag_here}"
echo "CTEme{create_your_own_flag_here}" > CRA_01/CRA_01_flag.txt
CREATE_PASSWORD=$(shuf -n 1 /usr/share/wordlists/rockyou.txt) # $(shuf -i 10-20 -n 1)
echo "used Password: $CREATE_PASSWORD"
zip -P "$CREATE_PASSWORD" -r CRA_01_CHA_lets_start_with_an_easy_one.zip CRA_01/
echo ""
echo "cleanup zip folder"
rm CRA_01 -r -v
echo ""
echo "sha1sum for zip file"
sha1sum CRA_01_CHA_lets_start_with_an_easy_one.zip
echo ""
# 8ea6046dc78a69f01b40b8b10f4b39941086da3f  CRA_01_CHA_lets_start_with_an_easy_one.zip
#
# the solution:
#
zip2john CRA_01_CHA_lets_start_with_an_easy_one.zip > CRA_01_CHA_lets_start_with_an_easy_one.hash
john --wordlist=/usr/share/wordlists/rockyou.txt CRA_01_CHA_lets_start_with_an_easy_one.hash
