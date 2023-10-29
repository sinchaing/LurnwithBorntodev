def vatCalcurate(totalprice):
    result = totalprice * 1.07
    return result
price = int(input("Enter price : "))
print("Total Inc. VAT = ", vatCalcurate(price))
