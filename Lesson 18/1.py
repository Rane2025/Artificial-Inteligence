import cv2, mediapipe as  mp, time, numpy as np

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Filter configration
FILTER = [None, "GRAYSCALE", "SEPIA", "NEGATIVE", "BLUR"]
current_filter = 0

# Webcam Setup
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Gesture timing and state
last_action_time = 0; DEBOUNCE_TIME = 1 # seconds
pinch_in_progress = False; capture_request = False
def apply_filter(frame, ftype):
    if ftype == "GRAYSCALE":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif ftype == "SEPIA":
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        return cv2.transform(frame, kernel)
    elif ftype == "NEGATIVE":
        return cv2.bitwise_not(frame)
    elif ftype == "BLUR":
        return cv2.GaussianBlur(frame, (15, 15), 0)
    else:
        return frame
    
while True:
        success, img = cap.read()
        if not success:
            print("Error: Could not read frame.")
            break
        img = cv2.flip(img, 1)
        h, w = img.shape[:2]
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        capture_request = False

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                distance = np.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)

                if distance < 0.05 and not pinch_in_progress and time.time() - last_action_time > DEBOUNCE_TIME:
                    pinch_in_progress = True
                    capture_request = True
                    last_action_time = time.time()
                elif distance >= 0.05 and pinch_in_progress:
                    pinch_in_progress = False
                break
        filtered_img = apply_filter(img, FILTER[current_filter])
        diplay_img = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2GRAY) if FILTER[current_filter] == "GRAYSCALE" else filtered_img
        

        # Capture photo if requested
        if capture_request:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"capture_{timestamp}.jpg"
            cv2.imwrite(filename, img)
            print(f"Photo captured: {filename}")
        cv2.imshow("Hand Gesture Filter Capture", diplay_img)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            break

cap.release()
cv2.destroyAllWindows()