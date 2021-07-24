# ------------------ 파일 입력하기 ------------------

s = """
Hello World!
"""

f = open('t.txt', 'w')
print(f.write(s))  # 출력 : 14
f.close()

with open('t1.txt', 'w') as f:
    f.write('위대한 세종대왕')


lines = ['first line\n', 'second line\n', 'third line\n']
f = open('t3.txt', 'w')
f.writelines(lines)


with open('t3.txt') as f:
    for line in f:
        print(line, end='')

"""
출력 : 
first line
second line
third line
"""

# ------------------ 파일 내용 출력 ------------------

f = open('t.txt')
s = f.read()
print(s)  # 출력 : Hello World!
f.close()

print(open('t.txt').read())  # 출력 : Hello World!

with open('t.txt') as f:
    print(f.read())  # 출력 : Hello World!


# ------------------ 이어적기 ------------------


f = open('remove.txt', 'w')
f.write('first line\n')

f.write('second line\n')
f.close()

f = open('remove.txt', 'a')
f.write('third line\n')
f.close()

f = open('remove.txt')
print(f.read())
f.close()

"""
출력 : 
first line
second line
third line
"""