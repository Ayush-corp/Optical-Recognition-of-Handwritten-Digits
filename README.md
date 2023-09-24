Certainly, here's a detailed README file for your GitHub repository, excluding the code:

# Handwritten Character Recognition - CPSC 585 Group 8 Project

Welcome to the CPSC 585 Group 8 Project on Handwritten Character Recognition! This repository contains the code and documentation for our project. 

## Introduction

In this project, we aim to tackle the challenging problem of handwritten character recognition using deep learning techniques. We explore the use of convolutional neural networks (CNNs) to accurately identify and classify handwritten characters.

## Dataset

We use the Extended MNIST (EMNIST) dataset, which is an extension of the popular MNIST dataset. EMNIST contains a more diverse set of handwritten characters, making it suitable for our project. The dataset comprises high-resolution grayscale images of handwritten characters.

## Usage

### Environment Setup

Before running the code in this repository, ensure you have the necessary Python environment set up with libraries such as TensorFlow, Matplotlib, and scikit-learn installed. You can find the list of required packages in the code's import statements.

### Running the Code

1. Clone this repository to your local machine.
2. Open the Jupyter Notebook file, `CPSC-585-01-Introductory_Project.ipynb`, in a Jupyter Notebook environment.
3. Execute the code cells step by step to understand the data loading, preprocessing, model creation, training, and evaluation process.

## Project Structure

Here's an overview of the key components and files in this repository:

- `CPSC-585-01-Introductory_Project.ipynb`: The main Jupyter Notebook containing the code for the project. It covers data loading, model creation, training, and evaluation.
- `README.md`: This README file providing an overview of the project, dataset, and instructions for usage.
- `LICENSE`: The project's license file (MIT License).

## Results

### Part 1: Model Training on EMNIST

In the Jupyter Notebook, we first explore the dataset, visualize some sample images, and split the data into training and testing sets. We then create a neural network model with two hidden layers of 512 nodes each and train it for 20 epochs. The results are as follows:

- Model Accuracy on Test Set: 97% (accuracy may vary based on your specific run)

### Part 2: Manual Predictions

We also implement manual predictions using the trained model's weights and biases. This allows us to make predictions on test images directly from the model's parameters. We compare these manual predictions with predictions made by the Keras model.

## Contributors

This project was developed by the following contributors:

- Ayush Bhardwaj
- Ken Cue
- Chris Freeland
- Gordon Huynh
- Anthony Hernandez
- Tina Torabinejad

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms specified in the [LICENSE](LICENSE) file.

Feel free to explore the code in the Jupyter Notebook and use it as a reference for your own handwritten character recognition projects. If you have any questions or feedback, please don't hesitate to contact us.

Happy coding!
