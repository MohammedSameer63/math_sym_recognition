from data_loader import load_data
from model import create_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

X, y = load_data()

y = to_categorical(y, 7)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = create_model()

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_data=(X_test, y_test)
)

model.save("math_symbol_model.h5")