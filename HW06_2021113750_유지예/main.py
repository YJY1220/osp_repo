import sys
#from bin-to-hex conversion import aa
#from union/intersection of intergerts import bb
#from fibonacci number import cc
import scratch

def print_menu():
    print("Select menu: 1)b2h 2)set 3)fibo 4)exit ?")

    inputed_number = int(input(" "))

    if inputed_number == 1:
        print("input bin number: ")
        print("hex number: ")
    elif inputed_number == 2:
        print("input the 1st list: ")
        print("input the 2nd list: ")
        print("union: ")
        print("intersection: ")
    elif inputed_number == 3:
        print("fibonacci number: ")
    elif inputed_number == 4:
        exit()
    elif inputed_number == 5:
        print(scratch.cal_lower(10000))
    else:
        print("번호를 다시 입력하세요.")

while True:
    print_menu()
