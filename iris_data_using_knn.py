# -*- coding: utf-8 -*-
"""Iris_data-using_KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YbOQ2Vd_xZZ0DyySq8-9S8MB2cb8DK8r
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

iris=pd.read_csv('Iris.csv')
iris.head()

iris['Species'].value_counts() #balanced data

#let's print scatter plot
#iris.plot(kind='scatter',x="SepalLengthCm",y="SepalWidthCm")
#plt.show()
sns.scatterplot(x="SepalLengthCm", y="SepalWidthCm", hue="Species",style="Species", size=4, data=iris,legend='brief')

"""DataWrangling"""

file_handler = open("Iris.csv", "r")
d= pd.read_csv(file_handler, sep = ",") 
file_handler.close()
Species = {'Iris-setosa': 1,'Iris-virginica': 2,'Iris-versicolor': 3} 
d.Species= [Species[item] for item in d.Species] 
iris=d
iris.head(5)

iris.drop("Id",axis=1,inplace=True)
iris.head(5)

iris.isnull().sum()

# for later use this can also be used. Just for reference
#model.fit(iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']], iris[['Species']]
#y_pred = model.predict(X_test)
#print(metrics.accuracy_score(y_test, y_pred))

"""Test and Train and Model"""

X=iris.drop("Species",axis=1)
y=iris["Species"]
print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

print(X_train.shape)
print(X_test.shape)

X_train.head(5)

X_test.head(5)

print(y_train.shape)
print(y_test.shape)

y_train.head(5)

y_test.head(5)

from matplotlib.colors import ListedColormap

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA','#00AAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00','#00AAFF'])

from sklearn.neighbors import KNeighborsClassifier

model=KNeighborsClassifier(n_neighbors=5)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred) #predicted species

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,y_pred)) #evaluate our knn model

print(classification_report(y_test,y_pred)) #classification report

from sklearn.metrics import accuracy_score

prediction=model.predict(X_test)

w=accuracy_score(y_test,prediction)*100
print(w,'%')