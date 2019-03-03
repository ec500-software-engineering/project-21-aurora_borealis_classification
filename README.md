# aurora borealis classification
## Sprint 1

### User stories 
1. We want to distinguish between a binary classification aurora and no aurora.
2. We want to predict the category of unseen auroral images based on extracted features.

### Definition of First Sprint
* Project Goal:
	* Detect aurora in the picture
	* Predict the categories of aurora
		* Arc: Image that one or multiple bands ofaurora
		- Diffuse: Images that show large patches of aurora, typically with fuzzy edges.
		- Discrete: The images show auroral forms with well‐defined, sharp edges.
		- Cloudy: The sky in these images is dominated by clouds or the dome of the imager is covered with snow.
		- Moon: The image is dominated by light from the Moon.
		* Clear  /Noaurora: images which show a clear sky without the appearance of aurora.
- Conduct machine learning and deep neural network researches
- Get familiar with Tensorflow
- Get the data set: (THEMIS all‐sky imager network. http://themis.ssl.berkeley.edu.)
- Design API 
- Complete project infrastructure

### Definition of the modular architecture of first sprint

### Technologies to be used in first sprint selected with clear reasons why they were chosen
1. Tensorflow: 

Since the entire project is designated for python implementation, tensorflow has well features and objects provided to python, including nodes and tensors. While tensorflow is able to train and run deep neural network, it's also the most fit for image recognition and classfication. Since our project conducts heavy machine learning and deep neural network(DNN), tensorflow is going to be our core technology to complete the project. 
	
2. Ridge Classification: 

This feature includes feature extraction and inception-v4 checkpoint from tensorflow. The method chose to calculate the weights by using the strategy regularization. Thus the program yeilds the highest possibility of the image within the categories. The benefit of this implementation is that the training and prediction could be evaluated within short lines of code but to maximize the efficiency. 
	
3. Dataset: 

Oslo Auroral THEMIS (OATH) Data Set is our top choice. It's originated by Clausen & Nickisch. It not only contains easy .csv classification format, but also provides training, validation and test sets. Auroral classification contains 6 categories. Basic installations are python 3, git, wget and imagemagick. The following photo is the directory structure of the file
![alt text](https://github.com/ec500-software-engineering/project-aurora_borealis_classification/blob/master/dataset%20structure.png)

4. Training environment: 

Testing purpose: Google Colaboratory

This is one of the best and easy access tool to do machine learning or data science project. It functions just like jupitor notebook which is easier to debug or test functionalities for our code. For testing purpose, I can directly import data from google drive or directly from my local computer, as well as import the dataset. It's able to manipulate simple testing on our model, but since it has limited gpu usage, it's not good to process entiere dataset training here. 
			
Dataset training purpose: Amazon AWS

We are aiming to use Amazon AWS such as SageMaker, EC2 tools to build, train and deploy our model in cloud. We plan to run on instance in AWS with several GPU options to use. 

### APIs of first sprint
1. Keras: 

Keras is a high level API build on Tensorflow, this library is specifically designed to build and train deep learning models. Since our approach is to train model using Convolutional Neural Network(CNN). There are two main targets we are aiming to import from Keras, Sequential as model type and Dense as layer type. Sequential is the easiest way to build a model because it allows you to add layers. Dense is just standard layer that we can specify nodes, activations relu and size of the input images. 

### Task assignments









