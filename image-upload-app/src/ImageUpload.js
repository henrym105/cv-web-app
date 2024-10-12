import React from 'react';

function ImageUpload({ onImageUpload }) {
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const formData = new FormData();
      formData.append('file', file);

      fetch('/upload', {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.blob())
        .then((blob) => {
          const url = URL.createObjectURL(blob);
          onImageUpload(url);
        })
        .catch((error) => console.error('Error:', error));
    }
  };

  return (
    <form>
      <input type="file" onChange={handleFileChange} />
    </form>
  );
}

export default ImageUpload;