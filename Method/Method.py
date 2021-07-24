def add (a,b):
    return a + b

print(add(3,4)) # 출력 : 7
print(add([1,2,3],[4,5,6])) # 출력 : [1, 2, 3, 4, 5, 6]
print(add(a = 10 , b = 5)) # 출력 : 15

def plus (a , b = 1 ) :
    return a + b

print(plus(3)) # 출력 : 4
print(plus(4,5)) # 출력 : 9

def area(h , w) :
    return h * w

print(area(w = 20 , h = 10)) # 출력 : 200
print(area(20,w = 5)) # 출력 : 100
# print(area(h = 5 , 20)) # 인수 이후 값이 나오면 에러













