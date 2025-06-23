import React, { useState, useRef } from "react";
import "./Upload.css";

const Upload = () => {
  const [file, setFile] = useState(null);
  const [error, setError] = useState("");
  const fileInputRef = useRef();

  const handleFiles = (files) => {
    const selectedFile = files[0];
    if (!selectedFile) return;

    if (selectedFile.type !== "application/pdf") {
      setError("Please upload a PDF file only.");
      setFile(null);
      return;
    }

    setError("");
    setFile(selectedFile);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    handleFiles(e.dataTransfer.files);
  };

  const handleDragOver = (e) => e.preventDefault();

  const handleFileChange = (e) => {
    handleFiles(e.target.files);
  };

  const handleSubmit = async () => {
    if (!file) {
      setError("No file selected");
      return;
    }

    setError("");
    const formData = new FormData();
    formData.append("file", file);

    try {
      const token = localStorage.getItem("token");
      const res = await fetch("http://localhost:8000/upload", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: formData,
      });

      if (!res.ok) throw new Error("Upload failed");

      alert("File uploaded successfully!");
      setFile(null);
      fileInputRef.current.value = null;
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Your Resume (PDF only)</h2>

      <div
        className="drop-zone"
        onDrop={handleDrop}
        onDragOver={handleDragOver}
      >
        {file ? (
          <p>
            Selected file: <strong>{file.name}</strong>
          </p>
        ) : (
          <p>Drag & drop your PDF here</p>
        )}
      </div>

      <p className="or-text">or</p>

      <input
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
        ref={fileInputRef}
      />

      {error && <p className="error">{error}</p>}

      <button onClick={handleSubmit} disabled={!file}>
        Upload Resume
      </button>
    </div>
  );
};

export default Upload;
