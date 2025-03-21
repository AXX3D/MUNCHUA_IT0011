class Item:
    def __init__(self, item_id, name, description, price):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("ID must be a positive integer.")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        
        self.item_id = item_id
        self.name = name.strip()
        self.description = description.strip()
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def get_item(self, item_id):
        try:
            return self.items[item_id]
        except KeyError:
            print("Error: Item not found.")

    def edit_item(self, item_id, name=None, description=None, price=None):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            
            item = self.items[item_id]
            if name:
                item.name = name.strip()
            if description:
                item.description = description.strip()
            if price is not None:
                if not isinstance(price, (int, float)) or price < 0:
                    raise ValueError("Price must be a non-negative number.")
                item.price = price
            
            print("Item updated successfully.")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def remove_item(self, item_id):
        try:
            if item_id not in self.items:
                raise KeyError("Item not found.")
            del self.items[item_id]
            print("Item deleted successfully.")
        except KeyError as e:
            print(f"Error: {e}")

    def show_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

if __name__ == "__main__":
    manager = ItemManager()
    
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Item")
        print("3. Edit Item")
        print("4. Delete Item")
        print("5. Show All Items")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                item_id = int(input("Enter item ID: "))
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.add_item(item_id, name, description, price)
            except ValueError:
                print("You cannot do that")
        elif choice == "2":
            try:
                item_id = int(input("Enter item ID to view: "))
                item = manager.get_item(item_id)
                if item:
                    print(item)
            except ValueError:
                print("You cannot do that")
        elif choice == "3":
            try:
                item_id = int(input("Enter item ID to edit: "))
                name = input("Enter new name (leave blank to keep unchanged): ") or None
                description = input("Enter new description (leave blank to keep unchanged): ") or None
                price_input = input("Enter new price (leave blank to keep unchanged): ")
                price = float(price_input) if price_input else None
                manager.edit_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            try:
                item_id = int(input("Enter item ID to delete: "))
                manager.remove_item(item_id)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            manager.show_items()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("You cannot do that")
