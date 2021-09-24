import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
#--------------------------------------------------------
dataset=pd.read_csv('D:\\Study\\UdemyData Sci\\Data.csv')
# print(dataset)
x=dataset.iloc[:,:-1].values    #locate indexes,all colnmn except last one
y=dataset.iloc[:,-1].values     #last colmn only
# print(y)
# print(x)      #before-containing nan i.e null

#--------------------------------------------------------

# MISSING DATA-missing value replace by mean value -1st & 2nd colmn
impute=SimpleImputer(missing_values=np.nan,strategy='mean')
impute.fit(x[:,1:3])
(x[:,1:3])=impute.transform(x[:,1:3])
# print(x)


#--------------------------------------------------------

#ENCODING CATGORICAL DATA
#ENCODING INDEPEDANT VAR.
# convert cntry clmn into binary value.

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
#country colmn encoded i.e 0,1
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],
                      remainder='passthrough')
x=np.array(ct.fit_transform(x))
# print(x)

#ENCODING DEPEDANT VAR.
# convert purchsd clmn into binary value.
from sklearn.preprocessing import LabelEncoder
labl=LabelEncoder()
y=labl.fit_transform(y)
# print(y)

#-----------------------------------------------------------------

# Spliting the data into train & test dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,
                    random_state=1)#0.2 means 20% of test data from table
# print('x train=', x_train)
# print('x test=',x_test)
# print('\ny train=',y_train)
# print('y test=',y_test)


#-----------------------------------------------------------------
# feature scaling has two method
# 1]standardisation
# 2] normalisation

from sklearn.preprocessing import StandardScaler
sclr=StandardScaler()
x_train[:,3:]=sclr.fit_transform(x_train[:,3:])
x_test[:,3:]=sclr.transform(x_test[:,3:])
print('feature scaling of train ',x_train)
print("")
print('feature scaling of train ',x_test)

#-----------------------------------------------------------------











