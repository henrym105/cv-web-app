import React, { useState } from 'react';
import ImageUpload from './ImageUpload';
import CameraCapture from './CameraCapture';
import './App.css';

function App() {
  const [uploadedImage, setUploadedImage] = useState(null);

  const handleImageUpload = (image) => {
    setUploadedImage(image);
  };

  return (
    <div className="App">
      <header>
        <div className="container">
          <div id="branding">
            <h1>Image Upload</h1>
          </div>
        </div>
      </header>
      <div className="container">
        <h2>Upload an Image</h2>
        <p>Choose an image file from your device or use your camera to take a picture.</p>
        <ImageUpload onImageUpload={handleImageUpload} />
        <CameraCapture onImageUpload={handleImageUpload} />
        {uploadedImage && (
          <div id="imageContainer">
            <img id="uploadedImage" src={uploadedImage} alt="Uploaded" style={{ maxWidth: '100%', height: 'auto' }} />
            <button onClick={() => setUploadedImage(null)}>Clear</button>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;