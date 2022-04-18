import sys  # allows for command line arguments


def namorFunc(x):  # passing in x from romanamor.py or function call
    if x == 'Ry':  # If the function wasn't sent from romanamor.py then I get how many arguments there are
        cla = len(sys.argv)
    else:  # if x != 'Ry' then I make cla = 2 so that the for loop only loops once
        cla = 2
    i = 1
    num = 0
    for i in range(1, cla):  # similar to 1 < i < cla
        if x == 'Ry':  # if the func wasn't sent from romanamor.py then I take in command line argument i
            newStr = str(sys.argv[i].upper())  # make it upper case
            word = len(sys.argv[i])
        else:  # if the func was sent from romanamor.py then I take the value that was sent
            newStr = str(x)
            newStr.upper()  # make it upper case
            p = 0
            word = 0
            for p in str(x):  # to get how many characters are in the value sent
                word += 1
        j = 0
        num = 0
        for j in range(word):  # the range is the number of characters in the command line argument or value passed in
            if newStr.startswith('M', j, j + 1):  # if character j is M then
                if not newStr.startswith('C', j - 1, j):  # if character j-1 != C then
                    num += 1000  # num is going to be the final number
                    j += 1  # for iteration
            elif newStr.startswith('C', j, j + 1) and newStr.startswith('M', j + 1, j + 2):  # if char j=C and j+1=M
                num += 900
                j += 2  # iterates twice since I go through two characters
            elif newStr.startswith('D', j, j + 1):
                if not newStr.startswith('C', j - 1, j):
                    num += 500
                    j += 1
            elif newStr.startswith('C', j, j + 1) and newStr.startswith('D', j + 1, j + 2):
                num += 400
                j += 2
            elif newStr.startswith('C', j, j + 1):
                if not newStr.startswith('X', j - 1, j):
                    num += 100
                    j += 1
            elif newStr.startswith('X', j, j + 1) and newStr.startswith('C', j + 1, j + 2):
                num += 90
                j += 2
            elif newStr.startswith('L', j, j + 1):
                if not newStr.startswith('X', j - 1, j):
                    num += 50
                    j += 1
            elif newStr.startswith('X', j, j + 1) and newStr.startswith('L', j + 1, j + 2):
                num += 40
                j += 2
            elif newStr.startswith('X', j, j + 1):
                if not newStr.startswith('I', j - 1, j):
                    num += 10
                    j += 1
            elif newStr.startswith('I', j, j + 1) and newStr.startswith('X', j + 1, j + 2):
                num += 9
                j += 2
            elif newStr.startswith('V', j, j + 1):
                if not newStr.startswith('I', j - 1, j):
                    num += 5
                    j += 1
            elif newStr.startswith('I', j, j + 1) and newStr.startswith('V', j + 1, j + 2):
                num += 4
                j += 2
            elif newStr.startswith('I', j, j + 1):
                num += 1
                j += 1
        else:  # Once the for loop finishes, I use else to print the number only if input was from command line argument
            if x == 'Ry':
                if 4000 <= num or num <= 0:  # If outside boundaries, make the number 0
                    print(newStr + " is 0")
                else:
                    print(str(newStr) + " is " + str(num))
    return num  # returns num when called by romanamor.py


r = 'Ry'
namorFunc(r)  # call namorFunc
