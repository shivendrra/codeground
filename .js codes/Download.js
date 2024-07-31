const { execFile } = require('child_process');
const path = require('path');

function downloadAudio(videoUrl, outputPath) {
  const pythonScriptPath = path.resolve(__dirname, 'download_audio.py');
  const pythonExecutable = 'python';

  execFile(pythonExecutable, [pythonScriptPath, videoUrl, outputPath], (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${stderr}`);
      return;
    }
    console.log(`Output: ${stdout}`);
  });
}

// Usage
const videoUrl = 'https://youtu.be/Z-mKF5CqncY?si=ldSKBYQFX5CSyqu9';
const directory = path.resolve(__dirname, 'downloads');
downloadAudio(videoUrl, directory);