import cv2
import time

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Start video capture from the webcam
cap = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    cv2.rectangle(frame, (10, 10), (200, 50), (0, 255, 0), -1)
    cv2.putText(frame, f'Faces: {len(faces)}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2) 

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for i,(x, y, w, h) in enumerate(faces):
        cv2.putText(frame, f'Face {i+1}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # centre tracking dot
        center_x = x + w // 2
        center_y = y + h // 2
        cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
        # face ID label
        cv2.putText(frame, f'ID: {i+1}', (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    # People count display
    cv2.putText(frame, f'Total Faces: {len(faces)}', (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # FPS Counter
    curr_time = time.time()
    fps = 1 / (curr_time - getattr(cap, 'prev_time', curr_time))
    prev_time = curr_time

    cv2.putText(frame, f'FPS: {fps:.2f}', (frame.shape[1] - 150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)



    # Display the resulting frame
    cv2.imshow('Smart face tracking and countion', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
