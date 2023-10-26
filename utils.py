import pandas as pd

def predict(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def fit(X, Y, theta0, theta1, learningRate, nbIteration):
    m = X.shape[0]
    for _ in range(nbIteration):
        theta0, theta1 = gradientDescent(m, X, Y, theta0, theta1, learningRate)
        
    return theta0, theta1

def gradientDescent(m, X, Y, theta0, theta1, learningRate):
    gradientTheta0 = 0
    gradientTheta1 = 0
    for i in range(m):
        prediction = predict(X[i], theta0, theta1)
        gradientTheta0 += prediction - Y[i]
        gradientTheta1 += (prediction - Y[i]) * X[i]
        
    gradientTheta0 = learningRate * (gradientTheta0 / m)
    gradientTheta1 = learningRate * (gradientTheta1 / m)
    
    theta0 = theta0 - gradientTheta0
    theta1 = theta1 - gradientTheta1
    return theta0, theta1

def getMileageFromUser():
    mileage = input("Please enter the mileage of the car: ")
    try:
        mileage = int(mileage)
        if (mileage < 0):
            raise ValueError() 
        print(f"The mileage input is: {mileage}")
        return mileage
    except ValueError as exc:
        print("Please enter a positive number for mileage")
        exit(1)

def getThetasFromCsv(filename):
    data = pd.read_csv(filename)
    
    try:
        if (data.theta0.__len__() != 1 or data.theta1.__len__() != 1):
            raise Exception()
        return data.theta0[0], data.theta1[0]
    except Exception:
        print("Don't change the format of the csv file.")
        exit(1)
        
def getDatasetFromCsv(filename):
    data = pd.read_csv(filename)
    
    try:
        if (data.km.__len__() <= 10 or data.price.__len__() <= 10):
            raise Exception
        return data.km / 1000, data.price / 1000
    except Exception:
        print("Don't change the format of the csv file.")
        exit(1)     