
hours = input('Enter Hours: ')
h = float(hours)
rate = input('Enter Rate: ')
r = float(rate)
regpay = r * h
halfpay = r/2
#
 # Overtime pay
if h>40 :
    oth = h - 40
    otp = oth * halfpay
    print(regpay + otp)
#Regular pay   
else :
    print(regpay)
