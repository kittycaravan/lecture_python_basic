"""
파이썬에서 사전(dictionary)은 키(key)와 값(value)으로 이루어진 자료형입니다. 	
사전은 변경 가능한(mutable) 자료형이며, 중괄호({})를 사용하여 생성할 수 있습니다.	
	json 과 같음
"""

#예를 들어, 다음과 같이 사전을 생성할 수 있습니다.
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}

#위 예제에서는 'apple', 'banana', 'orange'가 각각의 키이고, 1, 2, 3이 각각의 값입니다.

#사전에서는 키를 사용하여 값을 조회할 수 있습니다.
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict['apple'])    # 1
print(my_dict['orange'])   # 3

#사전은 중복된 키를 가질 수 없으며, 중복된 키를 사용하면 나중에 입력된 값이 유지됩니다.
my_dict = {'apple': 1, 'banana': 2, 'apple': 3}
print(my_dict)   # {'apple': 3, 'banana': 2}

#사전에 새로운 키-값 쌍을 추가하려면, 새로운 키를 사용하여 값을 할당하면 됩니다.
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
my_dict['melon'] = 4
print(my_dict)   # {'apple': 1, 'banana': 2, 'orange': 3, 'melon': 4}

#사전에서는 keys(), values(), items() 등의 메서드를 사용하여 키, 값, 키-값 쌍을 조회할 수 있습니다.
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
print(my_dict.keys())    # dict_keys(['apple', 'banana', 'orange'])
print(my_dict.values())  # dict_values([1, 2, 3])
print(my_dict.items())   # dict_items([('apple', 1), ('banana', 2), ('orange', 3)])