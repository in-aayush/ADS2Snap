import random

def generate_script(product, category):

    hooks = [
        "🔥 Limited Time Offer!",
        "⚡ Trending Now!",
        "💥 Don’t Miss This!"
    ]

    bodies = [
        f"Upgrade your life with {product}.",
        f"Experience the power of {product}.",
        f"{product} is designed just for you."
    ]

    ctas = [
        "Shop Now!",
        "Buy Today!",
        "Order Before It’s Gone!"
    ]

    return f"{random.choice(hooks)} {random.choice(bodies)} {random.choice(ctas)}"