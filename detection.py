import cv2
import time
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
at_com = 0
not_at_com = 0

def detect_bounding_box(vid):
    time_track = time.time()
    global at_com
    global not_at_com
    #gray_image converts color frame to gray for better detection
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    #limit to one face
    face = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))[:1]
    print(face)
    if len(face) == 0:
        cur_time = time.time()
        at_com += cur_time - time_track
        time_track = cur_time
        print("at com" + str(at_com))
    else:
        #only has one face
        x, y, w, h = face[0]
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cur_time = time.time()
        not_at_com += cur_time - time_track
        time_track = cur_time
        print("not at com" + str(not_at_com))
    return face

def process_video(video_capture):
    if not video_capture.isOpened():
        print("error: camera not turning on")
    while True:

        result, video_frame = video_capture.read() 
        if result is False:
            break 
        face = detect_bounding_box(video_frame)


        print(face)
        cv2.imshow(
            "Sit Still", video_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()