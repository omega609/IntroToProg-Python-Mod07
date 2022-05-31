# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: This script is intended to demonstrate Pickling and Structured
#              error handling. Data provided by the user will be pickled and
#              de-pickled. Error handling will be shown using a try-block
#               exception.
# ChangeLog (Who,When,What):
# Omar Lozano,05.31.2022, Script Created
# ---------------------------------------------------------------------------- #

import pickle  # Importing the pickle module to use in this code
# Data------------------------------------------------------------------------#
FileName = 'Assignment07test.dat' # File where data will be stored
lstVehicle = [] # empty list to store info for a vehicle

# Processing------------------------------------------------------------------#
def store_Data(file_name, list_data):  # Function to save data to file as binary
    file = open(file_name, "wb") # 'b' needed because operations are done in binary
    pickle.dump(list_data, file)
    file.close()

def load_Data(file_name):  # Function to read binary file
    file = open(file_name, "rb")  # rb to read from a binary file
    file_data = pickle.load(file)  # The file from which to load an object from
    file.close()
    return file_data

# Presentation---------------------------------------------------------------#
#  Get make, model, and year of car
strMake = input("Enter the make of a vehicle: ")
strModel = input("Enter the model of a car: ")

while (True):  # Loop used to keep asking user for a valid date
    try:  # Using try block exception to check if a valid integer is used for a date
        intYear = input("Enter the year of the car: ")
        intYear = int(intYear)  # Convert input into integer
    except ValueError:  # If year cannot be converted to integer exception thrown
        print("Enter a valid year as an integer")
        continue
    if (0 <= intYear) and (intYear <= 2022):  # Conditional statment to make sure year is valid
        break
    else:
        print("Enter a valid integer")

lstVehicle = [strMake, strModel, intYear]  # Assign attributes to list
store_Data(FileName, lstVehicle)
print(load_Data(FileName))
