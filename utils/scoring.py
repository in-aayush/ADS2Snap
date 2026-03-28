import random

def ad_score():
    return {
        "Creativity": random.randint(8, 10),
        "Visual Appeal": random.randint(7, 10),
        "Engagement": random.randint(7, 10),
        "Conversion Potential": random.randint(6, 10)
    }