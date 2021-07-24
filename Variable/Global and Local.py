def A() :
    return
print(A()) # 출력 : None

def B() :
    pass
print(B()) # 출력 : None

a = 20
def f(a):
    a = 10
f(a)
print(a) # 출력 : a = 20

def g(t):
    t[1] = 10
a = [1, 2, 3]
g(a)
print(a) # 출력 : [1, 10, 3]

def gg(t) :
    t = [1, 2, 3]
a = [5, 6, 7]
gg(a)
print(a) # 출력 : [5, 6, 7]