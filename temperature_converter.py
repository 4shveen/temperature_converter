'''Temperature Converter
Write a Python program that prompts the user to enter a temperature and its unit (Celsius or Fahrenheit).
Based on the unit provided, convert the temperature to the other unit and display the result. Use a string
variable to store the unit.'''

from colorama import Fore,Style
# Greet the user and explain how to use the program.
print(Fore.YELLOW + "Hello. This program serves to convert temperature from Celsius to Farenheit, or from Farenheit to Celcius." + Style.RESET_ALL)

# Take input from user for temperature as a number.
temp = float(input("Enter a value for the temperature: "))

# Ask user input for the unit (C or F).
unit = str(input("Enter C for Celcius or F for Farenheit: ")).strip().upper()

# Convert based on the unit; C to F or F to C, and print the respective result. If the unit is invalid, print an error message.
if unit == "C":
    result = (temp * 9/5) + 32
    print(f"{temp}°C is equal to {result:.2f}°F")
elif unit == "F":
    result = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {result:.2f}°C")
else:
    result = "Temperature unit not entered properly. The program will terminate."
