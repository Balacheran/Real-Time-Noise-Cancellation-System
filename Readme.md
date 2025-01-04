# Real-Time Noise Cancellation System

## Overview

The Real-Time Noise Cancellation System is a Python-based project that uses audio processing techniques to perform real-time noise cancellation. This system captures audio input, processes it to reduce noise, and then outputs the processed audio with significantly reduced noise.

## Features

- Real-time audio processing with low latency
- Supports both single-speaker and multi-speaker noise cancellation scenarios
- Customizable noise reduction levels
- Simple and efficient implementation using Python and PyAudio
- Interactive control via Streamlit UI

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- Python 3.6 or later
- PyAudio
- Numpy
- Librosa
- Scipy

You can install the required packages using the following command:
```bash
pip install -r requirements.txt
```

## File Structure

The project contains the following files and directories:

```
Real-Time-Noise-Cancellation-System/
│
├── filters/
│   ├── __init__.py
│   ├── single_speaker.py
│   ├── multi_speaker.py
│
├── utils/
│   ├── __init__.py
│   ├── audio_utils.py
│
├── src/
│   ├── main.py
│   ├── audio_processor.py
│   ├── noise_cancellation.py
│
├── output_audio/
│
└── README.md
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Balacheran/Real-Time-Noise-Cancellation-System.git
   cd Real-Time-Noise-Cancellation-System/src
   ```

2. Run the  app:
   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to control the noise cancellation process. You can select between single-speaker and multi-speaker scenarios and adjust the noise reduction level using the sidebar controls.

## Code Explanation

### main.py

This is the main entry point of the project. It initializes the `AudioProcessor`, captures audio input in chunks, processes the audio for noise cancellation, and saves the processed audio to a file.

### audio_processor.py

This file contains the `AudioProcessor` class, which handles the initialization, starting, stopping, and processing of audio streams. It applies the noise cancellation filter and writes the processed audio to the output stream.

### noise_cancellation.py

This file contains the noise cancellation functions. It uses the Short-Time Fourier Transform (STFT) to analyze the audio signal and reduce noise based on a noise profile.

### utils/utils.py

This file contains utility functions for audio processing, such as calculating the root mean square (RMS) of audio data and trimming silence from audio data.

### filters/single_speaker.py and filters/multi_speaker.py

These files contain the noise cancellation filters for single-speaker and multi-speaker scenarios, respectively.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. Your contributions are welcome!

