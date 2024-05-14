import tensorflow as tf
import numpy as np

# Training data: temperatures in Celsius and corresponding in Fahrenheit.
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

# Model traininghistory = model.fit(celsius, fahrenheit, epochs=5000, verbose=True)
print("Trained model!")

# Model testing
test_c = 100
predicted_f = model.predict([test_c])
print(f"{test_c} Celsius are {predicted_f[0][0]} Fahrenheit.")
