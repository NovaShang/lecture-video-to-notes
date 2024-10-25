from moviepy.editor import VideoFileClip
import whisper
import sys
import os
import openai

model = whisper.load_model("turbo")
#model = whisper.load_model("turbo", device="cuda")
client = openai.Client(
    api_key="PUT_YOUR_OPEN_AI_API_KEY_HERE"
)
prompt = """
I have a rough transcript of a lecture from a video. The transcript has some quality issues, and I need it cleaned up and organized into clear, well-structured notes using Markdown. Please do the following:
1. Organize the transcript into key sections and subsections based on the lecture content.
2. Use bullet points or numbered lists for important information, where appropriate.
3. Create headings (e.g., ## Main Topics, ### Subtopics) to structure the content logically.
4. Include any key quotes, examples, or references mentioned in the lecture, formatted properly in Markdown.
The goal is to turn the rough transcript into a concise, easy-to-read set of notes. Your response can up to {token} tokens long.
"""


def extract_audio(video_path, audio_path):
    print("Extracting audio from video...")
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path, codec="mp3")
    print("Audio extracted successfully, saved at: ", audio_path)


def speech_to_text(audio_path, text_path):
    print("Extracting text from audio...")
    result = model.transcribe(audio_path, verbose=True)
    with open(text_path, "w") as f:
        f.write(result["text"])
    print("Text extracted from audio, saved at: ", text_path)


def text_to_note(text_path, note_path):
    print("Generating notes from text...")
    with open(text_path, "r") as f:
        text = f.read()
    word_count = len(text.split())
    max_tokens = word_count * 0.5
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt.replace("{token}", str(max_tokens))},
            {"role": "user", "content": text},
        ],
        max_tokens=int(max_tokens),
    )
    with open(note_path, "w") as f:
        f.write(response.choices[0].message.content)
    print("Notes generated from text, saved at: ", note_path)


def main(video_path):
    dir = os.path.dirname(video_path)
    audio_path = os.path.join(dir, os.path.basename(video_path).split(".")[0] + ".mp3")
    text_path = os.path.join(dir, os.path.basename(video_path).split(".")[0] + ".txt")
    note_path = os.path.join(dir, os.path.basename(video_path).split(".")[0] + ".md")
    extract_audio(video_path, audio_path)
    speech_to_text(audio_path, text_path)
    text_to_note(text_path, note_path)


if __name__ == "__main__":
    for video_path in sys.argv[1:]:
        main(video_path)
