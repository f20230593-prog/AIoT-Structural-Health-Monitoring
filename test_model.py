import numpy as np
from tensorflow import keras

print("Loading model...")

model = keras.models.load_model("shm_model.keras")

print("Model loaded successfully")
model.summary()

x = np.random.rand(1, 64, 10)

print("Running prediction...")
prediction = model.predict(x)

print("Prediction successful")
print(prediction)