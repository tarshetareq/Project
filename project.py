
from periodictable import periodic_table

def get_element_by_atomic_number(atomic_number):

    element = periodic_table.get(atomic_number)
    if element:
        print(f"Name: {element['name']}")
        print(f"Symbol: {element['symbol']}")
        print(f"Atomic Number: {atomic_number}")
        print(f"Atomic Mass: {element['atomic_mass']}")
        print(f"Group: {element['group']}")
        print(f"Period: {element['period']}")
    else:
        print("Element not found.")

def get_element_by_symbol(symbol):
    for atomic_number, element in periodic_table.items():
        if element["symbol"].lower() == symbol.lower():
            print(f"Name: {element['name']}")
            print(f"Symbol: {element['symbol']}")
            print(f"Atomic Number: {atomic_number}")
            print(f"Atomic Mass: {element['atomic_mass']}")
            print(f"Group: {element['group']}")
            print(f"Period: {element['period']}")
            return
    print("Element not found.")

def add_element():

    try:
        atomic_number = int(input("Enter atomic number: "))
        if atomic_number in periodic_table:
            print("Element with this atomic number already exists.")
            return
        name = input("Enter element name: ")
        symbol = input("Enter element symbol: ")
        atomic_mass = float(input("Enter atomic mass: "))
        group = int(input("Enter group number: "))
        period = int(input("Enter period number: "))
        periodic_table[atomic_number] = {
            "name": name,
            "symbol": symbol,
            "atomic_mass": atomic_mass,
            "group": group,
            "period": period
        }
        print(f"Element {name} added successfully!")
    except ValueError:
        print("Invalid input. Please enter correct data.")

def remove_element():

    try:
        atomic_number = int(input("Enter atomic number of the element to remove: "))
        if atomic_number in periodic_table:
            removed_element = periodic_table.pop(atomic_number)
            print(f"Element {removed_element['name']} (Atomic Number: {atomic_number}) removed successfully!")
        else:
            print("Element not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("Periodic Table Analysis Tool")
        print("1. Search by Atomic Number")
        print("2. Search by Symbol")
        print("3. Add a New Element")
        print("4. Remove an Element")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            
                atomic_number = int(input("Enter atomic number: "))
                atomic_number = int(atomic_number)
                get_element_by_atomic_number(atomic_number)
            
        elif choice == "2":
            symbol = input("Enter element symbol: ")
            get_element_by_symbol(symbol)
        elif choice == "3":
            add_element()
        elif choice == "4":
            remove_element()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
