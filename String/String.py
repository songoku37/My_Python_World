s = "Hello World"

print(s[0])  # 출력 : H
print(s[-1])  # 출력 : d
print(s[1:3])  # 출력 : el
print(s[:])  # 출력 : Hello
print(s[1:])  # 출력 : ello World
print(s[:3])  # 출력 : Hel
print(s[::2])  # 출력 : HloWrd
print(s[::-1])  # 출력 : dlroW olleH
print('Hello' + ' ' + 'World')  # 출력 : Hello World
print('Hello' * 3)  # 출력 : Hello Hello Hello

# s[0] = 'h'  불가능
s = 'h' + s[1:]  # 출력 : hello World

print(len(s))  # 출력 : 11
print(s.upper())  # 출력 : HELLO WORLD
print(s.lower()) # 출력 : hello world
print(s.swapcase()) # 출력 : HELLO wORLD
print(s.capitalize()) # 출력 : Hello world
print(s.title()) # 출력 : Hello World

print(s.endswith('ld'))  # 출력 : True
print(s.endswith('ld',0,26)) # 출력 : False
print(s.startswith('hel'))  # 출력 : True
print(s.startswith('hel',7)) # 출력 : False
print(s.find('World'))  # 출력 : 6
print(s.find('World',3)) # 출력 : 6
print(s.index('World')) # 출력 : 6
print(s.rfind('like')) # 출력 : -1
print(s.count('ld')) # 출력 : 1
print('World' in s)  # 출력 : True

u = ' spam and ham '
s = 'one:two:three:four'
t = u.split()
print(u.split()) # 출력 : ['spam' , 'and' , 'ham']
print(u.split('and')) # 출력 : ['spam' , 'ham']
print(s.split(':',2)) # 출력 : ['one', 'two', 'three:four']
print(u.strip()) # 출력 : spam and ham
print('ㅎㅁㅎㅂ파이썬ㅂㅎㅁ'.strip('ㅎㅁㅂ')) # 출력 : 파이썬
print(s.rsplit(':',1)) # 출력 : ['one:two:three', 'four']
print(u.rstrip()) # 출력 :  spam and ham
print(u.lstrip()) # 출력 : spam and ham
print(u.replace('spam', 'spam, egg')) # 출력 : spam, egg and ham
print(':'.join(t)) # 출력 : spam:and:ham

lines = '''first line
second line
thrid line'''
print(lines.splitlines()) # 출력 : ['first line', 'second line', 'thrid line']

u = 'spam and egg'
print(u.center(20)) # 출력 :     spam and egg
print(u.center(20,'-')) # 출력 : ----spam and egg----
print(u.ljust(20)) # 출력 : spam and egg
print(u.rjust(20)) # 출력 :         spam and egg