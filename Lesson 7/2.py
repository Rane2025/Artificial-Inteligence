import cv2   # Import OpenCV

# Load the image
image = cv2.imread("image.png")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  

# Resize the grayscale image
resized_image = cv2.resize(gray_image, (224, 224))  
# Show the processed image
cv2.imshow("Processed Image", resized_image)  
# Wait for a key press
key = cv2.waitKey(0)  

# If 's' key is pressed → save the image
if key == ord('s'):
    cv2.imwrite("grayscale_resized_image.jpg", resized_image)
    print("Image saved as grayscale_resized_image.jpg")
else:
    print("Image not saved")

cv2.destroyAllWindows()

# Print dimensions
print(f"Processed Image Dimensions: {resized_image.shape}")
