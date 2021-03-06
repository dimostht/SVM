# -*- coding: utf-8 -*-
"""SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zcTLd2suXm4SJIQLYajPqmuO4j2kFvQj
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets
import matplotlib.pyplot as plt 
import time
from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import seaborn

# mnist datasets of pictures of 10 digits from Keras datasets
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# we turn the dimensions from (_,28,28) to (_,784)
train_images = train_images.reshape(-1, 784)
test_images = test_images.reshape(-1, 784)

# devide the values by 255 to make them in range 0-1
train_images , test_images = train_images/255.0 , test_images/255.0

# show these images
plot = plt.figure()

for i in range(10):
    im_idx = np.argwhere(train_labels == i)[0]
    img = np.reshape(train_images[im_idx], (28, 28))
    ax = plot.add_subplot(2, 5, i+1)
    ax.imshow(img, cmap='gray_r')

# we want to identify between odd and even numbers
# so we change the labels by 0,1,2,3,4.. to 0 or 1
test_labels = [x%2 for x in test_labels]
train_labels = [x%2 for x in train_labels]

t0 = time.time()
# create a scaler
scaler = StandardScaler()
# scale the data 
scaler.fit(train_images)
train_images_scaled = scaler.transform(train_images)
test_images_scaled = scaler.transform(test_images)
# keep 90 % of the information
pca = PCA(0.9)
pca.fit(train_images_scaled)

# create the new data sets with reduced dimensions
train_images_reduced = pca.transform(train_images_scaled)
test_images_reduced = pca.transform(test_images_scaled)

print("Dimensional reduction completed in %0.3fs" % (time.time() - t0))
print("Reduced from ",len(train_images[0])," to ",len(train_images_reduced[0])," dimensions.")

t0 = time.time()
# a non linear support vector classification model with the other
model1 = SVC(kernel='rbf')

# fit
model1.fit(train_images_reduced, train_labels)

# predict
y_pred1_ts = model1.predict(test_images_reduced)
acc1_ts = metrics.accuracy_score(y_true=test_labels, y_pred=y_pred1_ts)
y_pred1_tr = model1.predict(train_images_reduced)
acc1_tr = metrics.accuracy_score(y_true=train_labels, y_pred=y_pred1_tr)

print("Testing accuracy:", acc1_ts, "\n")
print("Training accuracy:", acc1_tr, "\n")
print("done in %0.3fs" % (time.time() - t0))

pred = y_pred1
cm = metrics.confusion_matrix(test_labels, pred)
plt.subplots(figsize=(10, 6))
seaborn.heatmap(cm, annot = True, fmt = 'g',cmap="coolwarm")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

t0 = time.time()
# a linear support vector classification model C = 10 and gamma = 0.001
model2 = SVC(kernel='rbf',C=10, gamma=0.001)

# fit
model2.fit(train_images_reduced, train_labels)

# predict
y_pred2_ts = model2.predict(test_images_reduced)
acc2_ts = metrics.accuracy_score(y_true=test_labels, y_pred=y_pred2_ts)
y_pred2_tr = model2.predict(train_images_reduced)
acc2_tr = metrics.accuracy_score(y_true=train_labels, y_pred=y_pred2_tr)

print("Testing accuracy:", acc2_ts, "\n")
print("Training accuracy:", acc2_tr, "\n")
print("done in %0.3fs" % (time.time() - t0))

t0 = time.time()
# a polynomial support vector classification model
model3 = SVC(kernel='poly')

# fit
model3.fit(train_images_reduced, train_labels)

# predict
y_pred3_ts = model3.predict(test_images_reduced)
acc3_ts = metrics.accuracy_score(y_true=test_labels, y_pred=y_pred3_ts)
y_pred3_tr = model3.predict(train_images_reduced)
acc3_tr = metrics.accuracy_score(y_true=train_labels, y_pred=y_pred3_tr)

print("Testing accuracy:", acc3_ts, "\n")
print("Training accuracy:", acc3_tr, "\n")
print("done in %0.3fs" % (time.time() - t0))

# in order for the next culculations to run we reduce the data
train_images2 = train_images[:2000]
train_labels2 = train_labels[:2000]
test_images2 = test_images[:400]
test_labels2 = test_labels[:400]

t0 = time.time()

c_list = [0.0001,0.001,0.01,0.1,1,10,100,1000,10000]
# linear model for various C values
acc_linear = []
acc_tr = []
for c in c_list:
    svm = SVC(kernel='linear', C = c)
    svm.fit(train_images2, train_labels2)
    
    p_tr = svm.predict(train_images2)
    a_tr = metrics.accuracy_score(train_labels2, p_tr)
    
    pred = svm.predict(test_images2)
    a = metrics.accuracy_score(test_labels2, pred)
    
    acc_tr.append(a_tr)
    acc_linear.append(a)
  
print("Linear models with different regularization parameter values")
print("done in %0.3fs" % (time.time() - t0))

print(acc_linear)
# plotting the test and train accuracy of the models
plt.subplots(figsize=(10, 5))
plt.semilogx(c_list, acc_linear,'-gD' ,color='red' , label="Testing Accuracy")
plt.semilogx(c_list, acc_tr,'-gD' ,color='blue', label="Training Accuracy")
plt.grid(True)
plt.xlabel("Cost Parameter C")
plt.ylabel("Accuracy")
plt.legend()
plt.title('Accuracy - Regularization parameter C ')
plt.show()

t0 = time.time()
# non-linear model for various gamma values
gamma_list = [0.00001 , 0.0001, 0.001, 0.01, 0.1, 1, 10]

acc_rbf = []
acc_tr = []
for g in gamma_list:
    svm = SVC(kernel='rbf', C = 10 ,gamma=g)
    svm.fit(train_images2, train_labels2)
    
    p_tr = svm.predict(train_images2)
    a_tr = metrics.accuracy_score(train_labels2, p_tr)
    
    pred = svm.predict(test_images2)
    a = metrics.accuracy_score(test_labels2, pred)
    
    acc_tr.append(a_tr)
    acc_rbf.append(a)
  
print("Non linear models with different gamma parameter values")
print("done in %0.3fs" % (time.time() - t0))

print(acc_rbf)
# plotting the test and train accuracy of the models
plt.subplots(figsize=(10, 5))
plt.semilogx(gamma_list, acc_rbf,'-gD' ,color='red' , label="Testing Accuracy")
plt.semilogx(gamma_list, acc_tr,'-gD' ,color='blue', label="Training Accuracy")
plt.grid(True)
plt.xlabel("Gamma Parameter")
plt.ylabel("Accuracy")
plt.legend()
plt.title('Accuracy - Gamma Parameter')
plt.show()