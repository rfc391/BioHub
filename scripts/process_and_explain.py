import cv2

def process_image_with_opencv(image_path):
    # Load an image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply edge detection
    edges = cv2.Canny(gray_image, 100, 200)
    return edges

def main():
    image_path = "assets/sample_image.jpg"  # Replace with your test image
    print("Processing image with OpenCV...")
    edges = process_image_with_opencv(image_path)
    cv2.imwrite("assets/edges_output.jpg", edges)
    print("Edges saved as 'assets/edges_output.jpg'")

if __name__ == "__main__":
    main()
