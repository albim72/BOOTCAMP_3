import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

cm = ['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima = pd.read_csv('diabetes.csv',header=None,names=cm)
print(pima.head())

feature_cols = ['pregnant','insulin','bmi','age','glucose','bp','pedigree']
X = pima[feature_cols]
y = pima.label

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)

print(X_train.shape)

clf = DecisionTreeClassifier(max_depth=4)
clf = clf.fit(X_train,y_train)

y_pred = clf.predict(X_test)
print(f"dokładność - accuracy: {metrics.accuracy_score(y_test,y_pred)}")
