import React from 'react';

function ImageUpload({ onImageUpload, setLoading }) {
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const formData = new FormData();
      formData.append('file', file);

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
    }
  };

  return (
    <form>
      <input type="file" onChange={handleFileChange} />
    </form>
  );
}

export default ImageUpload;