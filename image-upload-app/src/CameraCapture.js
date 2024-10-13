import React, { useRef, useState } from 'react';

function CameraCapture({ onImageUpload, setLoading }) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [isCameraOn, setIsCameraOn] = useState(false);

  const startCamera = () => {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then((stream) => {
        videoRef.current.srcObject = stream;
        setIsCameraOn(true);
      })
      .catch((err) => console.error('Error accessing camera: ', err));
  };

  const captureImage = () => {
    const context = canvasRef.current.getContext('2d');
    context.drawImage(videoRef.current, 0, 0, canvasRef.current.width, canvasRef.current.height);
    canvasRef.current.toBlob((blob) => {
      const formData = new FormData();
      formData.append('file', blob, 'captured_image.jpg');

      setLoading(true); // Start loading

      fetch('/upload', {
        method: 'POST',
        body: formData,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.blob();
        })
        .then((blob) => {
          const url = URL.createObjectURL(blob);
          onImageUpload(url);
          setLoading(false); // Stop loading when the image is uploaded
        })
        .catch((error) => {
          console.error('Error:', error);
          setLoading(false); // Stop loading on error
        });
    }, 'image/jpeg');
  };

  return (
    <div>
      <button onClick={startCamera}>Use Camera</button>
      {isCameraOn && (
        <div>
          <video ref={videoRef} width="640" height="480" autoPlay></video>
          <button onClick={captureImage}>Capture</button>
          <canvas ref={canvasRef} width="640" height="480" style={{ display: 'none' }}></canvas>
        </div>
      )}
    </div>
  );
}

export default CameraCapture;