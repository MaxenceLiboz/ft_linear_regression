from utils import predict, fit, getDatasetFromCsv, getMileageFromUser
import matplotlib.pyplot as plt

def main():
    X, Y = getDatasetFromCsv("data.csv")
    
    plt.scatter(X, Y)
    plt.show()
    
    # theta0, theta1 = fit(X, Y, 0, 0, 0.0001, 10000)
    # print(f'Theta0: ${theta0}, Theta1: ${theta1}')
    # mileage = getMileageFromUser()
    # print(f"The predicted price of the car is: ${predict(mileage, theta0, theta1)}")
    
        
if __name__ == "__main__":
    main()