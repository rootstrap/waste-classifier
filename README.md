# waste-classifier

# Reference paper

We take as starting point the following paper: [Fine-Tuning Models Comparisons on Garbage Classification for
Recyclability](https://arxiv.org/pdf/1908.04393.pdf)

## Data

Dataset: TrashNet dataset 
Which contains 6 classes: 
501 glass, 594 paper, 403 cardboard, 482 plastic, 410 metal, 137 trash


## Process
The main objective of the paper is to de develop a deep learning application which detects types of garbage into trash in order to
provide recyclability with vision system.
They used half of the data for training and the other half for testing. Applying transfer learning the training and test processes were shorter and with higher accuracy. The fine-tuned models used were Alexnet,
VGG16, Googlenet and Resnet. The classifiers 
used in the last layer were Softmax and Support Vector Machines. 

## Final Results
The highest accuracy was reached with GoogleNet and SVM as 97.86%. 

# Our process

The idea is to try some of the neural networks used in this paper in order to reuse it and adapt the algorithm for our case.

# Install
  ```bash
     virtualenv -p python3 venv
     source venv/bin/activate
     pip install -r requirements.txt
     # unzip dataset-resized.zip
     python -c 'import split_data; split_data.split_data()'
  ```

# Start jupyter notebook
  ```bash
     jupyter notebook
  ```
  
# Models  

## ResNet50
A Residual Neural Network (ResNet) introduces "skip connections" that makes the network to skip one or more layers. The idea is to add layers as residual blocks. Generally the network contains nonlinear layers (ReLU) and batch normalizaiton between. The case of ResNet50 corresponds to a convolutional network with 50 layers. Using tensorflow library, we are able to load a pre-trained version of the model trained over the ImageNet dataset. 

Therefore, we use the output from ResNet50 as input of a new network. The network adds the following layers:    
- average pooling layer: in order to resize the image in base on the average.      
- flatten: to transform the image dimension to only a vector.     
- dense: applying the activation function relu.     
- dropout: to generate different architectures during iterations.      
- dense: with 6 nodes, since are 6 classes, applying softmax to get the final class.      



  



