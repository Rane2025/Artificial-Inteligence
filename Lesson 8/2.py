import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('Corax.png')
# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image. Please check the file path.")
    exit()
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Resize the grayscale image to 224x224
resized_image = cv2.resize(gray_image, (224, 224))
# Save the processed image
cv2.imwrite('processed_image.jpg', resized_image)
print(f"Processed Image Dimensions: {resized_image.shape}")
# get hight and width of the resized image
(h, w) = image.shape[:2]
centre = (w // 2, h // 2)
# Rotate the image by 45 degrees
M = cv2.getRotationMatrix2D(centre, 45, 1.0)
rotated_image = cv2.warpAffine(resized_image, M, (w, h))
# Show the processed image
plt.imshow(rotated_image, cmap='gray')
plt.title("Rotated Image")
plt.axis('off')
plt.show()
# Save the rotated image
cv2.imwrite('rotated_image.jpg', rotated_image)
print(f"Rotated Image Dimensions: {rotated_image.shape}")
