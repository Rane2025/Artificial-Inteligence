import cv2
import mediapipe as mp
import numpy as np
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from math import hypot
import screen_brightness_control as sbc

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    min_vol, max_vol, _ = volume.GetVolumeRange()
except Exception as e:
    print(f"Audio control initialization failed: {e}")
    exit()


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            thumb_tip = (int(landmarks[4].x * w), int(landmarks[4].y * h))
            index_tip = (int(landmarks[8].x * w), int(landmarks[8].y * h))
            cv2.circle(img, thumb_tip, 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index_tip, 10, (255, 0, 0), cv2.FILLED)
            cv2.line(img, thumb_tip, index_tip, (255, 0, 0), 3)
            distance = hypot(index_tip[0] - thumb_tip[0], index_tip[1] - thumb_tip[1])
            vol = np.interp(distance, [30, 200], [min_vol, max_vol])
            volume.SetMasterVolumeLevel(vol, None)
            brightness = np.interp(distance, [30, 200], [0, 100])
            sbc.set_brightness(int(brightness))
            dist = hypot(index_tip[0] - thumb_tip[0], index_tip[1] - thumb_tip[1])
            if label == "right":
                vol = np.interp(dist, [30, 200], [min_vol, max_vol])
                try:
                    volume.SetMasterVolumeLevel(vol, None)
                except Exception as e:
                    print(f"Volume control failed: {e}")
                vol_bar = int(np.interp(dist, [30, 300], [400, 150]))
                cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 3)
                cv2.rectangle(img, (50, vol_bar), (85, 400), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'{int(np.interp(dist, [30, 200], [0, 100]))} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
            elif label == "left":
                brightness = np.interp(dist, [30, 200], [0, 100])
                try:
                    sbc.set_brightness(int(brightness))
                except Exception as e:
                    print(f"Brightness control failed: {e}")
                bright_bar = int(np.interp(dist, [30, 300], [400, 150]))
                cv2.rectangle(img, (100, 150), (135, 400), (255, 0, 0), 3)
                cv2.rectangle(img, (100, bright_bar), (135, 400), (255, 0, 0), cv2.FILLED)
                cv2.putText(img, f'{int(np.interp(dist, [30, 200], [0, 100]))} %', (90, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    
    cv2.imshow("Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()