# Importing necessary libraries
import tkinter as tk
from tkinter import ttk, messagebox

# Importing conversion functions from converter module
from converter import *  

# Class for the Converter Application
class ConverterApp:

    def __init__(self, root):
    
        self.root = root
        self.root.title("Unit Converter")               # Setting window title
        self.root.geometry("400x400")                   # Setting window size

        # Customizing the style for widgets using ttk
        self.style = ttk.Style()
        self.style.theme_use('clam')                    # Choosing the theme (can be changed)

        # Configuring styles for different widget types
        self.style.configure('TFrame', background='#f0f0f0')                                                                        # Frame background color
        self.style.configure('TButton', background='#4caf50', foreground='white', font=('Arial', 12, 'bold'), padx=10, pady=5)      # Button style
        self.style.map('TButton', background=[('active', '#45a049')])                                                               # Button style when active
        self.style.configure('TLabel', background='#f0f0f0', foreground='#333', font=('Arial', 12))                                 # Label style
        self.style.configure('TCombobox', font=('Arial', 12), width=15)                                                             # Combobox style

        # Main frame
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)                                # Packing the frame with padding and expansion settings

        # Title label
        self.label_title = ttk.Label(self.frame, text="Unit Converter", style='TLabel')             # Creating a label for the title
        self.label_title.grid(row=0, column=0, columnspan=2, pady=10)                               # Grid layout for title label

        # Input label and entry widget
        self.label_input = ttk.Label(self.frame, text="Enter value:", style='TLabel')               # Label for input
        self.label_input.grid(row=1, column=0, pady=10, sticky=tk.E)                                # Grid layout for input label
        self.entry_input = ttk.Entry(self.frame, width=10, font=('Arial', 12))                      # Entry widget for input
        self.entry_input.grid(row=1, column=1, pady=10, sticky=tk.W)                                # Grid layout for input entry widget

        # Dropdown menu for conversion from unit
        self.label_conversion_from = ttk.Label(self.frame, text="Convert from:", style='TLabel')                                                                    # Label for from unit
        self.label_conversion_from.grid(row=2, column=0, pady=10, sticky=tk.E)                                                                                      # Grid layout for from unit label
        self.from_unit = ttk.Combobox(self.frame, values=["Celsius", "Fahrenheit", "Meters", "Feet", "Kilograms", "Pounds"], state="readonly", font=('Arial', 12))  # Combobox for from unit
        self.from_unit.current(0)                                                                                                                                   # Default to Celsius
        self.from_unit.grid(row=2, column=1, pady=10, sticky=tk.W)                                                                                                  # Grid layout for from unit combobox

        # Dropdown menu for conversion to unit
        self.label_conversion_to = ttk.Label(self.frame, text="Convert to:", style='TLabel')                                                                        # Label for to unit
        self.label_conversion_to.grid(row=3, column=0, pady=10, sticky=tk.E)                                                                                        # Grid layout for to unit label
        self.to_unit = ttk.Combobox(self.frame, values=["Celsius", "Fahrenheit", "Meters", "Feet", "Kilograms", "Pounds"], state="readonly", font=('Arial', 12))    # Combobox for to unit
        self.to_unit.current(1)                                                                                                                                     # Default to Fahrenheit
        self.to_unit.grid(row=3, column=1, pady=10, sticky=tk.W)                                                                                                    # Grid layout for to unit combobox

        # Convert button
        self.convert_button = ttk.Button(self.frame, text="Convert", command=self.perform_conversion, style='TButton')   # Button to perform conversion
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=20)                                                 # Grid layout for convert button

        # Result label
        self.label_result = ttk.Label(self.frame, text="", style='TLabel')      # Label to display conversion result
        self.label_result.grid(row=5, column=0, columnspan=2, pady=10)          # Grid layout for result label



    def perform_conversion(self):
      
        """Function to perform unit conversion based on user input"""
      
        try:
            value = float(self.entry_input.get())   # Get input value from entry widget and convert to float
            from_unit = self.from_unit.get()        # Get selected 'from' unit from combobox
            to_unit = self.to_unit.get()            # Get selected 'to' unit from combobox

            # Perform conversion based on selected units
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = celsius_to_fahrenheit(value)
                self.label_result.config(text=f"{value}°C is equal to {result:.2f}°F")

            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = fahrenheit_to_celsius(value)
                self.label_result.config(text=f"{value}°F is equal to {result:.2f}°C")
            
            elif from_unit == "Meters" and to_unit == "Feet":
                result = meters_to_feet(value)
                self.label_result.config(text=f"{value} meters is equal to {result:.2f} feet")
            
            elif from_unit == "Feet" and to_unit == "Meters":
                result = feet_to_meters(value)
                self.label_result.config(text=f"{value} feet is equal to {result:.2f} meters")
            
            elif from_unit == "Kilograms" and to_unit == "Pounds":
                result = kilograms_to_pounds(value)
                self.label_result.config(text=f"{value} kg is equal to {result:.2f} pounds")
            
            elif from_unit == "Pounds" and to_unit == "Kilograms":
                result = pounds_to_kilograms(value)
                self.label_result.config(text=f"{value} pounds is equal to {result:.2f} kg")
            
            else:
                # Error message for invalid conversion
                messagebox.showerror("Error", "Invalid conversion. Please select valid units.")     
       
        except ValueError:
            # Error message for invalid input
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")            


def main():
    root = tk.Tk()              # Create main window
    app = ConverterApp(root)    # Initialize ConverterApp
    root.mainloop()             # Run the main event loop


# Execute main function if script is run directly
if __name__ == "__main__":
    main()  
