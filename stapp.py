import streamlit as st
import cv2
import numpy as np
from PIL import Image
from mymodels import poseEstimationModule as pem

# Title
st.title('Pose Estimation Web App')
st.text('upload any photo to overlay an outline of ')


# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    
    # Process the image with the pose estimation model
    try:
        detector = pem.poseDetector()
        img = detector.findPose(img)
        img = detector.findFeet(img)

        # Apply color correction
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Convert NumPy array to PIL Image and display
        img = Image.fromarray(img)
        st.image(img, caption='Processed Image', use_column_width=True)

    except Exception as e:
        st.error(f'Error during image processing: {str(e)}')
