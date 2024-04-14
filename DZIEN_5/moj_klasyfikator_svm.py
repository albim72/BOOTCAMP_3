from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#Standardyzacja danych
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#implementacja kalsyfikatora SVM

class SVM:
    def __init__(self,learning_rate = 0.01, lambda_param = 0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        #f(x)=w*x+b - w - wektor wag, x - wektor cech próbki, b - bias (przesunięcie w przestrzeni 2D)
        self.w = None
        self.b = None

    #Ustawienie wartości (x,y), zdefiniowanie w oraz b jako 0(startowo)
    #wykonaie n iteracji (1000)
    #aktualizacja wag i bias metodą algorytmu optymalizacji gradientowej(stochastyczny spadek gradientu)


    def fit(self,X,y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0
        for _ in range(self.n_iters):
            for idx,x_i in enumerate(X):
                condition = y[idx]*(np.dot(x_i,self.w)-self.b) >=1
                if condition:
                    self.w -= self.lr*(2*self.lambda_param*self.w)
                else:
                    self.w -= self.lr*(2*self.lambda_param*self.w - np.dot(x_i,y[idx]))
                    self.b -= self.lr*y[idx]

    def predict(self,X):
        approx = np.dot(X,self.w) - self.b
        return np.sign(approx)

svm_classifier = SVM(learning_rate=0.0001,lambda_param=0.0001, n_iters=10000)
svm_classifier.fit(X_train,y_train)

#predykcja
y_pred = svm_classifier.predict(X_test)

#ewaluacja modelu
accuracy = np.mean(y_pred == y_test)
print(f"dokładność klasyfikacji: {accuracy*100:.2f} %")
