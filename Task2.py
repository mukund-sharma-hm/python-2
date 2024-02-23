from tabulate import tabulate
from Task1 import day_details

# Task 2
def print_table(day_details):
    """function to tabulate the data from dictionary"""
    headers = ["Name of the Day",
                "Occurences", 
                "Short Form", 
                "Name in Lower", 
                "Name in Upper", 
                "Length"]
    data = [[day, *details] for day, details in day_details.items()]
    print(tabulate(data, headers=headers))

print_table(day_details)
