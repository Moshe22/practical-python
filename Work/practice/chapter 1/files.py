#1.26 file preliminaries
with open('../../Data/portfolio.csv', 'rt') as f: # rt = read 
    data = f.read()
print(data)

#with for loop to read by line
print('read with for loop')
with open('../../Data/portfolio.csv', 'rt') as f: # rt = read 
    for line in f:
        print(line, end='')
    data = f.read()
print(data)

# using next() and split
print('using next and split')
f = open('../../Data/portfolio.csv','rt')
headers = next(f).split(',')
print('headers =',headers)

for line in f:
    row =line.split(',')
    print(row)
f.close()
