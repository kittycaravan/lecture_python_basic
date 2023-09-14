"""
### 패키지
    파이썬에서 패키지(package)는 모듈을 더욱 체계적으로 관리하기 위한 방법입니다. 
    패키지는 모듈의 계층적인 구조를 정의하며, 관련된 모듈을 모아서 하나의 패키지로 묶어서 관리할 수 있습니다.


    패키지는 디렉토리 구조로 표현되며, 패키지 내부에는 __init__.py 파일이 있어야 합니다. 		
    __init__.py 파일은 해당 디렉토리가 패키지임을 나타내는 파일입니다. 		
            << 언더바 _ _ 2개임 뒤에도 2 개
            << 만들고 아무 코딩 안해도 되긴 함.
    이 파일에는 패키지를 사용하는 데 필요한 초기화 코드를 작성할 수 있습니다.		

"""


# import package_cat.cat

# print(package_cat.cat.name)
# package_cat.cat.cat()

### 가져온 변수,함수, 클래스를 줄여쓰는 방법
# 이렇게 하면 앞에 패키지.모듈. 안하고 바로 쓸 수 있게 됨

import package_cat.cat
from package_cat.cat import name
from package_cat.cat import cat

print(name)
cat()