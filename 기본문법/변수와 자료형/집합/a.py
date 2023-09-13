"""
파이썬에서 집합(set)은 중복되지 않는(unique) 요소들로 이루어진 컬렉션입니다. 
집합은 순서가 없는(unordered) 자료형이므로, 인덱싱을 지원하지 않습니다.
"""

#집합은 중괄호({})를 사용하여 생성하며, 각 요소는 쉼표(,)로 구분됩니다.
#예를 들어, 다음과 같이 집합을 생성할 수 있습니다.
my_set = {1, 2, 3}

#집합은 중복되지 않는 값을 가지므로, 중복된 값은 자동으로 제거됩니다.
my_set = {1, 2, 3, 1, 2}
print(my_set)   # {1, 2, 3}

# 집합은 수학적인 집합과 유사한 연산을 지원합니다. 
# 예를 들어, 교집합, 합집합, 차집합 등의 연산이 가능합니다.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))   # {3, 4}
print(set1.union(set2))          # {1, 2, 3, 4, 5, 6}
print(set1.difference(set2))     # {1, 2}


# 집합은 변경 가능한(mutable) 자료형이며, add(), update(), remove() 등의 	
# 	메서드를 사용하여 요소를 추가, 삭제, 갱신할 수 있습니다.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)   # {1, 2, 3, 4}

my_set.update({2, 3, 5})
print(my_set)   # {1, 2, 3, 4, 5}

my_set.remove(4)
print(my_set)   # {1, 2, 3, 5}