# Comments about how my program went:
# Overall, my program was super messy, but I am also new to Python.
# I had a lot of fun coding with Python and I now understand why everyone enjoys it.
# This program really helped me learn Python. I had to learn/research so many things and practice a lot.
# I felt that the program was easy, btu I got lost on the part 3 instructions.
# Once I understood the instructions, I was able to get the hang of it all. Most of my errors were small things
# with Python syntax.
# The line in the instrions that confused me the most was:
# "Converted 4000 to Error back to 0, which is wrong."
# Everything else was pretty great. I took my time on this to learn Python thoroughly. Thank you!

import sys  # allows for command line arguments


def romanFunc(x):  # passing in x from romanamor.py or function call
    if x == -5:  # if x == -5 then it is a command line argument
        cla = len(sys.argv)  # this is how many command line arguments there are
    else:  # if x != -5 then it is a function call from romanamor.py
        cla = 2  # so the for loop only loops once
    roman = ''
    i = 1
    for i in range(1, cla):  # the range is between 1 and either 2 or # of command line arguments
        if x == -5:  # if it is a command line argument, make originalNum equal to argument i
            originalNum = int(sys.argv[i])
        else:  # if it is a function call from romanamor.py, make originalNum equal to passed value
            originalNum = int(x)
        if 0 < originalNum < 4000:  # if originalNum is less than 4000 and greater than 0, set num to argument
            if x == -5:
                num = int(sys.argv[i])
            else:
                num = int(x)
            roman = ''  # reset roman
            while num > 0:
                if num - 1000 >= 0:  # if num - 1000 >= 0 then decrement num by 1000 and add character to roman
                    num -= 1000
                    roman += 'M'
                elif num - 900 >= 0:
                    num -= 900
                    roman += 'CM'
                elif num - 500 >= 0:
                    num -= 500
                    roman += 'D'
                elif num - 400 >= 0:
                    num -= 400
                    roman += 'CD'
                elif num - 100 >= 0:
                    num -= 100
                    roman += 'C'
                elif num - 90 >= 0:
                    num -= 90
                    roman += 'XC'
                elif num - 50 >= 0:
                    num -= 50
                    roman += 'L'
                elif num - 40 >= 0:
                    num -= 40
                    roman += 'XL'
                elif num - 10 >= 0:
                    num -= 10
                    roman += 'X'
                elif num - 9 >= 0:
                    num -= 9
                    roman += 'IX'
                elif num - 5 >= 0:
                    num -= 5
                    roman += 'V'
                elif num - 4 >= 0:
                    num -= 4
                    roman += 'IV'
                elif num - 1 >= 0:
                    num -= 1
                    roman += 'I'
            else:  # Else is used once while is completed to print the roman numeral if using command line arguments
                if x == -5:
                    print(str(originalNum) + " is " + roman)
        else:  # Else is used if originalNum is not between 0 and 4000 and prints error message
            if x == -5:
                print(str(originalNum) + " is Error ")
    return roman  # returns roman for romanamor.py


x = -5
romanFunc(x)  # calls romanFunc
