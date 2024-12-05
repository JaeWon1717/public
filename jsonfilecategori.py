import json

# JSON 데이터 파일 열기
with open('path', 'r') as file:
    data = json.load(file)

# 제거할 image_id 목록 (문제에서 주어진 대로 리스트로 작성)
remove_image_ids = [
    543, 544, 545, 586, 587, 595, 596, 597, 598, 599, 600, 657, 664, 665, 666, 735, 736, 737, 738, 857, 866
]


# annotations에서 image_id가 remove_image_ids 목록에 포함된 항목 제거
filtered_annotations = [item for item in data['annotations'] if item["image_id"] not in remove_image_ids]

# 제거된 항목이 반영된 새로운 JSON 데이터 생성
filtered_data = {
    "images": data['images'],  
    "annotations": filtered_annotations,
    "categories": data['categories']
}


pretty_json = json.dumps(filtered_data, indent=4)
print(pretty_json)

with open('filtered_data.json', 'w') as f:
    f.write(pretty_json)
