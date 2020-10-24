## 파이썬 코테용 문법 ( ver. 2020.10.24)

### 1. 입력 변수 편하게 여러개 받기(int, map 이용)

```python
# 리스트로 받는 방법
var_list = list(map(int, input.split(' ')))

# 특정 변수의 개수만큼 받는 방법
m, n, o, p = map(int, input.split(' '))
```



### 2. 자르기(Slicing) 

- Python이 다른 언어와 차별되는 강점으로 string을 list로 표현 가능
- 범위를 이용해서 다양한 테크닉 이용 가능

```python
# 문자열 변수 선언
moonjayeol = "oh coding test neomoo euryeopgo TT"

# 홀수 위치에 있는 문자만 출력
# 배열 범위 선언 뜻 -> 인덱스 0부터 2칸씩 띄워서 출력해~
print(moonjayeol[0::2])

# 짝수 위치에 있는 문자만 출력
# 배열 범위 선언 뜻 -> 인덱스 1부터 2칸씩 띄워서 출력해~
print(moonjayeol[1::2])

# 거꾸로 출력
# 배열 범위 선언 뜻 -> 모든 인덱스 다 출력 하는데, 역순으로 출력해
print(moonjayeol[::-1])
```



### 3. 문자 정합성 검증 함수들

```python
kor_str = "나는 한국말 쓸줄 알아"
eng_str = "I can speak english"
num_str = "12340983"
# id 검증할때, 알파벳 + 숫자로 구성하세요~ 검증할때 좋은 함수 알려드림
id_str = "create54"

# 변수가 알파벳으로만 이루어져있는지 검증 -> is this string consisted of aplhabet -> isalpha()
print(kor_str.isalpha())	 # False
print(eng_str.isalpha())	 # True
print(num_str.isalpha())	 # False

# 변수가 알파벳 + 숫자로만 이루어져있는지 검증 -> is this string consisted of aplhabet and number? -> isalnum()
print(kor_str.isalnum())	 # False
print(eng_str.isalnum())	 # True
print(num_str.isalnum())	 # True
print(id_str.isalnunm())	 # True

# 문자열을 이루고 있는 알파벳이 모두 대, 소문자인지 검사
# 알파벳 이외의 문자는 검사 대상에서 알아서 제외
print(eng_str.islower())
print("KOREA".islower())
print(eng_str.isupper())
print("KOREA".isupper())
```



### 4. 숫자 정합성 검증 함수들

```python
# 문자열이 숫자인지 확인
num_str = "123456"
print(num_str.isnumeric())	# True
print("123456".isnumeric())	# True

# 추가적으로 isdecimal(), isdigit() 가 있는데, 이는 특수문자, 로마숫자의 경우 리턴값이 다르므로, 가장 정확하게 판별 가능한 isnumeric()만 기억
```



### 5. 문자열 대,소문자 변환

```python
# 대문자로 변경
print("string".upper())

# 소문자로 변경
print("STRING".lower())

# 첫 글자만 대문자로 변경
print("i like korean food".capitalize())
```



### 6. 문자열 내 포함여부 검색 및 검사

```python
# 문자열 변수 선언
eng_str = "My name is Ukgi Baek"

# 포함여부 검사
print("n" in eng_str) 	# True

# n이 처음 위치하고 있는 인덱스 출력
print(eng_str.index("n"))
print(eng_str.find("n"))

# 같은 문자가 2개 이상이면 첫 번째 위치만 반환
# 첫 번째 위치에 +1 이후 위치를 검색하면 다음 위치 검색 가능
print(eng_str.index("n"))	# 4
print(eng_str.find("n"))	# 4

print(eng_str.index("n", 4 ))	
print(eng_str.find("n", 4))	

# 해당 문자열 포함 개수 출력 시 -> count() 이용
print(eng_str.count("i"))	# 2

# index, find는 return 값이 달라서, 다른 함수임
# find는 없으면 -1 반환, index는 없으면 '에러' 발생
# find 쓰자
```



### 7. 문자열 trim

```python
# database에서는 trim으로 알려진 파이썬 함수는 strip
untrimed_str = "     gongbakm oonja      "

# 왼쪽 공백 제거
print(untrimed_str.lstrip())

# 오른쪽 공백 제거
print(untrimed_str.rstrip())

# 양쪽 공백 제거
# 이 경우는 중간의 공백은 제거 X
print(untrimed_str.strip())

# 전체 공백을 제거하고 싶으면 replace를 쓰자
print(untrimed_str.replace(" ", ""))
```



### 8. Dictionary 분리해서 list 로 출력

```python
dict = {"a" : 1,
       	"b" : 2,
        "c" : 3
       }

# key값 추출하여 리스트로 변환
print(list(dict))	# ["a", "b", "c"]
print(list(dict.keys())	# type이 dict_keys라는 객체이므로 연산 불가능 -> list 씌워야 함
      
# value 값만 list로 변환
print(list(dict.value()))	# type이 dict_values라는 객체이므로 연산 불가능 -> list 씌워야 함
      
# key, value 모두 뽑아내기
print(dict.items())

```



### 9. List -> Dictionary 만들기 (Enumerate)

```python
a = ["a", "b", "c"]
b = [1, 2, 3]
dict = {}

for index, v in enumerate(a):
  dict[v] = b[index]

print(dict)
```



### 10. List Comprehension

```python
# for 문 이용해서 리스트 변수 초기화
a = [0 for _ in range(10)]
a = [0] * 10

# 정수 0으로 채워진 10 * 10 이차원 배열 생성
a = [[0] * 10 for _ in range(5)]

# 짝수만 거르기
b = [v for v in a if v % 2 == 0]
print(b)
```



### 11. Lambda

```python
# 람다 선언 직후 사용
# lambda 사용할매개변수 ,로 나열: 함수
print((lambda x, y, z: x + y + z)(1, 2, 3))

# 람다 리스트에 넣어서 사용 가능
lambdas = [lambda x:x+10, lambda x:x+100]
print(lambda[0](5))	# 15
print(lambda[1](5))	# 105

# 람다 함수로 딕셔너리 정렬 방법
alphabets = {"a" : 5, "b" : 9, "e" : 7, "d" : 3, "c" : 2}

sorted_by_key = sorted(alphabets.items(), key = lambda x:x[0])
sorted_by_value = sorted(alphabets.items(), key = lambda x:x[1])

print(sorted_by_key)
print(sorted_by_value)
```



### 



