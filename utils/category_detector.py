def detect_category(image_path):
    name = image_path.lower()

    if any(word in name for word in ["shoe", "shirt", "watch"]):
        return "fashion"
    elif any(word in name for word in ["phone", "laptop", "earbuds"]):
        return "electronics"
    else:
        return "general"