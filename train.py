from utils import predict, fit, get_data_from_csv, get_mileage_from_user

def main():
    trainX, trainY = get_data_from_csv("data.csv")
    theta0, theta1 = fit(trainX, trainY, 0, 0, 0.0001, 10000)
    print(f'Theta0: ${theta0}, Theta1: ${theta1}')
    mileage = get_mileage_from_user()
    print(f"The predicted price of the car is: ${predict(mileage, theta0, theta1)}")
    
        
if __name__ == "__main__":
    main()