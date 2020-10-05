import numpy as np #Generate Data
import random #Generate Data
#To Split the Data
from sklearn.model_selection import train_test_split
#To Apply Linear regression
from sklearn.linear_model import LinearRegression
import matplotlib #Plotting
from matplotlib import pyplot as plt

#Choosing the Style to be used
matplotlib.use('TkAgg')

#Make Random Numbers Predictable
np.random.seed(42)

#Generating Ages
random_ages = [random.randint(20,60) for _ in range(100)]

'''
Generate Net Worth
Draw Random Samples from Guassian Distribution
Scale to define width of distribution
'''
random_net_worth = [age * 6.25 + np.random.normal(scale=40.) \
                    for age in random_ages]

#Converting Lists to NumPy Arrays
random_ages = np.reshape(
                np.array(random_ages),
                (len(random_ages),1),
                )
random_net_worth = np.reshape(
                np.array(random_net_worth),
                (len(random_net_worth),1),
                )

#Splitting Data into training an testing Sets
age_train,age_test,net_worth_train,net_worth_test = train_test_split(
   random_ages, random_net_worth
    )

#Create Regression Object
reg_obj = LinearRegression()

#Train Model
reg_obj.fit(age_train,net_worth_train)

#Print Slope, Intercept
print(reg_obj.coef_)
print(reg_obj.intercept_)

#Get R-Squared Score - Trained Data
print("Training Data:",reg_obj.score(age_train,net_worth_train))

#Get R-Squared Score - Test Data
print("Test Data:",reg_obj.score(age_test,net_worth_test))

#Plot Graph - Age, Predicted NetWorth
plt.scatter(age_train,net_worth_train,color='b',label="Train Data") #Train Data
plt.scatter(age_test,net_worth_test,color='r',label="Test Data") #Test Data
plt.plot(age_test,reg_obj.predict(age_test),color="black") #Predicted Data


#Set X-Axis, Y-Axis Labels
plt.xlabel("Ages")
plt.ylabel("Net Worth")

#Show the Plot
plt.show()
