import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# 1. Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()[0]

# 2. Normalize pixel values to (0-255 --> 0-1)
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])
# 4. Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# 5. Train the model
model.fit(x_train, y_train, epochs=5)

# 6. Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print('\nTest accuracy:', test_acc)

# 7. Make predictions
predictions = model.predict(x_test)

# 8. Display a sample prediction
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}, Actual: {y_test[0]}")
plt.show()
