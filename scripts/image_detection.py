import cv2
from PIL import Image
import os
import glob
import numpy as np  # Add this line

def detect_and_mark_faces(input_path, output_dir):
    # Load the image using PIL to handle various image formats
    image_pil = Image.open(input_path)
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)  # Use np for nump

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Create an output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the marked image using PIL to handle various image formats
    output_path = os.path.join(output_dir, f"marked_{os.path.basename(input_path)}")
    marked_image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    marked_image_pil.save(output_path)

    print(f"Detected {len(faces)} face(s). Marked image saved to {output_path}")

if __name__ == "__main__":
    input_directory = "./input/"
    output_directory = "./output/"

    # Get a list of all image files in the input directory
    image_files = glob.glob(os.path.join(input_directory, "*"))

    for image_file in image_files:
        detect_and_mark_faces(image_file, output_directory)
