expression = input('Expression: ')
x,y,z = expression.split()
x = str(x)
z = str(z)
if y =='+':
    print(x+z)
elif y == '-':
    print(x-z)
elif y =='*':
    print(x*z)
elif y =='/':
    print(x/z)
