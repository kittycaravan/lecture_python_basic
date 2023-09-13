"""

문자열은 따옴표 (single quotes, double quotes, triple quotes)로 감싸서 생성할 수 있습니다.				
	"Quotes"는 "쿼츠"로 발음			
문자열은 시퀀스 자료형이므로, 인덱싱과 슬라이싱이 가능합니다. 				
인덱싱은 문자열에서 특정 위치에 있는 문자를 가져오는 것을 말하며, 인덱스는 0부터 시작합니다. 				
슬라이싱은 문자열에서 일부분을 잘라내는 것을 말하며, 콜론 (:)을 사용하여 시작 인덱스와 끝 인덱스를 지정합니다.				
				
"""

message = 'Hello, world!'
print(message[0:5])  # 'Hello'


'''

triple quotes				
	triple quotes는 파이썬에서 문자열을 여러 줄에 걸쳐 작성할 때 유용합니다. 			
	triple quotes는 세 개의 따옴표(""") 또는 작은따옴표(' * 3개)를 사용하여 문자열을 감싸며, 여러 줄에 걸쳐 작성할 수 있습니다.			
	예를 들어, 다음과 같이 triple quotes를 사용하여 여러 줄의 문자열을 작성할 수 있습니다.			
				

				
	위 예제에서 message 변수에는 네 줄에 걸쳐 			
		"Hello,", "World!", "This is a", "multi-line", "string." 문자열이 저장됩니다.		
	이렇게 여러 줄의 문자열을 한 번에 작성하면 코드의 가독성을 높이고, 			
		여러 줄에 걸쳐 작성하는 불편함을 줄일 수 있습니다.		

'''

message = """Hello,			
World!			
This is a			
multi-line			
string."""			

print(message)