# Lecture Video to Notes

## Overview

This script can generate markdown notes from a video lecture. It uses the moviepy library to extract audio from the video and openAI's whisper speech-to-text model to transcribe the audio. Finally, it use openai's GPT api to generate notes from the transcript.

## Prerequisites

- Python 3.9 or higher
- OpenAI API key: you can get one at openai.com, the payment is based on the number of tokens generated
- ffmpeg: it should be installed and added to the path environment variable

## Environment

### macOS

Since Apple Silicons GPU are not supported, the speed of speech-to-text maybe slow.

You can install ffmpeg using homebrew.

### Windows

I recommend using WSL2 to run the script. If you have a Nvidia GPU, use cuda to accelerate the speech-to-text.

## Installation

If you are familiar with these stuff, just copy the code and do what you want.

1. Clone the repository and install the dependencies, you can use a virtual environment.

```bash
git clone https://github.com/novashang/lecture-video-to-notes.git
cd lecture-video-to-notes
pip install -r requirements.txt
```

2. Modify the `main.py` file to add your openAI API key.

## Usage

```bash
python main.py path/to/video.mp4
```

You can use path/to/*.mp4 to process multiple videos at once.

## Output

After running the script, you will these files in the video files' directory:

- `[filename].txt`: the transcript of the video
- `[filename].md`: the notes generated from the transcript
- `[filename].mp3`: the audio extracted from the video

## Remarks

It's not a mature tool, just a simple script to automate the process. You are free to modify it to fit your needs.

I know it's hard to set up the environment. If a lot of people are interested, I will create a docker image to simplify the process.


# Example Output:

You can find an example of the generated notes [here](./examples/CEE226-2020-10.md).