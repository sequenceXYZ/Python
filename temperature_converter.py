"""
Write a program that converts temperatures between Celsius and Fahrenheit.
"""
"""
Create a new file called temperature_converter.py. 
In the file, define two functions: celsius_to_fahrenheit and fahrenheit_to_celsius. 
Each function should take one argument (the temperature to convert) 
and return the converted temperature. 
In the main part of the program, prompt the user to enter a temperature and its unit (C or F). 
Call the appropriate function based on the unit and print the converted temperature to the console.
"""


def celsius_to_fahrenheit():
    f = ((temp * 9/5) + 32)
    print("Celsius", temp, "degrees converted to Fahrenheit temperature is", f, "degrees!")
    return


def fahrenheit_to_celsius():
    c = ((temp - 32) / 1.8)
    print("Celsius temperature is", c, "degrees")
    return


temp = float(input('Enter the temperature number you want to convert: '))
marker = str(input('Enter the marker C for Celsius-to-Fahrenheit or F for Fahrenheit-to-Celsius: '))

if marker == 'C':
    celsius_to_fahrenheit()
elif marker == 'F':
    fahrenheit_to_celsius()
else:
    print('Invalid marker, marker must be in capital letter!!!')
