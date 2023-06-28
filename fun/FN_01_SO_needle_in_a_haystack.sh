#!/bin/bash
#
#   Project:    CTFme
#   author:     scapegrace13
#   Category:   fun
#   Challenge:  Needle in a haystack
#   difficulty: easy
#   Version:    0.1
#
#   Challenge Text:
#   Damn dude I lost my flag somewhere in my files, please help me finding it.
#
#   du -sh FN_01
#   2.9G    FN_01
#   sha512sum FN_01_SO_needle_in_a_haystack.tar.gz
#   e3e8556f7ae6428005fe04cf6c3c94c9798bcce835fc36c6ff29b666d6beab0be3e5d429c05577f901457db1c30039fd79c8f06ec52011c915fafa781b888a1b  FN_01_SO_needle_in_a_haystack.tar.gz
#
mkdir FN_01
# take care its starting at 10 so dont go below 12 here
range_one=99
range_two=99
range_three=99

echo "working until:  FN_01/FN_01_"$range_one"/"$range_two"/really_"$range_three".txt"
for ((i=10;i<=range_one;++i));
do
  FST_VAR=$i
  # echo "1st iteration:  FN_01_$i"
  mkdir FN_01/FN_01_$i
done

for f in FN_01/*;
do
  SEC_VAR=$f
  # echo "2nd iteration:  $f"
  for ((g=10;g<=range_two;++g));
  do
    TRD_VAR=$SEC_VAR"/"$g
    # echo "3rd iteration: " $SEC_VAR"/"$g
    mkdir $SEC_VAR"/"$g
    for ((file=10;file<=range_three;++file));
    do
      echo -en "\r4thd iteration: "$TRD_VAR"/really_"$file".txt"
      echo "\rCTFme{this_is_the_wrong_flag_sorry}" > $TRD_VAR"/really_"$file".txt"
    done
  done
done


flag_one=$(shuf -i 10-$range_one -n 1)
flag_two=$(shuf -i 10-$range_two -n 1)
flag_three=$(shuf -i 10-$range_three -n 1)

echo "CTFme{create_your_own_flag_here}"  > FN_01/FN_01_$flag_one/$flag_two/really_$flag_three.txt
echo ""
echo "flag is at:     FN_01/FN_01_"$flag_one"/"$flag_two"/really_"$flag_three".txt"

echo "and here the solution"
echo ""
grep -r -v "wrong" FN_01


