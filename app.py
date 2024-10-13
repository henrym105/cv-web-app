import os
import cv2
import io
import numpy as np
from flask import Flask, request, render_template, send_file, jsonify
from PIL import Image
from mymodels import poseEstimationModule as pem
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Ensure there's a folder for uploaded images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    logging.debug(f"Received file: {file.filename}")

    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        logging.debug(f"File saved to: {filename}")

        try:
            # Process the image with the pose estimation model
            logging.debug("Processing image with pose estimation model")
            img = cv2.imread(str(filename))
            detector = pem.poseDetector()
            img = detector.findPose(img)
            img = detector.findFeet(img)
            logging.debug("Image processed successfully")

            # Apply color correction
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Convert NumPy array to PIL Image
            img = Image.fromarray(np.uint8(img))
            
            # Convert PIL Image to byte stream
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=70)
            img_io.seek(0)

            return send_file(img_io, mimetype='image/jpeg')

        except FileNotFoundError:
            return jsonify({'Error': 'File not found after saving'}), 500
        except IOError:
            return jsonify({'Error': 'Error processing image file'}), 500
        except Exception as e:
            return jsonify({'Error': 'Error during image processing', 
                            'Message': str(e),
                            'Removing file':filename}), 500
        finally:
            # Remove the downloaded image after processing to avoid build up
            os.remove(filename)
    return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug=True)