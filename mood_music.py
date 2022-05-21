import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

data = pd.read_csv('training_cases.csv')
print(data)

X = data.drop(columns=['mood'])
y = data['mood']