from utils import predict, fit, getDatasetFromCsv, getMileageFromUser
import matplotlib.pyplot as plt
import pandas as pd

def main():
    X, Y = getDatasetFromCsv("data.csv")
    
    theta0, theta1 = fit(X, Y, 0, 0, 0.0001, 200000)
    print(f'theta0: {theta0}, theta1: {theta1}')

    
    thetas = { "theta0": [theta0 * 1000],
               "theta1": [theta1]}
    dataFrame = pd.DataFrame(thetas)
    dataFrame.to_csv("thetas.csv")

    plt.scatter(X * 1000, Y * 1000)
    plt.plot(list(range(250000)), [predict(x, theta0 * 1000, theta1) for x in range(250000)])
    plt.show()
        
if __name__ == "__main__":
    main()