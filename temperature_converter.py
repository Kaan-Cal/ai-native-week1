"""
Temperature Converter
A simple, beginner-friendly command-line tool to convert temperatures
between Celsius and Fahrenheit.
"""

def main():
    print("=== Temperature Converter ===")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")

    # Ask the user for their conversion choice
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        # Celsius to Fahrenheit conversion: F = (C * 9/5) + 32
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(f"\nResult: {celsius}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("\nError: Please enter a valid numeric temperature.")

    elif choice == "2":
        # Fahrenheit to Celsius conversion: C = (F - 32) * 5/9
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"\nResult: {fahrenheit}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("\nError: Please enter a valid numeric temperature.")

    else:
        print("\nInvalid choice. Please run the program again and select 1 or 2.")

if __name__ == "__main__":
    main()
