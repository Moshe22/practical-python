symbols = 'APPL,IBM,MSFT,YHOO,SCOO'
print(symbols[0])
print(symbols[1])
print(symbols[2])
print(symbols[-1])
print(symbols[-2])
symbols = symbols + ',GOOG'
print(symbols)
symbols = 'HPQ,' + symbols
print(symbols)

# 1.15
print('IBM' in symbols)

print('AA' in symbols)
print('CAT' in symbols)

#1.18 use fstrings for output on 1.10 (mortgage.py)
