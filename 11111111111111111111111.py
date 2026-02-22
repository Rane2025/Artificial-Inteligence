import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply a color filter to the image based on the specified type."""
    if filter_type == 'red_tint':
        # Create a red filter
        red_filter = np.zeros_like(image)
        red_filter[:, :, 2] = 255  # Set the red channel to maximum
        filtered_image = cv2.addWeighted(image, 0.5, red_filter, 0.5, 0)
    
    elif filter_type == 'green_tint':
        # Create a green filter
        green_filter = np.zeros_like(image)
        green_filter[:, :, 1] = 255  # Set the green channel to maximum
        filtered_image = cv2.addWeighted(image, 0.5, green_filter, 0.5, 0)
    
    elif filter_type == 'blue_tint':
        # Create a blue filter
        blue_filter = np.zeros_like(image)
        blue_filter[:, :, 0] = 255  # Set the blue channel to maximum
        filtered_image = cv2.addWeighted(image, 0.5, blue_filter, 0.5, 0)
    
    else:
        print("Invalid filter type. Please choose 'red_tint', 'green_tint', or 'blue_tint'.")
        return image
    
    return filtered_image

omaga_path = "image.png"  # Path to your image

omaga = cv2.imread(omaga_path)
if omaga is None:
    print(f"Error: Could not load image from {omaga_path}")
else:
    # Apply a red tint filter to the image
    filtered_image = apply_color_filter(omaga, 'red_tint')

    # Display the original and filtered images
    cv2.imshow("Original Image", omaga)
    cv2.imshow("Red Tint Filtered Image", filtered_image)

    # Wait for a key press and close the windows
    print("Press the following keys to apply filters:")
    print("o - Original")
    print("r - Red Tint")
    print("g - Green Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("q - Quit")

    while True:
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('o'):
            cv2.imshow("Filtered Image", omaga)
        
        elif key == ord('r'):
            filtered_image = apply_color_filter(omaga, 'red_tint')
            cv2.imshow("Filtered Image", filtered_image)
        
        elif key == ord('g'):
            filtered_image = apply_color_filter(omaga, 'green_tint')
            cv2.imshow("Filtered Image", filtered_image)
        
        elif key == ord('b'):
            filtered_image = apply_color_filter(omaga, 'blue_tint')
            cv2.imshow("Filtered Image", filtered_image)
        
        elif key == ord('i'):
            # Increase red intensity
            red_filter = np.zeros_like(omaga)
            red_filter[:, :, 2] = 255  # Set the red channel to maximum
            filtered_image = cv2.addWeighted(filtered_image, 0.5, red_filter, 0.5, 0)
            cv2.imshow("Filtered Image", filtered_image)
        
        elif key == ord('d'):
            # Decrease blue intensity
            blue_filter = np.zeros_like(omaga)
            blue_filter[:, :, 0] = 255  # Set the blue channel to maximum
            filtered_image = cv2.addWeighted(filtered_image, 0.5, blue_filter, -0.5, 0)
            cv2.imshow("Filtered Image", filtered_image)
        
        elif key == ord('q'):
            print("Exiting...")
            break
    cv2.destroyAllWindows()