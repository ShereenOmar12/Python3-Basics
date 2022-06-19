

#print multiplication table from 1 to 5
for m in range(1,6):
    for x in range(1,11):
        print(f'{m}x{x}={m*x}')

    print('---------')    



#print number and squar
start=int(input('Enter start number'))
end=int(input('Enter end number'))
print('Number \t squar')
print('------------------')
for x in range(start,end+1):
    print(x,'\t',x*x)
print('----------')


#loop in 1line
x=0
while(x<10): print(x);x+=1
print('--------')



#insted while loop
x=0
while(x<3):
    y=0

    while(y<6):
        print(y)
        y+=1
    print(x)
    x+=1
print('---------')
    



#print range item
print(list(range(10)))

print('--------')




#insted for
for x in range(5):
    for y in range(3):
        print(x,y)

print('---------')


#break
for x in range(10):
    if(x==6):
        break
    print(x)


#continue
for x in range(10):
    if(x==6):
        continue
    print(x)












