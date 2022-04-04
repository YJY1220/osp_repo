#!/bin/bash
#set PS3 prompt
declare -a array
PS3="select menu : "

menu=$1
if [ -z "$menu" ]; then
        echo "...none operator parameter..."
        select menu in add sub div mul
        do
                break
        done
fi

num1=$(<num1.txt)
num2=$(<num2.txt)
array=("$num1" "$num2")
op=$menu
case $menu in
        add) let total=num1+num2;;
        sub) let total=num1-num2;;
        div) let total=num1/num2;;
        mul) let total=num1*num2;;
esac

echo " "
echo "num1 : ${array[0]}"
echo "num2 : ${array[1]}"
echo "op : $op"
echo "total : $total"
