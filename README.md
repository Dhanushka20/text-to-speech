# Text to Speech Application

This Python-based application converts text input into speech using the Google Text-to-Speech (gTTS) library. Users can test the speech output directly from the application and save the generated audio as an MP3 file.

## Features

- Convert text to speech in multiple languages.
- Test the speech output within the application.
- Save the generated speech as an MP3 file.

## Requirements

- Python 3.x
- `tkinter` (for GUI)
- `gTTS` (for text-to-speech conversion)
- `mpg123` (for playing audio on Unix-based systems)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/text-to-speech-app.git
    cd text-to-speech-app
    ```

2. Install the required Python packages:
    ```sh
    pip install gtts
    ```

3. (Optional) Install `mpg123` for Unix-based systems (Linux, macOS) to play audio:
    ```sh
    # For Ubuntu/Debian-based systems
    sudo apt-get install mpg123

    # For macOS using Homebrew
    brew install mpg123
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. Enter text in the input field.

3. Select the desired language from the dropdown menu.

4. To test the speech output:
    - Click the "Test Speech" button. The application will convert the text to speech and play the audio.

5. To save the speech as an MP3 file:
    - Click the "Save Audio" button.
    - Choose the file location and name to save the MP3 file.

## Supported Languages

- English (`en`)
- Sinhala (`si`)
- Tamil (`ta`)


