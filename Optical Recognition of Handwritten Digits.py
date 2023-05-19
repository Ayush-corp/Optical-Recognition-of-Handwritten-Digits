# -*- coding: utf-8 -*-
"""CPSC-585-01-Introductory_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Ss9n5RVquZHzTP4bz2HdwKzAn0CnRC4

# Importing necessary packages
"""

import numpy as np
import random as r
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits

"""# Load the Dataset"""

# Load Digits Data
digits = load_digits()
print(digits.data.shape)

# Plotting any image for checking 
plt.matshow(digits.images[6])
plt.show()

# Checking the Type of dataset
type(digits)

# Printing out the Target Names
digits.target_names

# Printing out the dataset 
digits_as_frame = load_digits(as_frame=True)
digits_as_frame.data

"""## Splitting the dataset into Train Data and Test Data"""

X,Y = digits.data, digits.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

"""## Checking the Train Dataset"""

print(type(X_train))
print(X_train.shape)
X_train

print(Y_train.shape)
Y_train

X_train.shape[1]

Y_train.shape

"""## Reshaping using one hot encoding for Train and Test labels."""

y_train = to_categorical(Y_train, num_classes=10)
y_test = to_categorical(Y_test, num_classes=10)

"""# Task 1

## Creating a Model using keras with 2 Hidden Layers of 512 Nodes
"""

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='softmax'))

"""## Compiling the model using the categorical cross-entropy loss function, the adam optimizer, and accuracy as the evaluation metric."""

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

"""## Printing Model Summary"""

model.summary()

"""## Training the model for 20 epochs with batch size of 64 and evaluating the model."""

# Train the model
batch_size = 64
epochs = 20
history = model.fit(X_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(X_test, y_test))

"""## Print the test loss and accuracy"""

# Evaluate the model on the test set
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

"""## Predicting the test data by the model."""

Model_Predict = model.predict(X_test)

"""# Task 2

## Getting Weights and Bias Vector from Model's get_weights method
"""

w1,b1,w2,b2,w3,b3 = model.get_weights()
weight_bias_list = [[w1,b1],[w2,b2],[w3,b3]]

"""## Checking out the Weight and Bias data """

print(w1.shape)
print(b1.shape)
print(w2.shape)

"""## Function Softmax(z) that takes in a vector z and returns the softmax of that vector.

"""

def softmax(z):
  exp_z = np.exp(z)
  return exp_z / exp_z.sum()

"""## Rectified Linear Unit (ReLU) activation function in Python

"""

def relu(z):
  return np.maximum(0, z)

"""## Performing forward propagation by computing the dot product of the weight and input matrices, adding bias, and applying a non-linear activation function like ReLU or softmax to the result. 
## Transposing the matrices for matrix multiplication.
"""

def predict(input):
  for i,e in enumerate(weight_bias_list):
    temp = np.dot(np.transpose(e[0]), input) + e[1]
    if i == len(weight_bias_list) - 1:
      input = softmax(temp)
      return np.argmax(input)
    input = relu(temp)

"""## Testing the Predict Method on Test Data"""

predict(X_test[1])

Y_test[1]

print(predict(X_test[1]) == Y_test[1])

"""# Task 3

## Plotting the 1st image using Matlib library
"""

plt.matshow(X_test[0].reshape(8,8))

"""## Actual Label for the above image"""

Y_test[0]

"""## Predicted Output for the above image using Predict method"""

predict(X_test[0])

"""## Predicted Output for the above image using the Keras Model"""

np.argmax(Model_Predict[0])

"""## Trying to compare Multiple images and their outputs from both the Models and also trying to plot the image.
## Since Matlib plot is running asynchronously, the images are getting plotted in the end.bold text
"""

for i in range(2):
  j = r.randrange(len(X_test))
  plt.matshow(X_test[j].reshape(8,8))
  print(f"Image {i+1}")
  print(Y_test[j])
  print(predict(X_test[j]))
  print(np.argmax(Model_Predict[j]))

"""## Printing out the Accuracy for both Models"""

model_true_count, predict_true_count = 0, 0

for i in range(len(X_test)):
  model_true_count += 1 if Y_test[i] ==  np.argmax(Model_Predict[i]) else 0
  predict_true_count += 1 if Y_test[i] ==  predict(X_test[i]) else 0
print(f"Keras Model Accuracy : {model_true_count/len(X_test)}")
print(f"Manual Predict Model Accuracy : {predict_true_count/len(X_test)}")
