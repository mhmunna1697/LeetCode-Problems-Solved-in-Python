def plusOne(digits):

    for i in range(len(digits)-1, -1, -1):
        if digits[i]<9:
            digits[i]=digits[i]+1
            return digits
        else:
            digits[i]=0

    return [1]+digits


digits=[9, 9]
print (plusOne(digits))