import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import pickle
from sklearn.pipeline import Pipeline


df = pd.read_csv("E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/clean_dataset.csv")

print(df.head())

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['tweet'], df['label'], random_state=70)
"""print("x train")
print(X_train)
print("x test")
print(X_test)
print("y train")
print(y_train)
print("y test")
print(y_test)"""
#cv=CountVectorizer()
#traincv=cv.fit_transform(["HI how are you doing","hey whatsup","we are ready?"])
#print(traincv.toarray())
#print(cv.get_feature_names())
#x_traincv=cv.fit_transform(X_train)
#a=x_traincv.toarray()
#print(a[0])

#print(cv.inverse_transform(a[0]))
#below line represent fit and transform
model = Pipeline([("vect", CountVectorizer()),("clf",LogisticRegression())])

model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)
print('AUC: ', roc_auc_score(y_test, predictions))

filename = 'E:/academic/ganesh moodle material/6th semester/ISS/project/implementation/dataset/clean_model.csv'
joblib.dump(model, filename)

#with open(filename,'wb') as f:
  #  pickle.dump(model, f)
#with open(filename,'rb') as f:
 #  re=pickle.load(f)
