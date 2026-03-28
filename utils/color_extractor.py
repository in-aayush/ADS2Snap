import cv2
import numpy as np

def get_dominant_color(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (100, 100))

    data = img.reshape((-1, 3))
    data = np.float32(data)

    _, _, palette = cv2.kmeans(
        data, 1, None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0),
        10, cv2.KMEANS_RANDOM_CENTERS
    )

    color = palette[0]
    return tuple(map(int, color))