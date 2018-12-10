from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import imutils
import time
import dlib
import cv2
import boto3

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    C = dist.euclidean(eye[0], eye[3])

    ear = (A+B) / (2.0 * C)

    return ear

session = boto3.Session(aws_access_key_id="AKIAJSCUUGUNFZNZEOHQ", aws_secret_access_key="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", region_name="ap-northeast-2")
s3 = session.resource('s3')

EYE_AR_THRESH = 0.19
EYE_AR_CONSEC_FRAMES = 3

image_name = "face"
file_num = 0

COUNTER = 0
TOTAL = 0

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

vs = VideoStream(src=0).start()
fileStream = False
time.sleep(1.0)

while True:
    if fileStream and not vs.more():
        break

    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)
    #print(rects)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        (x, y, w, h) = face_utils.rect_to_bb(rect)
        roi_gray = gray[y-20:y+h+20, x-20:x+w+20]

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        #leftEyeHull = cv2.convexHull(leftEye)
        #rightEyeHull = cv2.convexHull(rightEye)
        #cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        #cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if ear < EYE_AR_THRESH:
            COUNTER += 1
        else:
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL += 1

                COUNTER = 0

        if TOTAL > 0:
            img_item = image_name + str(file_num) + ".jpg"
            cv2.imwrite(img_item, roi_gray)
            data = open(img_item, 'rb')
            s3.Bucket('dlatltkwls').put_object(Key=img_item, Body=data)

            file_num += 1
            TOTAL = 0

        #cv2.putText(frame, "Blinks: {}".format(TOTAL), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        #cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
cv2.destroyAllWindows()
vs.stop()






