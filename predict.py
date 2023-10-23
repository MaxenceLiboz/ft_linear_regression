import csv

def predict(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def main():
    mileage = input("Please enter the mileage of the car: ")
    try:
        mileage = int(mileage)
        if (mileage < 0):
            raise ValueError() 
        print(f"The mileage input is: {mileage}")
    except ValueError as exc:
        print("Please enter a positive number for mileage")
        exit(1)

    theta0 = 0
    theta1 = 0

    try:
        file = open('thetas.csv')
        csvreader = csv.reader(file)

        headers = []
        thetas = []

        headers = next(csvreader)
        if (headers[0] != "theta0" or headers[1] != "theta1"):
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
        
        print(f"The predicted price of the car is: ${predict(mileage, theta0, theta1)}")
        
    except ValueError:
        print("Les thetas doivent être des nombres positifs")
        exit(1)
    except Exception as exc:
        print(exc)
        exit(1)


if __name__ == "__main__":
    main()