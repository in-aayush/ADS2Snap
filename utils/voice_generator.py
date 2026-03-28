import pyttsx3

def generate_voice(text, output_path, voice_type="female"):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if voice_type == "female" and len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 150)

    engine.save_to_file(text, output_path)
    engine.runAndWait()