A = 1234567
B = 1234.56789

print(format(B,'.2f')) # 출력 : 1234.57
print(format(A,',d')) # 출력 : 1,234,567
print(format(B,',.2f')) # 출력 : 1,234.57

print('{} {}'.format(23, 2.12345)) # 출력 : 23 2.12345
L = [1, 5, 4, 2, 3]
print('최댓값:{0}, 최솟값:{1}'.format(max(L),min(L))) # 출력 : 최댓값:5, 최솟값:1

L = [0, 1, 2, 3, 5, 8]
print('{0[4]} is {0[5]}'.format(L)) # 출력 : 5 is 8

print('나이:{age} 키 :{height}'.format(age = 49 , height = 173)) # 출력 : 나이 : 49 키 : 173