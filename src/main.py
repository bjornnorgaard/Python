import os

from maths.calculator import Calculator


def main():
    calc = Calculator()
    sum_result = calc.add(10, 5)
    print(f"The sum is: {sum_result}")

    subtract_result = calc.subtract(10, 5)
    print(f"The result of the subtraction is: {subtract_result}")

    # Print value of env var SERVICE_NAME
    service_name = os.environ.get("SERVICE_NAME")
    print(f"Service name is: {service_name}")


if __name__ == "__main__":
    main()
