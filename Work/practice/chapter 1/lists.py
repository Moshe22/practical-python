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
print('AIG' in symlist)

#1.22
symlist.append('RHT')
print('1.22', symlist)

#1.22 insert
symlist.insert(1, 'AA')
print('1.22 insert', symlist)

#1.22 remove
symlist.remove('MSFT')
print('1.22 remove', symlist)

#1.22 append at end
symlist.append('YHOO')
print('1.22 append at end', symlist)
print('index of first YHOO', symlist.index('YHOO'))
print('number of YHOO', symlist.count('YHOO'))
symlist.remove('YHOO')
symlist.sort()
print('sorted',symlist)

symlist.sort(reverse=True)
print('reverse sorted', symlist)

#1.24 joining
a=','.join(symlist)
b=':'.join(symlist)
c=''.join(symlist)
print('comma join',a)
print('colon join',b)
print('no space join',c)
