# Brain_Tumor_Detection
Building a detection model using a convolutional neural network in Tensorflow & Keras.<br>
Used a brain MRI images data founded on Kaggle. You can find it [here](https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection).<br>

**About the data:**<br>
The dataset contains 2 folders: yes and no which contains 253 Brain MRI Images. The folder yes contains 155 Brain MRI Images that are tumorous and the folder no contains 98 Brain MRI Images that are non-tumorous.

# Getting Started

## Data Preprocessing

For every image, the following preprocessing steps were applied:

1. Crop the part of the image that contains only the brain (which is the most important part of the image).
2. Resize the image to have a shape of (240, 240, 3)=(image_width, image_height, number of channels): because images in the dataset come in different sizes. So, all images should have the same shape to feed it as an input to the neural network.
3. Apply normalization: to scale pixel values to the range 0-1.

## Data Split:

The data was split in the following way:
1. 70% of the data for training.
2. 15% of the data for validation.
3. 15% of the data for testing.

# Neural Network Architecture

I have used Transfer Learning with Resnet50 architecture as my focus was more on making an end to end application:

![Neural Network Architecture](res50![res50](https://user-images.githubusercontent.com/58721376/172156227-be7c8abd-5068-4f4b-bd50-ba00ea80537e.png)
.png)

**Understanding the architecture:**<br>
Each input x (image) has a shape of (240, 240, 3) and is fed into the neural network. And, it goes through the following layers:<br>

1. A Zero Padding layer with a pool size of (2, 2).
2. A convolutional layer with 32 filters, with a filter size of (7, 7) and a stride equal to 1.
3. A batch normalization layer to normalize pixel values to speed up computation.
4. A ReLU activation layer.
5. A Max Pooling layer with f=4 and s=4.
6. A Max Pooling layer with f=4 and s=4, same as before.
7. A flatten layer in order to flatten the 3-dimensional matrix into a one-dimensional vector.
8. A Dense (output unit) fully connected layer with one neuron with a sigmoid activation (since this is a binary classification task).


# Training the model
The model was trained for 50![Accuracy](https://user-images.githubusercontent.com/58721376/172156520-ff6a6e19-88e7-4889-b6e2-ead0bc24d919.png)
![Loss](https://user-images.githubusercontent.com/58721376/172156526-619d0f60-d7f1-455a-9780-00315c7b5133.png)
 epochs and these are the loss & accuracy plots:


![Loss plot](Loss.PNG)


![Accuracy plot](Accuracy.PNG)

# Results

Best Validation Accuracy: 0.8889
Best Validation Loss: 0.4237

**Performance table of the best model:**

# Final Notes

What's in the files?

1. The code in the IPython notebooks.
2. The weights file of the model.
3. Files needed for deploying the model locally using flask.
4. The original data in the folders named 'yes' and 'no'.


Contributes are welcome!
<br>Thank you!


