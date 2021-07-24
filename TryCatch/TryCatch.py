name = 'nontxet'

try :
    f = open(name,'r')
except ZeroDivisionError as x :
    print(x)
finally :
    print("You can nothing")
    f.close()