import decimal

d = decimal.Decimal('00.26598')
print("Original Number : ",d)
for i in range(1, 5):
    decimal.getcontext().prec = i
    print("Precision-",i, ':', d * 1)