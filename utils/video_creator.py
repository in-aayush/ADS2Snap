from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Create text image using PIL (NO ImageMagick)
def create_text_image(text, size=(720, 1280)):
    img = Image.new("RGB", size, color="black")
    draw = ImageDraw.Draw(img)

    # Use default font
    font = ImageFont.load_default()

    # Wrap text manually
    lines = []
    words = text.split()
    line = ""

    for word in words:
        if len(line + word) < 25:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    y = 500
    for l in lines:
        draw.text((50, y), l, fill="white", font=font)
        y += 40

    return np.array(img)


def create_video(images, text, voice_path, music_path, output_path,
                 image_duration=2, text_duration=3):

    clips = []

    # Image clips
    for img in images:
        clip = ImageClip(img).set_duration(image_duration)
        clip = clip.resize(lambda t: 1 + 0.1*t)
        clips.append(clip)

    # Text clip using PIL
    text_img = create_text_image(text)
    txt_clip = ImageClip(text_img).set_duration(text_duration)

    clips.append(txt_clip)

    final = concatenate_videoclips(clips, method="compose")

    # Audio
    voice = AudioFileClip(voice_path)

    if music_path:
        music = AudioFileClip(music_path).volumex(0.2)
        final_audio = CompositeAudioClip([voice, music])
    else:
        final_audio = voice

    final = final.set_audio(final_audio)

    final.write_videofile(output_path, fps=24)