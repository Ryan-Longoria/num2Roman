from namor import namorFunc  # import both files and functions
from roman import romanFunc

# I wanted to try out a dictionary (:
romanDict = {"M": 1000
    , "CM": 900
    , "D": 500
    , "CD": 400
    , "C": 100
    , "XC": 90
    , "L": 50
    , "XL": 40
    , "X": 10
    , "IX": 9
    , "V": 5
    , "IV": 4
    , "I": 1}


def check(errors):  # passing in errors for no real reason
    i = 1
    for i in range(0, 4001):  # range is from 0-4001
        a = romanFunc(i)  # send number returns string
        j = i  # so that I don't have to change i
        temp = ''  # reset temp
        while j != 0:
            if j - romanDict["M"] >= 0:  # if j - 1000 does not go below 0 then
                temp += 'M'  # add character to temp
                j -= romanDict["M"]  # subtract 1000 from j
            elif j - romanDict["CM"] >= 0:
                temp += 'CM'
                j -= romanDict["CM"]
            elif j - romanDict["D"] >= 0:
                temp += 'D'
                j -= romanDict["D"]
            elif j - romanDict["CD"] >= 0:
                temp += 'CD'
                j -= romanDict["CD"]
            elif j - romanDict["C"] >= 0:
                temp += 'C'
                j -= romanDict["C"]
            elif j - romanDict["XC"] >= 0:
                temp += 'XC'
                j -= romanDict["XC"]
            elif j - romanDict["L"] >= 0:
                temp += 'L'
                j -= romanDict["L"]
            elif j - romanDict["XL"] >= 0:
                temp += 'XL'
                j -= romanDict["XL"]
            elif j - romanDict["X"] >= 0:
                temp += 'X'
                j -= romanDict["X"]
            elif j - romanDict["IX"] >= 0:
                temp += 'IX'
                j -= romanDict["IX"]
            elif j - romanDict["V"] >= 0:
                temp += 'V'
                j -= romanDict["V"]
            elif j - romanDict["IV"] >= 0:
                temp += 'IV'
                j -= romanDict["IV"]
            elif j - romanDict["I"] >= 0:
                temp += 'I'
                j -= romanDict["I"]

        b = namorFunc(temp)  # send string returns number
        if b >= 4000:  # if number exceeds 4000 print error message
            errors += 1
            print("Converted " + str(b) + " to Error back to 0, which is wrong.")
        num = i  # so I don't have to change i
        sum = 0  # reset sum
        roman = ''  # reset roman
        while num > 0:
            if num - 1000 >= 0:  # I just realized I could have used dictionary here after I finished ):
                num -= 1000  # too tired to change it now
                sum += 1000
                roman += 'M'  # add character to roman
            elif num - 900 >= 0:
                num -= 900
                sum += 900
                roman += 'CM'
            elif num - 500 >= 0:
                num -= 500
                sum += 500
                roman += 'D'
            elif num - 400 >= 0:
                num -= 400
                sum += 400
                roman += 'CD'
            elif num - 100 >= 0:
                num -= 100
                sum += 100
                roman += 'C'
            elif num - 90 >= 0:
                num -= 90
                sum += 90
                roman += 'XC'
            elif num - 50 >= 0:
                num -= 50
                sum += 50
                roman += 'L'
            elif num - 40 >= 0:
                num -= 40
                sum += 40
                roman += 'XL'
            elif num - 10 >= 0:
                num -= 10
                sum += 10
                roman += 'X'
            elif num - 9 >= 0:
                num -= 9
                sum += 9
                roman += 'IX'
            elif num - 5 >= 0:
                num -= 5
                sum += 5
                roman += 'V'
            elif num - 4 >= 0:
                num -= 4
                sum += 4
                roman += 'IV'
            elif num - 1 >= 0:
                num -= 1
                sum += 1
                roman += 'I'
        else:  # I use else once while loop is completed and try to find errors by comparing a and b
            if roman != a:  # this is to check if function a worked (I think this was kind of useless)
                if sum != b:  # sum is equal to a in number
                    if temp != a:  # temp is equal to b in roman
                        errors += 1
        i += 1  # increment i
    else:  # Else is used to display how many errors there were once for loop is completed
        print("Checked values from 0 to 4000. Errors = " + str(errors) + ".")


e = 0
check(e)  # call the function
