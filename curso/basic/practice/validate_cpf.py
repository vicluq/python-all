def formula(num):
    result1 = 11 - (num % 11)
    digit = 0 if (result1 > 9) else result1
    return digit

