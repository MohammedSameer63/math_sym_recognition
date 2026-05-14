# Handwritten Mathematical Symbol Recognition using CNN

A deep learning mini-project that recognizes handwritten mathematical symbols using a Convolutional Neural Network (CNN).

The project allows users to draw mathematical symbols on a canvas and predicts the symbol in real time using a trained CNN model.

Supported Symbols:

```text
+, −, ×, ÷, =, ∫, Σ
```

---

# Features

* Handwritten symbol recognition using CNN
* Real-time prediction GUI using Tkinter
* Trained on HASYv2 handwritten symbols dataset
* Simple and lightweight implementation
* Easy to train and extend for more symbols

---

# Tech Stack

* Python 3
* TensorFlow / Keras
* OpenCV
* NumPy
* Pandas
* Tkinter
* PIL (Pillow)

---

# Project Structure

```text
Handwritten-Math-Symbol-Recognizer/
│
├── app.py                 # GUI application
├── train.py               # Model training script
├── model.py               # CNN architecture
├── data_loader.py         # Dataset loading & preprocessing
├── math_symbol_model.h5   # Trained model
├── requirements.txt
├── .gitignore
│
├── hasy-data/             # Dataset folder (download separately)
│
└── README.md
```

---

# Dataset

Dataset used: **HASYv2**

Download from:

[HASYv2 Dataset](https://zenodo.org/record/259444?utm_source=chatgpt.com)

After downloading:

1. Extract the dataset
2. Rename/extract folder as:

```text
hasy-data/
```

3. Place it inside the project root directory.

Final structure:

```text
project-folder/
│
├── hasy-data/
├── train.py
├── app.py
└── ...
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd Handwritten-Math-Symbol-Recognizer
```

---

## 2. Create Virtual Environment (Recommended)

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Training the Model

Run:

```bash
python train.py
```

This will:

* Load dataset
* Preprocess images
* Train CNN model
* Save trained model as:

```text
math_symbol_model.h5
```

---

# Running the Application

Run:

```bash
python app.py
```

---

# How to Use

1. Draw a mathematical symbol on the canvas
2. Click **Predict**
3. View predicted symbol

Use **Clear** button to reset canvas.

---

# CNN Architecture

The model contains:

* Convolution Layer
* Max Pooling Layer
* Convolution Layer
* Max Pooling Layer
* Flatten Layer
* Dense Layer
* Output Layer (Softmax)

Input image size:

```text
32 × 32 × 1
```

---

# Model Training Details

* Optimizer: Adam
* Loss Function: Categorical Crossentropy
* Activation Function:

  * ReLU
  * Softmax
* Epochs: 10
* Batch Size: 32

---

# Output Example

```text
Prediction: ∫
Confidence: 94.2%
```

---

# Future Improvements

* Support more mathematical symbols
* Recognize complete equations
* Improve accuracy with more training
* Deploy as web application
* Add equation parsing

---

# Authors

```text
Mohammed Sameer
Mohammed Suhail
Rithvik
Ullas Gowda M
```

---

# Academic Information

Mini Project for:

```text
Machine Learning (BCS602)
Department of Computer Science & Engineering
Bangalore Institute of Technology
Academic Year: 2025-26
```
