'''
<문제> 문자열 재정렬
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.

이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력


<문제 해결 아이디어>
1. 문자열이 입력되었을 때 문자를 하나씩 확인
	- 숫자인 경우 따로 합계를 계산
	- 알파펫의 경우는 별도의 리스트에 저장
2. 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답
'''

input_data = input()
alphabet = ""
total_sum = 0

for ch in input_data:
	if ch in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
		total_sum += int(ch)
	else:
		alphabet += ch
	
result = list(alphabet).sort()
print(result)
print(alphabet + str(total_sum))