# SVM

Support Vector Machine for Data Classification — A Simple Take
Dimosthenis Tsormpatzoudis
Dimosthenis Tsormpatzoudis

Dec 29, 2020




![alt text](https://miro.medium.com/max/2400/1*N5tEKi0Z0DpzleJX-ep9RA.png)
1. Introduction
What it is a SVM? A supervised learning model used for classification and regression analysis. Developed at AT&T Bell Labs at 1992. SVM models construct hyperplanes in a multidimensional environment in order to be able to separate the data. A common practice is to use more dimensions than the original data.
The vital point is to determine where to place the hyperplane to achieve the maximum accuracy.

![alt text](https://miro.medium.com/max/700/1*pqd5IGshad6X05CKQhnMsQ.png)

As we can see in the example, both the blue and the red line are correctly separating our data. But which line is better at predicting the class of new point and how we can determine that? The answer is by calculating the lines’ margins.

2. Implementation
 
A great way for a beginner to quickly learn how to implementate a SVM model and try it on a data set is with the sklearn.svm.SVC library. It offers many options and parameters to tweak in order to achieve the desired result.
The most common parameters the user can change is the kernel as seen below, the C parameter and the gamma.

![alt text](https://miro.medium.com/max/640/1*0xzZ8XUF0XGD9l_ORkfTrA.png)

3. C Regularization Parameter

The C parameter exchange the correct classification of points in the training set to achieve the maximum margin. A low value of C will result in a large margin and a simpler decision. A high value of C will result in a small margin.

![alt text](https://miro.medium.com/max/700/1*HhFggpUdCd2l1nOq6RcNHg.png)

As we can see from the graph, the maximum accuracy in the testing set is achieved when the C has a value of 0.1 . When the training set accuracy rises higher than this point the accuracy of the testing starts to fall. This is a result of overfitting, meaning that the SVM model has a small margin created to fit to the training model but it cannot perform the same in different data.

4. Gamma parameter

The gamma parameter determines the influence a single point reaches. A low gamma value means that a point has a big influence and it will taken into account when trying to determine another point’s class even if this points is far away. A high gamma value means that a point’s impact is short distanced. On one hand a low gamma value will result in a oversimplification and not being able to tell apart classes. On the other hand high values will prevent the model from being able to determine more complex shapes.
![alt text](https://miro.medium.com/max/700/1*3oTPcQGkr_aqJ-1HXV_xUg.png)

We observe from the graph that the maximum accuracy can be achieved at a medium value of gamma.

5. Advantages and Disadvantages

SVM models have many advantages that a programmer can take into account.
Can perform in a high dimensional environment.
It can separate data both linear and non-linear.
It is memory efficient compared to other techniques.
SVM models also have some disadvantages that the user must be careful of.
Parameters tweaking can be time consuming.
It cannot perform well on noisy data.
Probability estimates slow down the calculations.

6. Conclusion

Having a good knowledge of SVM models and how they work can be a valuable asset for a Data analyst. Learning how to efficient handle it’s parameters can be helpful for Data classification purposes. Programmers must always be aware of the details of their data so they can choose the method and it’s parameters that fit their needs properly.
