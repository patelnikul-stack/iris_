import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn 
from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split
from  sklearn.metrics import confusion_matrix,accuracy_score,classification_report 
from sklearn.svm import SVC 
import warnings
warnings.filterwarnings('ignore')
print('library imported sucessfully')




i=load_iris()
df=pd.DataFrame(i.data,columns=i.feature_names)
df['species']=i.target

print(df.head())

print('')

from scipy.stats import zscore
z=np.abs(zscore(df))
dfn=df[(z<3).all(axis=1)]
print(df.shape,dfn.shape)


x=dfn.iloc[:,:-1]
y=dfn.iloc[:,-1]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.30,random_state=46)
print(x_test.shape,y_test.shape)

svc=SVC()
svc.fit(x_test,y_test)

pred=svc.predict(x_test)
print(accuracy_score(y_test,pred))

import joblib as j
j.dump(svc,'svc.pkl')
print('model  saved')