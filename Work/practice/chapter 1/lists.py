symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')
print(symlist)
print('symlist[0]',symlist[0])
print('symlist[-1]', symlist[-1])
print('symlist[-2]', symlist[-2])
symlist[2] = 'AIG'
print(symlist)
print(symlist[0:3])
print(symlist[-2:])
mysyms = []
mysyms.append('GOOG')
print('mysyms', mysyms)

# this method resizes list
symlist[-2:] = mysyms
print('symlist', symlist)

#10
for s in symlist:
    print('s=',s)
