a = ['cat', 'cow', 'tiger']
for x in a:
    print(len(x), x)


''' 
출력 :
3 cat
3 cow
6 tigter 
'''

for x in 'abcdef':
    print(x, ord(x))

'''
출력 :
a 97
b 98
c 99
d 100
e 101
f 102
'''

for x in range(10):  # 0 1 2 3 4 5 6 7 8 9
    print(x)

L = ['cat', 'dog', 'bird', 'pig']
for k, animal in enumerate(L):
    print(k, animal)

""" 
출력 :
0 cat
1 dog
2 bird
3 pig
"""
