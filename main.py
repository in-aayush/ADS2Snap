from core.pipeline import run_pipeline

if __name__ == "__main__":

    image_path = "input/img1.jpg"
    product_name = "Smart Watch"

    video, script, category = run_pipeline(image_path, product_name)

    print("\n✅ Ad Generated Successfully!")
    print(f"📦 Product: {product_name}")
    print(f"📂 Category: {category}")
    print(f"🧠 Script: {script}")
    print(f"🎬 Output Video: {video}")