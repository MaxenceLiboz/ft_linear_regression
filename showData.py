from utils import getDatasetFromCsv, getThetasFromCsv, predict
import matplotlib.pyplot as plt

def main():
    X, Y = getDatasetFromCsv("data.csv")
    X = X * 1000
    Y = Y * 1000

    theta0, theta1 = getThetasFromCsv('thetas.csv')
    if (theta0 and theta1):
        plt.plot(list(range(250000)), [predict(x, theta0, theta1) for x in range(250000)])

    plt.scatter(X, Y)
    plt.show()
    
        
if __name__ == "__main__":
    main()