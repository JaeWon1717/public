import os

# 이미지가 저장된 디렉토리 경로
directory = "/Users/jaewon/Desktop/Taskfolder/labeling_opencv/chunk_3"

# 폴더 내 파일 개수를 카운트
file_count = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

print(f"Total number of files in the directory: {file_count}")
