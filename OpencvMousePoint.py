import cv2

# 마우스 이벤트 콜백 함수
def show_coordinates(event, x, y, flags, param):
    global mouse_position
    if event == cv2.EVENT_MOUSEMOVE:  # 마우스 움직임 이벤트
        mouse_position = (x, y)

# 동영상 파일 경로 설정 (0이면 웹캠으로 가능 )
video_path = '/Users/jaewon/Desktop/Taskfolder/public/servertime.mov'  
cap = cv2.VideoCapture(video_path)


mouse_position = (0, 0)


cv2.namedWindow('Video')
cv2.setMouseCallback('Video', show_coordinates)

print("Move your mouse over the video to see coordinates. Press 'q' to exit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Finished playing video or error reading frame..")
        break

  
    cv2.putText(frame, f'X: {mouse_position[0]}, Y: {mouse_position[1]}', 
                (mouse_position[0] + 10, mouse_position[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

 
    cv2.imshow('Video', frame)

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
