def generate_features(product):

    words = product.split()

    return [
        f"Premium {words[0]} Quality",
        "High Performance",
        "Best in Class Design"
    ]