import json

# JSON 데이터를 파일에서 읽어오기 (예시)
with open('path', 'r') as file:
    data = json.load(file)

# JSON 데이터를 보기 좋게 출력
pretty_json = json.dumps(data, indent=4)

# 출력
print(pretty_json)

# 또는 파일로 저장할 경우:
with open('path', 'w') as file:
    file.write(pretty_json)
