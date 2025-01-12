import pandas as pd 
import numpy as np 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, recall_score
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, recall_score
import pickle


df = pd.read_csv('/home/ali/Desktop/ML-CICD/smart_web/Smart_Web_2/app/model/titanic.csv')
df = df[['Pclass','Sex','Age','Embarked','Survived']]
df.Sex.replace(['male', 'female'], [0, 1], inplace=True)
df.Embarked.replace(['S', 'C', 'Q'], [0, 1, 2], inplace=True)
df.Age.fillna(df.Age.mean(), inplace=True)
df.Embarked.fillna(df.Embarked.mode()[0], inplace=True)
x = df[['Pclass','Sex','Age','Embarked']]
y = df['Survived']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
lr_model = LogisticRegression( max_iter=1000, C=1, solver='lbfgs')
lr_model.fit(x_train, y_train)
pred = lr_model.predict(x_test)


with open("/home/ali/Desktop/ML-CICD/smart_web/Smart_Web_2/app/model/model.pkl", "wb") as file:
    pickle.dump(lr_model, file)
