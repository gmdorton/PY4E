
def computepay(h, r):
    if h>40 :
        oth = h - 40
        otp = oth * halfpay
        return regpay + otp
    else :
        return regpay

hours = input('Enter Hours: ')
h = float(hours)

rate = input('Enter Rate: ')
r = float(rate)

regpay = r * h
halfpay = r/2

p = computepay(h, r)
print("Pay", p)
