import streamlit as st
from core.pipeline import run_pipeline
from utils.scoring import ad_score

st.set_page_config(page_title="AdForge AI", layout="centered")

st.title("🚀 AdForge AI")
st.subheader("Create Stunning Ads Instantly")

# Upload multiple images
uploaded_files = st.file_uploader(
    "📤 Upload Product Images",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)

product_name = st.text_input("🛍️ Enter Product Name")

# Custom script
custom_script = st.text_area("✍️ Write Custom Script (Optional)")

# Custom music
music_file = st.file_uploader("🎵 Upload Custom Music (Optional)", type=["mp3", "wav"])

# Time controls
st.markdown("### ⏱️ Adjust Timing")
image_duration = st.slider("Image Duration (seconds)", 1, 5, 2)
text_duration = st.slider("Text Duration (seconds)", 2, 6, 3)

if st.button("🎬 Generate Ad"):

    if uploaded_files and product_name:

        image_paths = []

        # Save images
        for i, file in enumerate(uploaded_files):
            path = f"input/img_{i}.jpg"
            with open(path, "wb") as f:
                f.write(file.read())
            image_paths.append(path)

        # Save custom music
        if music_file:
            music_path = "assets/music/custom.mp3"
            with open(music_path, "wb") as f:
                f.write(music_file.read())
        else:
            music_path = None

        with st.spinner("Generating your ad... 🔥"):

            video, script, category = run_pipeline(
                image_paths,
                product_name,
                custom_script=custom_script,
                custom_music=music_path,
                image_duration=image_duration,
                text_duration=text_duration
            )

            scores = ad_score()

        st.success("✅ Ad Generated!")

        st.video(video)

        st.markdown("### 🧠 Script Used")
        st.write(script)

        st.markdown(f"### 📂 Category: {category}")

        st.markdown("### 📊 Ad Score")
        st.json(scores)

    else:
        st.warning("⚠️ Upload images and enter product name")