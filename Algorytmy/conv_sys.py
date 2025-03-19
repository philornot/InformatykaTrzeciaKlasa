
def BinToDecimal(nu):
    decimal_value = 0
    base = 1
    while (nu):
        last_digit = nu % 10
        nu = nu // 10
        decimal_value += last_digit * base
        base = base * 2
    # print("The decimal value is :",decimal_value)
    return decimal_value




def OctalToDecimal(num):
    decimal_value = 0
    base = 1
    while (num):
        last_digit = num % 10
        num = num // 10
        decimal_value += last_digit * base
        base = base * 8
    # print("The decimal value is :",decimal_value)
    return decimal_value

ol = 1015
dl = OctalToDecimal(ol)

print(ol, dl)

bl = 11111
dbl = BinToDecimal(bl)
print(bl, dbl)

