octal_1 = input('enter the first octal number:')
octal_2 = input('enter the second octal number:')
result = int(octal_1, 8) // int(octal_2, 8)
reminder = int(octal_1, 8) % int(octal_2, 8)
f_result = oct(result)
print("{r} R {m}".format(r=f_result, m=reminder))