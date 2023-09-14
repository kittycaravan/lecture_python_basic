"""
함수
함수 개념은 같음.

rule.	def 함수이름(매개변수):		
			코드 블록		
			return 반환값		

"""
def get_cat():
	return '괭이'

print(get_cat())


#예문으로 설명

## 함수	
	
# 리턴 있는 함수	
print("==== 리턴 있는 함수 ====")
def get_cat():	
	return '괭이'	
	
print(get_cat())    #함수 호출	
	
# 리턴 없는 함수	
print("==== 리턴 없는 함수 ====")
def x():	
	print('x')	
	
x() # 함수 호출	
	
# 리턴 값 없는 리턴이 있는 함수	
print("==== 리턴 값 없는 리턴이 있는 함수 ====")
def y():	
	print('y')	
	return	

y() # 함수 호출	
	
# 매개변수 있고 리턴이 있는 함수	
print("==== 매개변수 있고 리턴이 있는 함수 ====")
def add(a,b):	
	return a+b	
	
print(add(10,20))	
