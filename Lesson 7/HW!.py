import cv2

# Load an image
image = cv2.imread('Corax.png')

# Check if image loaded successfully
if image is None:
    print("Error: Could not load image. Please check the file path.")
    exit()

# Create a resized window
cv2.namedWindow('Resized Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Resized Window', 800, 600)

# Show then image in the window
cv2.imshow('Loaded Image', image)

# Print image dimension
print(f"Image Dimensions: {image.shape[1]}x{image.shape[0]} (Width x Height)")

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()