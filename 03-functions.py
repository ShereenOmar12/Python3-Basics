def mysum(x,y):
    result=x+y
    return result



m=mysum(3,4)
print(m*2)

#anonymous function
#mysum is function
mysum=lambda x,y : x+y
print(mysum(2,2))



#lambda function with calling in one line
#mysum is variable
result=(lambda x,y:x+y)(3,3)
print(result)

#variable in function is local can not be use out function scope without determin it as global variable

f=0
print(f)
def do():
    global f
    f=5
    print(f)

do()
print(f)
