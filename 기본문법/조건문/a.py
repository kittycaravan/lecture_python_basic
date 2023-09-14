"""
파이썬도 조건문과 반복문이 있고 다른언어의 룰(80%정도 비슷)과 내용이 같음.
"""

'''

if 문	
rule.	if 조건: 코드 블록	
'''

if 2<11: print("야옹")

'''
			
if , else	
	java의 if else 와 내용은 같음		
	rule.	if 조건: 코드 블록	
    		else 조건: 코드 블록	
'''
if 2>11: print("야옹")
else: print("멍")


'''
                        
elif 조건:	
    else if 를 줄여 elif 라는 키워드로 씀. 내용은 같음.		
	rule.	if 조건: 코드 블록	
			elif 조건: 코드 블록	
'''
if 2>11: print("야옹")
elif 2<5: print("멍")


'''

                        
if elif else		if , else if , else 같은 내용임. 표기만 주의.	
	rule.	if 조건: 코드 블록	
		elif 조건: 코드 블록	
		else : 코드 블록	
			
'''
s = "개"
if s=="고양이": print("괭")
elif s=="개": print("개")
elif s=="토끼": print("토")
else : print("x")



'''

        			
switch 문은 없음		if elif else 로 커버	
			
'''