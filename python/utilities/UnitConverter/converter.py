def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Formula:
        Fahrenheit = Celsius * 9/5 + 32

    Parameters:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Equivalent temperature in Fahrenheit.
    """
    fahrenheit = celsius * 9/5 + 32  # Conversion formula
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Formula:
        Celsius = (Fahrenheit - 32) * 5/9

    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Equivalent temperature in Celsius.
    """
    celsius = (fahrenheit - 32) * 5/9  # Conversion formula
    return celsius


def meters_to_feet(meters):
    """
    Convert Meters to Feet.

    Formula:
        Feet = Meters * 3.28084

    Parameters:
        meters (float): Length in meters.

    Returns:
        float: Equivalent length in feet.
    """
    feet = meters * 3.28084  # Conversion formula
    return feet


def feet_to_meters(feet):
    """
    Convert Feet to Meters.

    Formula:
        Meters = Feet / 3.28084

    Parameters:
        feet (float): Length in feet.

    Returns:
        float: Equivalent length in meters.
    """
    meters = feet / 3.28084  # Conversion formula
    return meters


def kilograms_to_pounds(kilograms):
    """
    Convert Kilograms to Pounds.

    Formula:
        Pounds = Kilograms * 2.20462

    Parameters:
        kilograms (float): Weight in kilograms.

    Returns:
        float: Equivalent weight in pounds.
    """
    pounds = kilograms * 2.20462  # Conversion formula
    return pounds


def pounds_to_kilograms(pounds):
    """
    Convert Pounds to Kilograms.

    Formula:
        Kilograms = Pounds / 2.20462

    Parameters:
        pounds (float): Weight in pounds.

    Returns:
        float: Equivalent weight in kilograms.
    """
    kilograms = pounds / 2.20462  # Conversion formula
    return kilograms
