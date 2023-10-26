import csv
from utils import get_mileage_from_user, get_thetas_from_csv, predict


def main():
    mileage = get_mileage_from_user()
    theta0, theta1 = get_thetas_from_csv('thetas.csv')
    print(f"The predicted price of the car is: ${predict(mileage, theta0, theta1)}")

if __name__ == "__main__":
    main()