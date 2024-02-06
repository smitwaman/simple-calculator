def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def display_menu():
    print("\nCalculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_user_input()

def main():
    while True:
        display_menu()
        choice = input("Select operation (1, 2, 3, 4, 5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_user_input()

            if choice == '1':
                result = add(num1, num2)
                print("Result:", result)
            elif choice == '2':
                result = subtract(num1, num2)
                print("Result:", result)
            elif choice == '3':
                result = multiply(num1, num2)
                print("Result:", result)
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print("Result:", result)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
