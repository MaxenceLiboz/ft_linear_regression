import csv
from utils import getMileageFromUser, getThetasFromCsv, predict, getDatasetFromCsv
import matplotlib.pyplot as plt



def main():
    # Get the thetas, run the prediciton
    theta0, theta1 = getThetasFromCsv('thetas.csv')
    print(f'theta0: {theta0}, theta1: {theta1}')
    mileage = getMileageFromUser()
    predictedValue = predict(mileage, theta0, theta1)
    print(f"The predicted price of the car is: {predictedValue}")

    # Create a graph with all values, the linear regression line and the point predicted
    X, Y = getDatasetFromCsv("data.csv")
    X = X * 1000
    Y = Y * 1000
    plt.scatter(mileage, predictedValue, color='red')
    plt.scatter(X, Y)
    plt.plot(list(range(250000)), [predict(x, theta0, theta1) for x in range(250000)])
    plt.show()

if __name__ == "__main__":
    main()