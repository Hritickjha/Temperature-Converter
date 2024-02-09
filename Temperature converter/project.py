def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("Temperature Converter Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius_input = float(input("Enter temperature in Celsius: "))
        converted_temperature = celsius_to_fahrenheit(celsius_input)
        print(f"{celsius_input} Celsius is equal to {converted_temperature:.2f} Fahrenheit.")
    
    elif choice == '2':
        fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
        converted_temperature = fahrenheit_to_celsius(fahrenheit_input)
        print(f"{fahrenheit_input} Fahrenheit is equal to {converted_temperature:.2f} Celsius.")
    
    else:
        print("Invalid choice. Please enter either 1 or 2.")