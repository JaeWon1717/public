import cv2

# 동영상 파일 경로 (파일명과 경로는 실제 파일 경로로 수정)
video_path = '/Users/jaewon/Desktop/Taskfolder/servertime.mov'
i=1
j=800
# 동영상 캡처 객체 생성
cap = cv2.VideoCapture(video_path)

# 동영상 파일이 열리지 않으면 오류 출력
if not cap.isOpened():
    print("Error: Couldn't open the video.")
    exit()

while True:
    # 비디오에서 한 프레임씩 읽기
    ret, frame = cap.read()
    if j==0:
        j=800
    if i==800:
        i=1
    # 프레임이 제대로 읽히지 않으면 종료
    if not ret:
        print("Error: Couldn't fetch the frame.")
        break
    # 한 줄 그리기 (시작점과 끝점 설정)

    i+=1
    j-=2
    start_point = (i, j)  # 시작점 (x, y)
    end_point = (j, i)    # 끝점 (x, y)
    color = (i, j, j)       # 선의 색상 (녹색)
    thickness = 2             # 선의 두께

    # cv2.line() 함수로 선 그리기
    cv2.line(frame, start_point, end_point, color, thickness)
    # 프레임을 화면에 표시
    cv2.imshow('Video', frame)
    
    # 'q' 키를 누르면 영상 창을 닫고 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 동영상 캡처 객체 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
