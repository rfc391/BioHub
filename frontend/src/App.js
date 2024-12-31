
import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { ThemeProvider, createTheme } from '@mui/material';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const theme = createTheme({
  palette: {
    primary: { main: '#2196f3' },
    secondary: { main: '#f50057' },
  },
});

const dropzoneStyles = {
  container: {
    border: '2px dashed #ccc',
    borderRadius: '4px',
    padding: '20px',
    textAlign: 'center',
    cursor: 'pointer',
    marginBottom: '20px'
  },
  resultContainer: {
    border: '1px solid #ccc',
    borderRadius: '4px',
    padding: '20px',
    whiteSpace: 'pre-wrap'
  },
  wrapper: {
    padding: '20px',
    maxWidth: '800px',
    margin: '0 auto'
  }
};

function App() {
  const [loading, setLoading] = useState(false);
  const [markdown, setMarkdown] = useState('');

  const onDrop = useCallback(async (acceptedFiles) => {
    setLoading(true);
    const formData = new FormData();
    formData.append('file', acceptedFiles[0]);

    try {
      const response = await fetch('http://0.0.0.0:3000/convert', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      if (!data.success) throw new Error(data.error);
      setMarkdown(data.markdown);
    } catch (error) {
      alert(error.message);
    } finally {
      setLoading(false);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <ThemeProvider theme={theme}>
      <div style={dropzoneStyles.wrapper}>
        <h1>Office to Markdown Converter</h1>
        
        <div {...getRootProps()} style={dropzoneStyles.container}>
          <input {...getInputProps()} />
          {loading ? <p>Converting...</p> :
           isDragActive ? <p>Drop the file here...</p> :
           <p>Drag and drop a file here, or click to select a file</p>}
        </div>

        {markdown && (
          <div style={dropzoneStyles.resultContainer}>
            <h2>Converted Markdown:</h2>
            <pre>{markdown}</pre>
          </div>
        )}
        <ToastContainer />
      </div>
    </ThemeProvider>
  );
}

export default App;
