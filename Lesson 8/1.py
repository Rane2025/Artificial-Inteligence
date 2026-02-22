import cv2
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('Corax.png')

# Step 2: Convert from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()

# Step 3: Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Step 4: Resize the image to 224x224
resized_image = cv2.resize(gray_image, (224, 224))
plt.imshow(resized_image, cmap='gray')
plt.title("Resized Grayscale Image")
plt.show()

# Step 5: Save the processed image
cv2.imwrite('processed_image.jpg', resized_image)
print(f"Processed Image Dimensions: {resized_image.shape}")

# Step 6: Crop the image to 100x100 from the center
h, w = resized_image.shape
crop_size = 100
start_x = w // 2 - crop_size // 2
start_y = h // 2 - crop_size // 2
cropped_image = resized_image[start_y:start_y + crop_size, start_x:start_x + crop_size]
plt.imshow(cropped_image, cmap='gray')
plt.title("Cropped Image")
plt.show()
cv2.imwrite('cropped_image.jpg', cropped_image)
print(f"Cropped Image Dimensions: {cropped_image.shape}")