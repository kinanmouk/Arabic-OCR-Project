import os
import cv2

def preprocess_image(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Failed to load image: {image_path}")
        return
    
    # Resize the image to 32x32 (if necessary)
    image = cv2.resize(image, (32, 32))
    
    # Apply Gaussian blur to reduce noise
    processed_image = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Save the processed image
    cv2.imwrite(output_path, processed_image)
    print(f"Processed and saved image: {output_path}")

def process_directory(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Recursively process each image in the directory structure
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(root, filename)
                
                # Create the corresponding output directory structure
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                os.makedirs(output_subdir, exist_ok=True)
                
                output_path = os.path.join(output_subdir, filename)
                print(f"Processing file: {filename}")
                preprocess_image(input_path, output_path)
            else:
                print(f"Skipped non-image file: {filename}")

if __name__ == "__main__":
    # Define input and output directories
    input_dir = "data/handwritten"
    output_dir = "data/handwritten/processed"
    
    # Process the handwritten images
    process_directory(input_dir, output_dir)
