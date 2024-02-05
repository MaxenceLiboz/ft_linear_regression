import pandas as pd
import math

# The cost function used here is the Mean Squared Error
def calcCost(X, Y, theta0, theta1):
    sum = 0
    for i in range(len(Y)):
        x = X[i]
        y = Y[i]
        prediction = predict(x, theta0, theta1)
        sum += (prediction - y) ** 2

    cost = sum / (2 * len(Y))
    return cost

def predict(mileage, theta0, theta1):
    return (theta0 + (theta1 * mileage))

def fit(X, Y, theta0, theta1, learningRate, epochs):
    m = X.shape[0]
    cost = 0
    for i in range(epochs):
        if i % 50000 == 0:
            print(f"Epochs: {i} / {epochs}")
            print(f"Cost: {cost}")
        cost = calcCost(X, Y, theta0, theta1)
        theta0, theta1 = gradientDescent(m, X, Y, theta0, theta1, learningRate)
        
    return theta0, theta1

def gradientDescent(m, X, Y, theta0, theta1, learningRate):
    gradientTheta0 = 0
    gradientTheta1 = 0
    for i in range(m):
        prediction = predict(X[i], theta0, theta1)
        gradientTheta0 += prediction - Y[i]
        gradientTheta1 += (prediction - Y[i]) * X[i]
    
    gradientTheta0 = learningRate * gradientTheta0 / m
    gradientTheta1 = learningRate * gradientTheta1 / m
    
    theta0 = theta0 - gradientTheta0
    theta1 = theta1 - gradientTheta1
    return theta0, theta1

def getMileageFromUser():
    while True:
        mileage = input("Please enter the mileage of the car: ")
        try:
            mileage = int(mileage)
            if mileage < 0:
                raise ValueError("Mileage must be a non-negative number.")
            print(f"The mileage input is: {mileage}")
            return mileage
        except ValueError as exc:
            print("Please enter a positive number for mileage")

def getThetasFromCsv(filename):
    data = pd.read_csv(filename)
    
    try:
        if (data.theta0.__len__() != 1 or data.theta1.__len__() != 1
            or math.isnan(data.theta0[0]) or math.isnan(data.theta1[0])):
            raise Exception()
        return float(data.theta0[0]), float(data.theta1[0])
    except Exception:
        print("Don't change the format of the csv file.")
        exit(1)


def getDatasetFromCsv(filename):
    try:
        data = pd.read_csv(filename)   
            
        if (data.km.__len__() <= 0 and data.price.__len__() <= 0):
            raise Exception
        
        for km in data.km:
            int(km)
        for price in data.price:
            int(price)
        return data.km / 1000, data.price / 1000
    except Exception as e:
        print("Don't change the format of the csv file.")
        exit(1)     