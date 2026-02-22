import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image using OpenCV and Matplotlib"""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale
        plt.imshow(image, cmap='gray')
    else:  # Color
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_image_processing(image_path):
    """Main function to perform interactive image processing"""
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return

    # Display original image
    display_image("Original Image", image)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Grayscale Image", gray_image)

    # Resize the grayscale image
    resized_image = cv2.resize(gray_image, (224, 224))
    display_image("Resized Grayscale Image", resized_image)
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Choose an operation (1-6): ").strip()
        if choice == '1':
            sobelx = cv2.Sobel(resized_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(resized_image, cv2.CV_64F, 0, 1, ksize=3)
            sobel_combined = cv2.magnitude(sobelx, sobely)
            display_image("Sobel Edge Detection", sobel_combined)
        
        elif choice == '2':
            edges = cv2.Canny(resized_image, 100, 200)
            display_image("Canny Edge Detection", edges)
        
        elif choice == '3':
            laplacian = cv2.Laplacian(resized_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", laplacian)
        
        elif choice == '4':
            blurred = cv2.GaussianBlur(resized_image, (5, 5), 0)
            display_image("Gaussian Smoothing", blurred)
        
        elif choice == '5':
            median = cv2.medianBlur(resized_image, 5)
            display_image("Median Filtering", median)
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

interactive_image_processing("Radha Krishna.jpg")