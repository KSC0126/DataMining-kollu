
'''libraries imported'''
import matplotlib.pyplot as plt
import pandas as pd

'''pandas is used to read a csv file'''
set=pd.read_csv("dataset.csv")

'''x and y axis have intrest and home price stored respectively'''
x=set.iloc[:, :-1].values
y=set.iloc[:, 1].values

''' importing training and testing datasets.'''
from sklearn.cross_validation import train_test_split
'''importing linear regression'''
from sklearn.linear_model import LinearRegression

''' datasets are splitted by 0.2 as train and test data seta'''
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.3,random_state=0)
''' Linear regression is performed.'''
r= LinearRegression()
''' it is fit into train dataset'''
r.fit(x_train,y_train)

''' predicts the result.'''
y_pred = r.predict(x_test)

''' scatter and plot testing data set values'''
plt.scatter(x_test,y_test,color='red')
plt.plot(x_test,y_pred,color='green')
plt.xlabel('intrest rate')
plt.ylabel('median home price')
plt.title('median home price vs intrest rate')
plt.show()
'''scatter and plot training dataset values'''
plt.scatter(x_train,y_train, color = 'blue')
plt.plot(x_test,y_pred,color = 'green')
plt.xlabel('intrest rate')
plt.ylabel('median home price')
plt.title('median home price vs intrest rate')
plt.show()



