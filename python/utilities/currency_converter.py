import requests  # Imports the 'requests' library for making HTTP requests to the API.

def get_exchange_rates(base_currency="USD"):
    
    # Fetches exchange rates from an API.
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"  # Constructs the API URL using the base currency.
    response = requests.get(url)                    # Sends a GET request to the API endpoint.
    response.raise_for_status()                     # Raises an exception if there's an HTTP error (e.g., 404 Not Found).
    data = response.json()                          # Parses the JSON response from the API.
    return data["rates"]                            # Returns a dictionary containing exchange rates for various currencies.


def convert_currency(amount, from_currency, to_currency):
    
    # Converts an amount from one currency to another.
    rates = get_exchange_rates(base_currency=from_currency)     # Fetches exchange rates using the 'from_currency' as the base.
    converted_amount = amount * rates[to_currency]              # Calculates the converted amount using the exchange rate.
    return converted_amount                                     # Returns the converted amount.

if __name__ == "__main__":
    while True:
        print("\nCurrency Converter")                                                       # Prints a header for the currency converter.
        amount = float(input("Enter the amount to convert: "))                              # Prompts the user to enter the amount.
        from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()   # Prompts for the 'from' currency and converts to uppercase.
        to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()       # Prompts for the 'to' currency and converts to uppercase.

        try:
            converted_amount = convert_currency(amount, from_currency, to_currency)                 # Calls the 'convert_currency' function to perform the conversion.
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")     # Prints the converted amount.
        
        except KeyError:
            print("Invalid currency code. Please check the currency codes.")                        # Handles invalid currency codes.

        if input("\nDo you want to make another conversion? (y/n): ").lower() != 'y':                 # Prompts the user to continue or exit.
            break # Exits the loop if the user doesn't enter 'y'. 