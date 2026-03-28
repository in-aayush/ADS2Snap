#!/bin/bash

echo "🚀 Setting up AdForge AI..."

# Create folders
mkdir -p input output output/temp assets/music assets/fonts assets/logos utils core tests

# Create empty python files
touch app.py main.py README.md
touch requirements.txt

# Utils files
touch utils/__init__.py
touch utils/script_generator.py
touch utils/category_detector.py
touch utils/color_extractor.py
touch utils/feature_generator.py
touch utils/voice_generator.py
touch utils/music_selector.py
touch utils/subtitle_generator.py
touch utils/scoring.py
touch utils/video_creator.py

# Core files
touch core/__init__.py
touch core/pipeline.py
touch core/config.py

