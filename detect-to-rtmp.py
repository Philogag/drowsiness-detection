#! python
# -*- coding: utf-8 -*-
# Author: kun
# @Time: 2020-01-06 14:00

from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
from time import sleep

from ffmpeg_streamer import Streamer

model_path = "./model/shape_predictor_68_face_landmarks.dat"

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


def detect():
    thresh = 0.25
    frame_check = 10  # default is 20
    detect = dlib.get_frontal_face_detector()
    predict = dlib.shape_predictor(model_path)  # Dat file is the crux of the code

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

    cap = cv2.VideoCapture("rtmp://192.168.10.10:1935/live/cap")
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print("Get size: {}x{}".format(size[0], size[1]))
    # cap = cv2.VideoCapture(-1, cv2.CAP_DSHOW)
    streamer = Streamer("rtmp://192.168.10.10:1935/live/detect", (640, 480))

    flag = 0
    while True:
        ret, frame = cap.read()
        
        # print(ret, not frame is None)
        if (not ret):
            print("Cannot open vedio.")
            sleep(5)
        frame = imutils.resize(frame, width=640, height=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)
        for subject in subjects:
            shape = predict(gray, subject)
            shape = face_utils.shape_to_np(shape)  # converting to NumPy Array
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
            if ear < thresh:
                flag += 1
                # print("ear: ", flag)
                if flag >= frame_check:
                    cv2.putText(frame, "****************ALERT!****************", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(frame, "****************ALERT!****************", (10, 325),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                # print ("Drowsy")
            else:
                flag = 0
        # print("Flag: {}".format(flag))
        cv2.putText(frame, "Flag: {}".format(flag), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        # cv2.imshow("Frame", frame)
        streamer.pushframe(frame)
        # key = cv2.waitKey(1) & 0xFF
        # if key == ord("q"):
        #     break
    # cv2.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    detect()