from utils.script_generator import generate_script
from utils.category_detector import detect_category
from utils.voice_generator import generate_voice
from utils.music_selector import select_music
from utils.video_creator import create_video

def run_pipeline(images, product_name, custom_script=None, custom_music=None,
                 image_duration=2, text_duration=3):

    category = detect_category(images[0])

    # Script
    if custom_script:
        script = custom_script
    else:
        script = generate_script(product_name, category)

    # Voice
    voice_path = "output/voice.mp3"
    generate_voice(script, voice_path)

    # Music
    if custom_music:
        music_path = custom_music
    else:
        music_path = select_music(category)

    output_video = "output/final_ad.mp4"

    create_video(
        images,
        script,
        voice_path,
        music_path,
        output_video,
        image_duration,
        text_duration
    )

    return output_video, script, category