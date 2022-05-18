#import the packges
import matplotlib.pyplot as plt
import pandas as pd
#Read Dataset
dataset=pd.read_csv("hours.csv")
#index read 
x=dataset.iloc[:,:-1].values  #slice all column
y=dataset.iloc[:,1].values  #last Column

#import packages of LR
from sklearn.linear_model import LinearRegression
regressor=LinearRegression() #create object of LR

# Fit Function
regressor.fit(x,y)

#score Function
Accuracy=regressor.score(x,y)*100
print('Accuracy')
print(Accuracy)

#Predict Function
y_pred=regressor.predict([[10]])
print(y_pred)

#input from user
hours=int(input("Enter the no of hours"))

# Coefficient 
# intercept
eq=regressor.coef_*hours+regressor.intercept_
print("Risk Score",eq[0])

plt.plot(x,y,'o')
plt.plot(x,regressor.predict(x));
plt.show()






