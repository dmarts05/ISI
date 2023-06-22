import math


def show_menu():
    print("************************************")
    print("*            CALCULATOR            *")
    print("************************************")
    print("1) Add an arbitrary number of values.")
    print("2) Subtract two values.")
    print("3) Multiply an arbitrary number of values.")
    print("4) Divide two values.")
    print("5) Calculate the value of one number raised to another.")
    print("6) Calculate the natural logarithm of a number.")
    print("7) Exit.")
    print("")


def get_number_input(msg: str) -> float:
    while True:
        try:
            number = float(input(msg))
            break
        except ValueError:
            print("Invalid number, try again...")

    return number


def get_number_stop_input() -> tuple:
    number = 0
    stop = False
    while True:
        try:
            number = input(
                "Please, enter a number or 'stop' to stop asking for more numbers: "
            )

            if number == "stop":
                stop = True
                break

            number = float(number)
            break
        except ValueError:
            print("Invalid number, try again...")

    return number, stop


def add(values: list) -> float:
    return sum(values)


def subtract(v1: float, v2: float) -> float:
    return v1 - v2


def multiply(values: list) -> float:
    return math.prod(values)


def divide(v1: float, v2: float) -> float:
    return v1 / v2


def xpow(v1: float, v2: float) -> float:
    return pow(v1, v2)


def natural_log(value: float) -> float:
    return math.log(value)


if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Please, select an option: ")

        if option == "1":
            values = []
            while True:
                number, stop = get_number_stop_input()
                if stop:
                    break
                values.append(number)
            print(f"Result: {add(values)}")
        elif option == "2":
            v1 = get_number_input("Please, enter the first number: ")
            v2 = get_number_input("Please, enter the second number: ")
            print(f"Result: {subtract(v1, v2)}")
        elif option == "3":
            values = []
            while True:
                number, stop = get_number_stop_input()
                if stop:
                    break
                values.append(number)
            print(f"Result: {multiply(values)}")
        elif option == "4":
            v1 = get_number_input("Please, enter the first number: ")
            v2 = get_number_input("Please, enter the second number: ")
            print(f"Result: {divide(v1, v2)}")
        elif option == "5":
            v1 = get_number_input("Please, enter the first number: ")
            v2 = get_number_input("Please, enter the second number: ")
            print(f"Result: {xpow(v1, v2)}")
        elif option == "6":
            value = get_number_input("Please, enter a number: ")
            print(f"Result: {natural_log(value)}")
        elif option == "7":
            break
