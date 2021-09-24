import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

data=pd.read_csv('D:/Study/Udemy/Udemy-ML/Regression/Machine Learning A-Z'
               ' (Codes and Datasets)/Part 2 - Regression/Section 4 - '
               'Simple Linear Regression/Python/Salary_Data.csv')
x=data.iloc[:,:-1].values #all rows with 2nd colmn (except last colmn)
# x=data.iloc[1:10,:-1] # 1st 10 rows
# x=data.iloc[5:,-2] # take values from above 5th row of 2nd last colmn ind. var
y=data.iloc[:,-1].values #last colmn dep. var
#print(x)
#print(y)

#-----------------------------------------------------------------
# Spliting the data into train & test dataset
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=1/3,random_state=0)
# print(xtrain)
#print(xtest)        # 6 value
#print(ytrain)
#print(ytest)      # 6 value

#-----------------------------------------------------------------------------
           #Training the smpl lin.regr. model on train set
from sklearn.linear_model import LinearRegression
regrsr=LinearRegression()
regrsr.fit(xtrain,ytrain)       #fit method work on both set

#-----------------------------------------------------------------------------
            #Predecting the test set result
#ytest contain actual sal & ypred contain predicted sal.
y_predict=regrsr.predict(xtest)
#-----------------------------------------------------------------------------
#             visualiz traing  set
# pt.scatter(xtrain,ytrain,color='r')
# pt.plot(xtrain,regrsr.predict(xtrain),color='b')
# pt.title('Salary over yr.s of Exp(Train)')
# pt.xlabel('Exp. in yr')
# pt.ylabel('Salary in rs')
# pt.show()

#           visualiz  test set
# pt.scatter(xtest,ytest,color='r')
# pt.plot(xtrain,regrsr.predict(xtrain),color='b')#we kept x train pred. line for refrnce
# pt.title('Salary over yr.s of Exp(Test)')
# pt.xlabel('Exp. in yr')
# pt.ylabel('Salary in rs')
# pt.show()

#-----------------------------------------------------------------------------
         #  Making  single prediction if y=12 yr ,salary=?

print('Salary of 12 yr:',regrsr.predict([[12]])) #the "predict" method always expects a 2D array as the format of its inputs. And putting 12
# into a double pair of square brackets makes the input exactly a 2D array.

#-----------------------------------------------------------------------------
         # lin. regr. eq. with the values of the coefficients
print('\n regression equation coefficient is', regrsr.coef_)
print('\n regression equation intrecept is',regrsr.intercept_)





