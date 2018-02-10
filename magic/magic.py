

import cv2


face_cascade = cv2.CascadeClassifier('m2.xml')
magic_cascade = cv2.CascadeClassifier('m3.xml')


def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        magic = magic_cascade.detectMultiScale(roi_gray, 1.7, 22)
        for (sx, sy, sw, sh) in magic:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            cv2.putText(roi_color, 'you look beautiful when you do this', (sx + 5, sy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0),
                                    2)
		
    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
