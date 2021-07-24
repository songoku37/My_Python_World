t = (1, 2, 3)
print(t[0]) # 출력 : 1
print(t[-1]) # 출력 : 3
print(t[0:2]) # 출력 : (1, 2)
print(t[::2]) # 출력 : (1, 3)
print(t + t + t) # 출력 : (1, 2 , 3, 1, 2, 3, 1, 2, 3)
print(t * 3) # 출력 : (1, 2 , 3, 1, 2, 3, 1, 2, 3)

a, *b, c = (1, 2, 3, 4)
print(a, b, c) # 출력 : a = 1 , b = (2, 3) , c = 4
data = 1, 2, 3, 4
print(data) # 출력 : data = (1, 2, 3, 4)
a, b, c, d = 'jhon'
print(a, b, c, d) # 출력 : a = j , b = h , c = o  , d = n

# t[10] = 100 # 에러

t = (1, 2, 3, 2, 2, 3)
print(t.count(2)) # 출력 : 3
print(t.index(2)) # 출력 : 1
print(t.index(2 , 1)) # 출력 : 1
print(len(t)) # 출력 : 3
print(3 in t) # 출력 : True

u = t , (1, 2, 3)
print(u) # 출력 : ((1, 2, 3, 2, 2, 3), (1, 2, 3))

x, y = 1, 2
x, y = y, x
print(x, y) # 출력 : 2 1

t = 1, 2 , 'hello' # 출력 : (1, 2, 'hello')
a , *b = t # 출력 : a = 1 , b = [2 , 'hello']
print(a, b)

