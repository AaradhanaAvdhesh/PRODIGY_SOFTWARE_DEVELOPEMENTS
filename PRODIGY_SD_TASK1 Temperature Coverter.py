def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = input("Enter your choice (1-6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        try:
            temperature = float(input("Enter the temperature: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        if choice == '1':
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is equal to {result} Fahrenheit.")
        elif choice == '2':
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is equal to {result} Celsius.")
        elif choice == '3':
            result = celsius_to_kelvin(temperature)
            print(f"{temperature} Celsius is equal to {result} Kelvin.")
        elif choice == '4':
            result = kelvin_to_celsius(temperature)
            print(f"{temperature} Kelvin is equal to {result} Celsius.")
        elif choice == '5':
            result = fahrenheit_to_kelvin(temperature)
            print(f"{temperature} Fahrenheit is equal to {result} Kelvin.")
        elif choice == '6':
            result = kelvin_to_fahrenheit(temperature)
            print(f"{temperature} Kelvin is equal to {result} Fahrenheit.")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
