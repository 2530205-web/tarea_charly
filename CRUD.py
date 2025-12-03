# ================================================================
# PORTADA
# ================================================================
# Name: __________________________________________
# Student ID (Matricula): _________________________
# Group: __________________________________________
#
# File: matricula_ApellidoNombre.py
# ================================================================
#
# EXECUTIVE SUMMARY
# ------------------------------------------------
# A CRUD system (Create, Read, Update, Delete) allows managing data
# efficiently through basic operations on a storage structure. This
# program implements an in-memory CRUD using a list of dictionaries
# to store items like products. Using functions improves organization,
# modularity, and maintainability. The program includes a menu,
# validations, and all CRUD operations.


# ================================================================
# PROBLEM: In-memory CRUD manager with functions
# ================================================================
# Description:
# Program that implements a simple CRUD (Create, Read, Update, Delete)
# for items stored in memory. The program uses functions for each
# operation and a text-based menu to interact with the user.
#
# Data structure chosen:
# Option B — List of dictionaries.
# Reason: It allows multiple items with flexible attributes and makes
# iteration simple and readable.
#
# Inputs:
# - Menu options
# - For CREATE/UPDATE: item_id, name, price, quantity
# - For READ/DELETE: item_id
#
# Outputs:
# - Messages: "Item created", "Item updated", "Item deleted",
#   "Item not found", "Items list:", etc.
#
# Validations:
# - Menu option must be valid (0–5)
# - item_id must not be empty
# - price must be float >= 0
# - quantity must be int >= 0
# - Prevent duplicate IDs during creation
#
# Test cases:
# 1) Normal:
#    Create item (id=1), read it, update it, delete it → expected messages.
#
# 2) Border:
#    Create item with minimal values, e.g., quantity=0 → allowed.
#
# 3) Error:
#    Invalid menu option or empty id or non-numeric price → "Error: invalid input"

# Data structure: list of dicts
items_list = []


def find_item_by_id(item_list, item_id):
    """Return item dict if found, otherwise None."""
    for item in item_list:
        if item["id"] == item_id:
            return item
    return None


def create_item(item_list, item_id, name, price, quantity):
    """Create a new item if id does not already exist."""
    if find_item_by_id(item_list, item_id) is not None:
        return False  # Duplicate ID not allowed
    new_item = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    item_list.append(new_item)
    return True


def read_item(item_list, item_id):
    """Return item by id, or None if not found."""
    return find_item_by_id(item_list, item_id)


def update_item(item_list, item_id, new_name, new_price, new_quantity):
    """Update an item if it exists."""
    item = find_item_by_id(item_list, item_id)
    if item is None:
        return False
    item["name"] = new_name
    item["price"] = new_price
    item["quantity"] = new_quantity
    return True


def delete_item(item_list, item_id):
    """Delete an item if it exists."""
    item = find_item_by_id(item_list, item_id)
    if item is None:
        return False
    item_list.remove(item)
    return True


def list_items(item_list):
    """Print all items."""
    print("Items list:")
    if not item_list:
        print("(Empty)")
    else:
        for item in item_list:
            print(f"- ID: {item['id']}, Name: {item['name']}, "
                  f"Price: {item['price']}, Quantity: {item['quantity']}")


def main_menu():
    while True:
        print("\n===== CRUD MENU =====")
        print("1) Create item")
        print("2) Read item by ID")
        print("3) Update item by ID")
        print("4) Delete item by ID")
        print("5) List all items")
        print("0) Exit")

        option = input("Enter option: ").strip()

        if option not in {"0", "1", "2", "3", "4", "5"}:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        # CREATE
        if option == "1":
            item_id = input("Enter item ID: ").strip()
            name = input("Enter item name: ").strip()
            price_str = input("Enter price: ").strip()
            quantity_str = input("Enter quantity: ").strip()

            if not item_id or not name:
                print("Error: invalid input")
                continue

            try:
                price = float(price_str)
                quantity = int(quantity_str)
                if price < 0 or quantity < 0:
                    raise ValueError
            except ValueError:
                print("Error: invalid input")
                continue

            if create_item(items_list, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: ID already exists")

        # READ
        elif option == "2":
            item_id = input("Enter item ID to read: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            item = read_item(items_list, item_id)
            if item is None:
                print("Item not found")
            else:
                print(f"Item: ID={item['id']}, Name={item['name']}, "
                      f"Price={item['price']}, Quantity={item['quantity']}")

        # UPDATE
        elif option == "3":
            item_id = input("Enter item ID to update: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            name = input("Enter new name: ").strip()
            price_str = input("Enter new price: ").strip()
            quantity_str = input("Enter new quantity: ").strip()

            try:
                price = float(price_str)
                quantity = int(quantity_str)
                if price < 0 or quantity < 0:
                    raise ValueError
            except ValueError:
                print("Error: invalid input")
                continue

            if update_item(items_list, item_id, name, price, quantity):
                print("Item updated")
            else:
                print("Item not found")

        # DELETE
        elif option == "4":
            item_id = input("Enter item ID to delete: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            if delete_item(items_list, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        # LIST
        elif option == "5":
            list_items(items_list)


# Run program
if __name__ == "__main__":
    main_menu()


# ================================================================
# CONCLUSIONS
# ================================================================
# Using functions made the CRUD easier to manage by separating logic
# into clear and reusable components. A list of dictionaries allowed
# flexible storage and simple iteration for searches. Validating user
# input ensured program stability and prevented incorrect operations.
# Challenges included keeping consistent ID handling and validating
# numeric fields, which was solved with clear conditions. This CRUD
# could be extended by adding file saving, databases, or more fields.


# ================================================================
# REFERENCES
# ================================================================
# 1) Python Documentation – Data structures (dict, list)
# 2) Python Documentation – Defining functions
# 3) Tutorials on Python CRUD systems and menu-driven programs


# ================================================================
# GITHUB REPOSITORY URL
# ================================================================
# Add your GitHub repo URL here:
# https://github.com/_________________________
