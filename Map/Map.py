
def f(x):
    return x * x

X = [1,2,3,4,5]

list(map(f,X)) # 출력 : [1,4,9,16,25]

Y =  list(map(lambda a : a * a, X))  # 출력 : 출력 : [1,4,9,16,25]

P = [1,2,3,4,5]
Q = [6,7,8,9,10]

Z = list(map(lambda x , y : x + y ,P, Q)) # 출력 : [7,9,11,13,15]


# ------------------- filter ---------------------------

f = filter(lambda x : x + 2 , [1,2,3,4])
print(list (f)) # 출력 : [1 ,2 ,3 ,4]



