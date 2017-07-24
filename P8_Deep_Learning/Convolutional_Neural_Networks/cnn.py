# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution (Layer 1 - Convolution Layer)
classifier.add(Convolution2D(32, 3, 3, # 32 feature detactors which are 3x3 matrices
                             input_shape = (64, 64, 3), # 3 colums for colored pics (TensorFlow Backend order)
                             activation = 'relu'))

# Step 2 - Max Pooling the feature maps (Layer 2 - Pooling Layer)
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding one extra convolution layer and max pooling layer to increase the accuraccy
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening (input layer of a future ANN) - converting the matrices to single-column-vectors
classifier.add(Flatten())

# Step 4 - Full Connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid')) # sigmoid for binary outcome, SoftMax for more than 2 outcomes

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', # for more than 2 outcomes, use catergorical_crossentropy
                   metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator 
# Rescale all values to [0, 1], shear rotate the images, zoom images and horizontally flip images
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                target_size=(64, 64), # consistant with input_shape of convolution layer
                                                batch_size=32,
                                                class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit_generator(training_set,
                         steps_per_epoch=8000,
                         epochs=25,
                         validation_data=test_set,
                         validation_steps=2000)












