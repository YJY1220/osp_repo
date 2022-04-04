#!/bin/bash
# set PS3 prompt
PS3="select menu : "
mkdir temp
echo "...create temp directory..."

cp num1.txt temp/num1.txt
cp num2.txt temp/num2.txt
cp mycal.sh temp/mycal.sh

echo "...copy filed to temp directory..."

cd temp
select menu in  add sub div mul
do
        echo "...$menu  selected..."
        echo "...run calculator..."
        ./mycal.sh $menu
        break
done