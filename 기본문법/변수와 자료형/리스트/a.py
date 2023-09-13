#빈 리스트 생성
my_list = []

#정수형 요소를 가진 리스트 생성
my_list = [1, 2, 3, 4, 5]

#문자열 요소를 가진 리스트 생성
my_list = ["apple", "banana", "cherry"]

#서로 다른 자료형의 요소를 가진 리스트 생성
my_list = [1, "apple", True, 3.14]

#리스트에 접근
my_list[0]

#리스트에 값 추가
my_list.append(6)

#리스트의 요소 개수를 반환
#len()
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # 5

#리스트의 끝에 다른 리스트를 연결하여 확장
#extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # [1, 2, 3, 4, 5]

#지정된 위치에 새로운 요소를 삽입
#insert()
my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # [1, 4, 2, 3]

#지정된 값을 가진 첫 번째 요소를 삭제
#remove()
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # [1, 2, 4, 5]

#리스트의 마지막 요소를 반환하고 삭제
#pop()
my_list = [1, 2, 3, 4, 5]
last_element = my_list.pop()
print(last_element)  # 5
print(my_list)  # [1, 2, 3, 4]

#지정된 값을 가진 첫 번째 요소의 인덱스를 반환
#index()
my_list = [1, 2, 3, 4, 5]
index = my_list.index(3)
print(index)  # 2

#지정된 값을 가진 요소의 개수를 반환
#count()
my_list = [1, 2, 3, 2, 4, 2, 5]
count = my_list.count(2)
print(count)  # 3

#리스트를 오름차순으로 정렬
#sort()
my_list = [5, 3, 1, 4, 2]
my_list.sort()
print(my_list)  # [1, 2, 3, 4, 5]

#리스트의 요소 순서를 뒤집기
#reverse()
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # [5, 4, 3, 2, 1]
