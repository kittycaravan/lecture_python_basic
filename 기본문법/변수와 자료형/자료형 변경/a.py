"""
자료형 변경	
	Python에서는 변수의 자료형을 변경할 수도 있습니다. 
	이것을 "타입 캐스팅(type casting)"이라고 합니다. 
"""

a = 10      # a는 정수형
b = float(a)  # b는 실수형으로 변환
c = str(a)    # c는 문자열로 변환

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>