from utils import getDatasetFromCsv, getThetasFromCsv, calcCost
import matplotlib.pyplot as plt

def main():
    X, Y = getDatasetFromCsv("data.csv")
    X = X
    Y = Y

    theta0, theta1 = getThetasFromCsv('thetas.csv')
    cost = calcCost(X, Y, theta0 / 1000, theta1)
    print(f"The cost value is: {cost}")
    
        
if __name__ == "__main__":
    main()