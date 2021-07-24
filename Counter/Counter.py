# 본 프로그램은 텍스트 데이터를 빈도 분석하기 전 기초편입니다.
# 작성자 이성재
# 프로그램 wc_base02.py
# import 와 from의 차이를 구분해서 사용할 수 있게한다.
# Counter를 사용하면 출력 결과는 Dictionary 형태로 반환하여 준다.

from collections import Counter
import collections

List = ['aa','dd','cc','aa','bb','ee']

# from collections import Counter 을 사용 했을 때
dict1 = Counter(List)
print (dict1)
# 출력 : Counter({'aa': 2, 'dd': 1, 'cc': 1, 'bb': 1, 'ee': 1})

# most_common() 은 딕셔너리 형태를 배열로 변환
dict1_arry = dict1.most_common() # most_common() 배열로 변환하는 함수
print(dict1_arry)
# 출력 : [('aa', 2), ('dd', 1), ('cc', 1), ('bb', 1), ('ee', 1)]

# dict함수는 배열형태로 되어있는 딕셔너리형 데이터를 다시 딕셔너리형으로 변경
new_dict1 = dict(dict1_arry) # dict 배열형태로 변환
print(new_dict1)
# 출력 : {'aa': 2, 'dd': 1, 'cc': 1, 'bb': 1, 'ee': 1}