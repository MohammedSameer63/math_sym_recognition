from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

def create_model():
    model = Sequential()

    model.add(Conv2D(32, (3,3), activation='relu', input_shape=(32,32,1)))
    model.add(MaxPooling2D(2,2))

    model.add(Conv2D(64, (3,3), activation='relu'))
    model.add(MaxPooling2D(2,2))

    model.add(Flatten())

    model.add(Dense(128, activation='relu'))
    model.add(Dense(7, activation='softmax'))

    return model