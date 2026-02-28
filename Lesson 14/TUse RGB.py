# Import nessacary libraries
import cv2
import numpy as np
# Apply filters

def apply_filter(image, ftype):
    """Apply a convolution filter to an image."""
    img = image.copy()
    if ftype =="red_tint":
        img[:, :, 1] = img[:, :, 0] = 0   # Set green channel to red channel value
    elif ftype =="green_tint":
        img[:, :, 0] = img[:, :, 2] = 0   # Set red channel to green channel value
    elif ftype =="blue_tint":
        img[:, :, 0] = img[:, :, 1] = 0   # Set red channel to blue channel value.
    elif ftype =="sobel":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        img = np.sqrt(sobelx**2 + sobely**2)
    elif ftype =="canny":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.Canny(gray, 100, 200)
    elif ftype =="cartoon":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
        color = cv2.bilateralFilter(img, 9, 250, 250)
        img = cv2.bitwise_and(color, color, mask=edges)
    return img

# Put def main to deal with main problem.
# If you remove a word (exept coments) their will be a huge problem!
def main():
    # Load the image
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    ftype = "original"
    print("Press 'r' for red tint, 'g' for green tint, 'b' for blue tint, 's' for sobel edge detection, 'c' for canny edge detection, 't' for cartoon effect, and 'o' for original.")
    print("Credits are given to:")
    print("1. OpenCV for providing the library to work with images and videos.")
    print("2. The developers and contributors of OpenCV for their continuous efforts in improving the library(That me).")
    print("3. VS Code for providing a great code editor to write and test the code.")
    print("4. Git Repostries for helping to come in contect of the Git media")
    print("Enjoy the filters and have fun experimenting with them! Remember to press 'q' to quit the application.")
    print("Don't forget to share my creations and have fun exploring the world of image processing!")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        filtered_frame = apply_filter(frame, ftype)
        cv2.imshow('Filtered Video', filtered_frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            ftype = "red_tint"
        elif key == ord('g'):
            ftype = "green_tint"
        elif key == ord('b'):
            ftype = "blue_tint"
        elif key == ord('s'):
            ftype = "sobel"
        elif key == ord('c'):
            ftype = "canny"
        elif key == ord('t'):
            ftype = "cartoon"
        elif key == ord('o'):
            ftype = "original"
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()