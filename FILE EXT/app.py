import os
import shutil
from pydub.utils import mediainfo
import cv2
from PIL import Image
import json
from docx import Document 

def classify(input_directory, output_directory):
    image_ext = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    audio_ext = ['.wav', '.mp3', '.flac', '.ogg']
    video_ext = ['.mp4', '.avi', '.mkv']
    text_ext = ['.txt', '.json', '.csv', '.xml']


    os.makedirs(os.path.join(output_directory, 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_directory, 'audio'), exist_ok=True)
    os.makedirs(os.path.join(output_directory, 'video'), exist_ok=True)
    os.makedirs(os.path.join(output_directory, 'text'), exist_ok=True)

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(filename)[-1].lower()

        if ext in image_ext:
            try:
                img = Image.open(file_path)
                img.verify()
                shutil.move(file_path, os.path.join(output_directory, 'images', filename))
                print(f'Moved image: {filename}')
            except Exception as e:
                print(f'Error processing image {filename}: {e}')

        elif ext in audio_ext:
            try:
                mediainfo(file_path)
                shutil.move(file_path, os.path.join(output_directory, 'audio', filename))
                print(f'Moved audio: {filename}')
            except Exception as e:
                print(f'Error processing audio {filename}: {e}')

        elif ext in video_ext:
            try:
                cap = cv2.VideoCapture(file_path)
                if cap.isOpened():
                    cap.release()  # Ensure file lock is released
                    shutil.move(file_path, os.path.join(output_directory, 'video', filename))
                    print(f'Moved video: {filename}')
                else:
                    print(f"Unable to open video: {filename}")
            except Exception as e:
                print(f'Error processing video {filename}: {e}')

        elif ext in text_ext or ext == '.docx':
            try:
                if ext == '.json':
                    with open(file_path, 'r') as f:
                        try:
                            json.load(f)
                        except json.JSONDecodeError:
                            print(f'Invalid JSON in {filename}')
                elif ext == '.docx':
                    try:
                        doc = Document(file_path)  # Open and verify the .docx file
                    except Exception as e:
                        print(f'Error reading DOCX file {filename}: {e}')
                shutil.move(file_path, os.path.join(output_directory, 'text', filename))
                print(f'Moved text: {filename}')
            except Exception as e:
                print(f'Error processing text {filename}: {e}')

input_dir = './files'
output_dir = './classified'
classify(input_dir, output_dir)
