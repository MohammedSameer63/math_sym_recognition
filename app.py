import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
import cv2
from tensorflow.keras.models import load_model

model = load_model("math_symbol_model.h5")

LABELS = ["+", "-", "×", "÷", "=", "∫", "Σ"]

# Create canvas
width, height = 200, 200
image = Image.new("L", (width, height), color=255)
draw = ImageDraw.Draw(image)

def paint(event):
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    canvas.create_oval(x1, y1, x2, y2, fill="black")
    draw.ellipse([x1, y1, x2, y2], fill=0)

def clear():
    canvas.delete("all")
    draw.rectangle([0, 0, width, height], fill=255)
    result_label.config(text="")

def predict():
    img = np.array(image)
    img = cv2.resize(img, (32, 32))
    img = img / 255.0
    img = img.reshape(1, 32, 32, 1)

    pred = model.predict(img)
    symbol = LABELS[np.argmax(pred)]

    result_label.config(text=f"Prediction: {symbol}")

# UI
root = tk.Tk()
root.title("Handwritten Math Symbol Recognizer")
root.configure(bg="white")

# Title
# title = tk.Label(
#     root,
#     text="Handwritten Math Symbol Recognizer",
#     font=("Helvetica", 18, "bold"),
#     bg="white",
#     fg="#222"
# )
# title.pack(pady=10)

# Canvas frame (centered look)
canvas_frame = tk.Frame(root, bg="white")
canvas_frame.pack(pady=10)

canvas = tk.Canvas(
    canvas_frame,
    width=width,
    height=height,
    bg="white",
    bd=2,
    relief="solid",
    highlightthickness=0
)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

# Buttons frame
btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=10)

btn_predict = tk.Button(
    btn_frame,
    text="Predict",
    command=predict,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    width=10,
    relief="flat"
)
btn_predict.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(
    btn_frame,
    text="Clear",
    command=clear,
    bg="#f44336",
    fg="white",
    font=("Arial", 12),
    width=10,
    relief="flat"
)
btn_clear.grid(row=0, column=1, padx=10)

# Result label
result_label = tk.Label(
    root,
    text="Draw a symbol and click Predict",
    font=("Arial", 14),
    bg="white",
    fg="#333"
)
result_label.pack(pady=15)

root.mainloop()