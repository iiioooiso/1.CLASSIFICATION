import os
import shutil
from PIL import Image
import cv2
from mutagen import File as AudioFile  # For audio metadata
import filetype  # Modern library to detect file type based on content
import json
from docx import Document

def classify(input_directory, output_directory):

    os.makedirs(os.path.join(output_directory, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_directory, 'audio'), exist_ok=True)
    os.makedirs(os.path.join(output_directory, 'video'), exist_ok=True)
    os.makedirs(os.path.join(output_directory, 'text'), exist_ok=True)

    # Process each file in the input directory
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Detect file type using `filetype`
        kind = filetype.guess(file_path)

        try:
            if kind is None:
                print(f"Unknown file type: {filename}")
                continue

            # Classify based on MIME type or metadata
            if kind.mime.startswith('image/'):  # Images
                classify_image(file_path, output_directory)
            elif kind.mime.startswith('audio/'):  # Audio
                classify_audio(file_path, output_directory)
            elif kind.mime.startswith('video/'):  # Video
                classify_video(file_path, output_directory)
            elif kind.mime.startswith('text/') or filename.endswith(('.json', '.csv', '.xml')):  # Text
                classify_text(file_path, output_directory)
            else:
                print(f"Unrecognized file type for {filename}: {kind.mime}")
        except Exception as e:
            print(f"Error processing file {filename}: {e}")


# Helper functions to classify specific file types
def classify_image(file_path, output_directory):
    try:
        with Image.open(file_path) as img:  # Open image using Pillow
            img.verify()  # Verify it's a valid image
            shutil.move(file_path, os.path.join(output_directory, 'images', os.path.basename(file_path)))
            print(f'Moved image: {os.path.basename(file_path)}')
    except Exception as e:
        print(f'Error processing image {file_path}: {e}')

def classify_audio(file_path, output_directory):
    try:
        audio = AudioFile(file_path)  # Analyze audio metadata using `mutagen`
        if audio is not None:
            shutil.move(file_path, os.path.join(output_directory, 'audio', os.path.basename(file_path)))
            print(f'Moved audio: {os.path.basename(file_path)}')
        else:
            print(f"Unrecognized audio file: {file_path}")
    except Exception as e:
        print(f'Error processing audio {file_path}: {e}')

def classify_video(file_path, output_directory):
    try:
        cap = cv2.VideoCapture(file_path)  # Open video using OpenCV
        if cap.isOpened():
            shutil.move(file_path, os.path.join(output_directory, 'video', os.path.basename(file_path)))
            print(f'Moved video: {os.path.basename(file_path)}')
        cap.release()  # Release the video capture object
    except Exception as e:
        print(f'Error processing video {file_path}: {e}')

def classify_text(file_path, output_directory):
    try:
        # Handle .docx files specifically
        if file_path.endswith('.docx'):
            try:
                doc = Document(file_path)  # Open the .docx file
                _ = [p.text for p in doc.paragraphs]  # Read paragraphs to ensure it's valid
                shutil.move(file_path, os.path.join(output_directory, 'text', os.path.basename(file_path)))
                print(f'Moved .docx file: {os.path.basename(file_path)}')
            except Exception as e:
                print(f'Error processing .docx file {file_path}: {e}')
            return  # Exit early since we've processed .docx files here

        # For other text formats (.txt, .json, .csv, etc.)
        with open(file_path, 'r', encoding='utf-8') as f:
            if file_path.endswith('.json'):
                try:
                    json.load(f)  # Check if JSON is valid
                except json.JSONDecodeError:
                    print(f'Invalid JSON in {file_path}')
            shutil.move(file_path, os.path.join(output_directory, 'text', os.path.basename(file_path)))
            print(f'Moved text: {os.path.basename(file_path)}')
    except Exception as e:
        print(f'Error processing text {file_path}: {e}')
        
input_dir = './files'
output_dir = './classified'
classify(input_dir, output_dir)
