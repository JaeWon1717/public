## 앞에서 2600개를 제외한 나머지 파일을 삭제
import os

# 사진이 들어있는 폴더 경로
folder_path = "path"

# 파일 목록을 가져와 정렬
all_files = sorted(os.listdir(folder_path))


for file_name in all_files[2600:]:
    file_path = os.path.join(folder_path, file_name)
    
    # 파일이 실제로 있는지 확인 후 삭제
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")

print("Deletion completed.")
