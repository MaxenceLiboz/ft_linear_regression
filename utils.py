import csv
import numpy as np

def predict(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def fit(trainX, trainY, theta0, theta1, learningRate, nbIteration):
    m = trainX.shape[0]
    thetaTmp0 = 0
    thetaTmp1 = 0
    for _ in range(nbIteration):
        for i in range(m):
            prediction = predict(trainX[i], theta0, theta1)
            thetaTmp0 += prediction - trainY[i]
            thetaTmp1 += prediction * trainX[i]
        
        thetaTmp0 = learningRate * (thetaTmp0 / m)
        thetaTmp1 = learningRate * (thetaTmp1 / m)
        
        theta0 = theta0 - thetaTmp0
        theta1 = theta1 - thetaTmp1
    
    return theta0, theta1

def get_mileage_from_user():
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

def get_thetas_from_csv(filename):
    try:
        file = open(filename)
        csvreader = csv.reader(file)

        headers = []
        thetas = []

        headers = next(csvreader)
        if (headers.__len__ != 2 or headers[0] != "theta0" or headers[1] != "theta1"):
            raise Exception("Ne changez pas le format du fichier thetas.csv")

        for row in csvreader:
            if (row.__len__() != 2):
                raise Exception("Ne changez pas le format du fichier thetas.csv")
            thetas.append(row[0])
            thetas.append(row[1])
            break


        theta0 = int(thetas[0])
        theta1 = int(thetas[1])
        if (theta0 < 0 or theta1 < 0):
            raise ValueError()

        file.close()
        return theta0, theta1
    except ValueError:
        print("Les thetas doivent être des nombres positifs")
        exit(1)
    except Exception as exc:
        print(exc)
        exit(1)
        
def get_data_from_csv(filename):
    try:
        file = open(filename)
        csvreader = csv.reader(file)

        headers = []
        trainXTmp = []
        trainYTmp = []


        headers = next(csvreader)
        if (headers.__len__() != 2 or headers[0] != "km" or headers[1] != "price"):
            raise Exception("Ne changez pas le format du fichier data.csv")
        
        for row in csvreader:
            if (row.__len__() != 2):
                raise Exception("Ne changez pas le format du fichier data.csv")
            trainXTmp.append(int(row[0]) / 1000)
            trainYTmp.append(int(row[1]) / 1000)

        file.close()
        
        trainX = np.array(trainXTmp)
        trainY = np.array(trainYTmp)
        return trainX, trainY
        
    except ValueError:
        print("Les thetas doivent être des nombres positifs")
        exit(1)
    except Exception as exc:
        print(exc)
        exit(1)     