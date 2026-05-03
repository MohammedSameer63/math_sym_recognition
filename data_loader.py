import pandas as pd
import cv2
import numpy as np
import os

DATA_PATH = "hasy-data"

TARGET_SYMBOLS = {
    "+": 0,
    "-": 1,
    "\\times": 2,
    "\\div": 3,
    "=": 4,
    "\\int": 5,
    "\\sum": 6
}

def load_data():

    labels_df = pd.read_csv(f"{DATA_PATH}/hasy-data-labels.csv")
    symbols_df = pd.read_csv(f"{DATA_PATH}/symbols.csv")

    # Merge on symbol_id
    df = labels_df.merge(symbols_df, on="symbol_id")

    X = []
    y = []

    for _, row in df.iterrows():
        latex = row['latex_y']

        if latex in TARGET_SYMBOLS:
            img_path = os.path.join(DATA_PATH, row['path'])

            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            img = cv2.resize(img, (32, 32))
            img = img / 255.0

            X.append(img)
            y.append(TARGET_SYMBOLS[latex])

    X = np.array(X).reshape(-1, 32, 32, 1)
    y = np.array(y)

    return X, y