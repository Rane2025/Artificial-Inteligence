import cv2
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread("Corax.png")
if image is None:
    raise FileNotFoundError("Could not load Corax.png")

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Get image dimensions
height, width = gray_image.shape
print(f"Image Dimensions: {width}x{height} (Width x Height)")

# Convert BGR to RGB for matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 4: Draw rectangles
rect_width, rect_height = 150, 150

# Rectangle 1 (top-left)
top_left1 = (20, 20)
bottom_right1 = (20 + rect_width, 20 + rect_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 0, 255), 2)

# Rectangle 2 (bottom-right)
top_left2 = (width - 20 - rect_width, height - 20 - rect_height)
bottom_right2 = (width - 20, height - 20)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 0), 2)

# Step 5: Draw center circles
center1 = (top_left1[0] + rect_width // 2, top_left1[1] + rect_height // 2)
center2 = (top_left2[0] + rect_width // 2, top_left2[1] + rect_height // 2)

cv2.circle(image_rgb, center1, 10, (0, 255, 0), -1)
cv2.circle(image_rgb, center2, 10, (0, 255, 0), -1)

# Step 6: Labels and connecting line
cv2.putText(image_rgb, 'Region 1', (center1[0] - 40, center1[1] - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.putText(image_rgb, 'Region 2', (center2[0] - 40, center2[1] - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.line(image_rgb, center1, center2, (255, 255, 0), 2)

# Step 7: Bi-directional arrows
cv2.arrowedLine(image_rgb, center1, center2, (255, 0, 255), 2, tipLength=0.1)
cv2.arrowedLine(image_rgb, center2, center1, (255, 0, 255), 2, tipLength=0.1)

# Step 8: Annotate image height
text_position = (20, height // 2)
cv2.putText(image_rgb, f'Height: {height}px', text_position,
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# Step 9: Display the result
plt.figure(figsize=(10, 6))
plt.imshow(image_rgb)
plt.axis('off')
plt.title('Annotated Image with Rectangles, Circles, and Arrows')
plt.show()
