import cv2
import time
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
# Start video capture
SCROLL_SPEED = 20
SCROLL_DEALY = 1 # seconds between scroll actions
CAM_WIDTH, CAM_HEIGHT = 640, 480

# Function to detect gesture based on hand landmarks
def detect_gesture(landmarks, handedness):
    fingers = []
    
    # Fingertip and pip landmark indences
    tips = [
        mp_hands.HandLandmark.THUMB_TIP,
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    # Check if fingers are up (Exept thumb)
    for tip in tips[1:]:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)  # Finger is up
        else:
            fingers.append(0)  # Finger is down
    
    # Check thumb separately based on hand orientation
    thumb_tip = mp_hands.HandLandmark.THUMB_TIP
    thumb_ip = mp_hands.HandLandmark.THUMB_IP
    if (handedness == 'Right' and landmarks[thumb_tip].x > landmarks[thumb_ip].x) or \
       (handedness == 'Left' and landmarks[thumb_tip].x < landmarks[thumb_ip].x):
        fingers.append(1)  # Thumb is up
    else:
        fingers.append(0)  # Thumb is down
    
    total_fingers = sum(fingers)

    if total_fingers == 5:
        return "Scroll Up"
    elif total_fingers == 0:
        return "Scroll Down"
    else:
        return "None"


# Initialize camera:
cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)

last_scroll = 0
p_time = 0
print("🤚🏽🤚🏼🤚🏾🤚🏿🤚🏻🤚 Gesture Scroll Control Active 🤚🏽🤚🏼🤚🏾🤚🏿🤚🏻🤚")
print("Open palm ➡️ Scroll Up")
print("Closed fist ➡️ Scroll Down")
print("Press 🅿️ with your 🫵 stop to the program from running ")
# Main loop
while cap.isOpened:
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Process the image and find hands
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand_landmarks.landmark, hand_handedness.classification[0].label)
            current_time = time.time()
            if gesture == "Scroll Up" and current_time - last_scroll > SCROLL_DEALY:
                pyautogui.scroll(SCROLL_SPEED)
                last_scroll = current_time
            elif gesture == "Scroll Down" and current_time - last_scroll > SCROLL_DEALY:
                pyautogui.scroll(-SCROLL_SPEED)
                last_scroll = current_time

    # Display the resulting image
    cv2.imshow('Hand Gesture Scroll Control', image)

    # Exit on 'p' key press
    if cv2.waitKey(5) & 0xFF == ord('p'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()