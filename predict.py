import csv
from utils import getMileageFromUser, getThetasFromCsv, predict


def main():
    mileage = getMileageFromUser()
    theta0, theta1 = getThetasFromCsv('thetas.csv')
    print(f"The predicted price of the car is: ${predict(mileage, theta0, theta1)}")

if __name__ == "__main__":
    main()