"""

연산자


연산자의 우선순위는 수학 연산과 동일하며, 		
	필요에 따라 괄호를 사용하여 연산 우선순위를 변경할 수 있습니다.	

"""


'''

    수치 연산자							
	수치 연산자는 수치형 데이터 타입(정수, 실수, 복소수 등)에 적용되는 연산자입니다. 						
	연산자	설명	연산자	설명	연산자	설명	
	+	덧셈	/	나눗셈	//	몫	
	-	뺄셈	%	나머지	**	거듭제곱	
	*	곱셈					

'''

print(10 ** 3)  #1000
print(10 // 3)  #3

'''
    논리 연산자									
	논리 연산자는 불리언(bool) 데이터 타입에 적용되는 연산자입니다.								
	연산자	설명		연산자	설명		연산자	설명	
	and	논리곱(AND)		or	논리합(OR)		not	논리부정(NOT)	

'''

# and

x = True
y = False

result = x and y
print(result)  # False를 출력합니다.


# or

x = True
y = False

result = x or y
print(result)  # True를 출력합니다.


# not

x = True

result = not x
print(result)  # False를 출력합니다.


age = 25
is_student = True

# 나이가 18 이상이고 학생인 경우에만 특별 할인을 적용합니다.
if age >= 18 and is_student:
    print("특별 할인을 적용합니다.")
else:
    print("할인을 적용하지 않습니다.")


'''
    비교 연산자								
	비교 연산자는 서로 다른 데이터 타입에 적용되는 연산자입니다. 							
	연산자	설명			연산자	설명		
	==	같음			<	작음		
	!=	다름			<=	작거나 같음		
	>	큼			is	같은 객체인지 확인		
	>=	크거나 같음			is not	같은 객체가 아닌지 확인		
'''

x = 15
y = 10
z = 20

result = (x > y) and (x < z)  # True, x는 y보다 크고 z보다 작습니다.

print(result)