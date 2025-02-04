class Inventory:
    def __init__(self):
        # Initialize an empty dictionary to store items and their quantities
        self.items = {}

    def add_item(self, item_name, quantity):
        # If the item is already in the inventory, update its quantity
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            # If the item is not in the inventory, add it with the specified quantity
            self.items[item_name] = quantity

    def get_item_info(self, item_name):
        # Retrieve information about a specific item
        if item_name in self.items:
            return f"{item_name}: {self.items[item_name]} units"
        else:
            return f"{item_name} is not in the inventory."

    def total_quantity(self):
        # Calculate and display the total quantity of all items in the inventory
        total = sum(self.items.values())
        return f"Total quantity of all items: {total} units"

def main():
    # Create an instance of the Inventory class
    inventory = Inventory()

    while True:
        # Display menu options to the user
        print("\n1. Add item")
        print("2. Get item info")
        print("3. Get total quantity")
        print("4. Exit")

        # Prompt the user to choose an option
        choice = input("Choose an option: ")

        if choice == "1":
            # Add item to the inventory
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            inventory.add_item(item_name, quantity)
            print(f"{quantity} units of {item_name} have been added to the inventory.")

        elif choice == "2":
            # Retrieve information about a specific item
            item_name = input("Enter the item name: ")
            print(inventory.get_item_info(item_name))

        elif choice == "3":
            # Display the total quantity of all items
            print(inventory.total_quantity())

        elif choice == "4":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
