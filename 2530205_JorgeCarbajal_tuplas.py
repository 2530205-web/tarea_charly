#nombre: Jorge Candelario Carbajal Carrizales
#matricula: 2530205
#grupo: IM 1-2
# Resumen Ejecutivo
# En Python, las colecciones permiten almacenar y procesar conjuntos de datos de manera
# estructurada mediante tres tipos principales: listas, tuplas y diccionarios. Las listas
# son estructuras ordenadas y mutables, ideales para agregar, modificar o eliminar
# elementos; las tuplas son ordenadas pero inmutables, útiles para datos que deben
# permanecer fijos; y los diccionarios permiten asociar claves con valores para realizar
# búsquedas rápidas y directas. Este documento presenta seis problemas que aplican estas
# estructuras en contextos prácticos, incluyendo catálogos, registros y análisis de datos.
# Cada problema incluye su descripción, entradas y salidas, validaciones esenciales y tres
# casos de prueba que ilustran el uso adecuado de operaciones como indexación, inserción,
# eliminación, actualización, ordenamiento y agregación de información.





# =================== Problem 1: Shopping List Basics (List Operations) ===================
# Description: Manage a list of products (strings) and quantities (integers):
# - Create an initial list of products
# - Add a new product to the end
# - Show total number of items
# - Check if a specific product is in the list (boolean)

# Inputs:
# - initial_items_text (str): comma-separated items, e.g., "apple,banana,orange"
# - new_item (str): product to add
# - search_item (str): product to search in the list

# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" True|False

# Validations:
# - initial_items_text must not be empty after strip()
# - new_item and search_item must not be empty
# - Remove extra spaces from each item
# - If initial_items_text is empty, start with an empty list (documented decision)

# Test cases:
# 1) Normal: initial_items_text="apple,banana", new_item="orange", search_item="banana"
#    -> Items list: ['apple','banana','orange'], Total items: 3, Found item: True
# 2) Border: initial_items_text="apple", new_item="apple", search_item="apple"
#    -> Items list: ['apple','apple'], Total items: 2, Found item: True
# 3) Error: initial_items_text="", new_item="  ", search_item="  "
#    -> Error: invalid input

def shopping_list_basics():
    initial_items_text = input("Enter initial items (comma-separated): ").strip()
    new_item = input("Enter a new item to add: ").strip()
    search_item = input("Enter an item to search: ").strip()
    
    # Validation: initial_items_text, new_item, search_item not empty
    if len(new_item) == 0 or len(search_item) == 0:
        print("Error: invalid input")
        return
    
    # Create initial list
    if len(initial_items_text) == 0:
        items_list = []  # Decision: start empty if initial text is empty
    else:
        items_list = [item.strip() for item in initial_items_text.split(",") if item.strip() != ""]
    
    # Validation: if initial list empty after processing, it's acceptable
    # Add new item
    items_list.append(new_item)
    
    # Check if search_item is in list
    is_in_list = search_item in items_list
    
    # Output results
    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", is_in_list)

# Run Problem 1
if __name__ == "__main__":
    shopping_list_basics()

# =================== Problem 2: Points and Distances with Tuples ===================
# Description: Use tuples to represent two points in 2D space and calculate distance and midpoint.

# Inputs:
# - x1, y1, x2, y2 (float): coordinates of the points

# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)

# Validations:
# - All four inputs must be convertible to float
# - No other range restrictions

# Test cases:
# 1) Normal: x1=0, y1=0, x2=3, y2=4 -> Distance: 5.0, Midpoint: (1.5, 2.0)
# 2) Border: x1=1, y1=1, x2=1, y2=1 -> Distance: 0.0, Midpoint: (1.0, 1.0)
# 3) Error: x1="a", y1=0, x2=2, y2=3 -> Error: invalid input

def points_and_distances():
    try:
        x1 = float(input("Enter x1: ").strip())
        y1 = float(input("Enter y1: ").strip())
        x2 = float(input("Enter x2: ").strip())
        y2 = float(input("Enter y2: ").strip())
    except ValueError:
        print("Error: invalid input")
        return
    
    # Create tuples
    point_a = (x1, y1)
    point_b = (x2, y2)
    
    # Calculate distance
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    # Calculate midpoint
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)
    
    # Output results
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

# Run Problem 2
if __name__ == "__main__":
    points_and_distances()

# =================== Problem 3: Product Catalog with Dictionary ===================
# Description: Manage a small product catalog using a dictionary:
# - key: product name (string)
# - value: unit price (float)
# The program calculates total price for a given product and quantity.

# Inputs:
# - product_name (str)
# - quantity (int): number of units to buy

# Outputs:
# - If product exists:
#   - "Unit price:" <unit_price>
#   - "Quantity:" <quantity>
#   - "Total:" <total_price>
# - If product does not exist:
#   - "Error: product not found"

# Validations:
# - product_name must not be empty after strip()
# - quantity must be > 0
# - Check if product_name exists in the dictionary

# Test cases:
# 1) Normal: product_name="apple", quantity=3 -> Unit price: 10.0, Quantity: 3, Total: 30.0
# 2) Border: product_name="banana", quantity=1 -> Unit price: 5.0, Quantity: 1, Total: 5.0
# 3) Error: product_name="pear", quantity=2 -> Error: product not found

def product_catalog():
    # Initial product catalog
    product_prices = {
        "apple": 10.0,
        "banana": 5.0,
        "orange": 7.5
    }
    
    product_name = input("Enter product name: ").strip()
    quantity_input = input("Enter quantity: ").strip()
    
    # Validate product_name
    if len(product_name) == 0:
        print("Error: invalid input")
        return
    
    # Validate quantity
    try:
        quantity = int(quantity_input)
        if quantity <= 0:
            print("Error: invalid input")
            return
    except ValueError:
        print("Error: invalid input")
        return
    
    # Check if product exists
    if product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
    else:
        print("Error: product not found")

# Run Problem 3
if __name__ == "__main__":
    product_catalog()

# =================== Problem 4: Student Grades with Dict and List ===================
# Description: Manage student grades using a dictionary:
# - key: student name (string)
# - value: list of grades (list of float)
# The program calculates the average and determines if the student passed.

# Inputs:
# - student_name (string)

# Outputs:
# - If student exists:
#   - "Grades:" <grades_list>
#   - "Average:" <average>
#   - "Passed:" True|False
# - If student does not exist:
#   - "Error: student not found"

# Validations:
# - student_name must not be empty after strip()
# - Check if student_name exists in dictionary
# - Ensure grades list is not empty before calculating average

# Test cases:
# 1) Normal: student_name="Alice" -> Grades: [90,85,78], Average: 84.33, Passed: True
# 2) Border: student_name="Bob" -> Grades: [70,70,70], Average: 70.0, Passed: True
# 3) Error: student_name="Charlie" -> Error: student not found

def student_grades():
    # Initial grades dictionary
    grades_dict = {
        "Alice": [90.0, 85.0, 78.0],
        "Bob": [70.0, 70.0, 70.0],
        "Eve": [60.0, 65.0, 58.0]
    }
    
    student_name = input("Enter student name: ").strip()
    
    if len(student_name) == 0:
        print("Error: invalid input")
        return
    
    if student_name in grades_dict:
        grades_list = grades_dict[student_name]
        if len(grades_list) == 0:
            print("Error: no grades available for this student")
            return
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0
        print("Grades:", grades_list)
        print("Average:", round(average, 2))
        print("Passed:", is_passed)
    else:
        print("Error: student not found")

# Run Problem 4
if __name__ == "__main__":
    student_grades()

# =================== Problem 5: Word Frequency Counter (List + Dict) ===================
# Description: Count the frequency of each word in a sentence using a list and dictionary.
# - key: word (string)
# - value: frequency (int)
# The program also identifies the most common word.

# Inputs:
# - sentence (string)

# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>

# Validations:
# - sentence must not be empty after strip()
# - Ensure the words list is not empty
# - Optional: remove simple punctuation

# Test cases:
# 1) Normal: sentence="apple banana apple" -> Words list: ['apple','banana','apple'], Frequencies: {'apple':2,'banana':1}, Most common word: 'apple'
# 2) Border: sentence="one" -> Words list: ['one'], Frequencies: {'one':1}, Most common word: 'one'
# 3) Error: sentence="   " -> Error: invalid input

def word_frequency_counter():
    sentence = input("Enter a sentence: ").strip()
    
    if len(sentence) == 0:
        print("Error: invalid input")
        return
    
    # Optional: remove simple punctuation (commas, periods)
    sentence_clean = sentence.replace(",", "").replace(".", "")
    
    # Convert to lowercase and split into words
    words_list = sentence_clean.lower().split()
    
    if len(words_list) == 0:
        print("Error: no valid words found")
        return
    
    # Build frequency dictionary
    freq_dict = {}
    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    # Find the most common word
    most_common_word = max(freq_dict, key=freq_dict.get)
    
    # Output results
    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)

# Run Problem 5
if __name__ == "__main__":
    word_frequency_counter()

# =================== Problem 6: Simple Contact Book (Dictionary CRUD) ===================
# Description: Implement a mini contact book using a dictionary.
# - key: contact name (string)
# - value: phone number (string)
# Supports adding, searching, and deleting contacts.

# Inputs:
# - action_text (string): "ADD", "SEARCH", or "DELETE"
# - name (string): contact name
# - phone (string): contact phone (only for "ADD")

# Outputs:
# - "ADD": Contact saved: name, phone
# - "SEARCH": Phone: <phone> or Error: contact not found
# - "DELETE": Contact deleted: name or Error: contact not found

# Validations:
# - action_text normalized to uppercase
# - action_text must be "ADD", "SEARCH", or "DELETE"
# - name must not be empty
# - For "ADD": phone must not be empty

# Test cases:
# 1) ADD: action="ADD", name="Alice", phone="12345" -> Contact saved: Alice, 12345
# 2) SEARCH: action="SEARCH", name="Alice" -> Phone: 12345
# 3) DELETE: action="DELETE", name="Alice" -> Contact deleted: Alice

def contact_book():
    # Initial contacts dictionary
    contacts = {
        "Alice": "1234567890",
        "Bob": "0987654321",
        "Eve": "5551234567"
    }
    
    action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()
    
    if action_text not in ["ADD", "SEARCH", "DELETE"]:
        print("Error: invalid action")
        return
    
    name = input("Enter contact name: ").strip()
    if len(name) == 0:
        print("Error: invalid input")
        return
    
    if action_text == "ADD":
        phone = input("Enter phone number: ").strip()
        if len(phone) == 0:
            print("Error: invalid input")
            return
        contacts[name] = phone
        print("Contact saved:", name, phone)
    
    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")
    
    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")

# Run Problem 6
if __name__ == "__main__":
    contact_book()

# =================== Conclusions ===================
# - Lists are ideal for ordered collections and flexible addition/removal of elements.
# - Tuples are useful for immutable data that should not change, like coordinates.
# - Dictionaries allow fast lookup by key, making them ideal for contacts, grades, or product catalogs.
# - Combining structures (dict of lists, list of tuples) enables complex data modeling.
# - Normalizing inputs (strip(), upper(), lower()) prevents common errors.
# - Validating entries ensures robust and predictable program behavior.
# - Boolean flags are useful for decision-making based on conditions (e.g., is_passed, is_in_list).
# - Patterns like CRUD operations and frequency counting recur frequently in programming tasks.

# References:
# 1) Python Software Foundation. "Built-in Types — Sequence Types (list, tuple)".
#    Documentación oficial de Python.
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
#
# 2) Python Software Foundation. "Mapping Types — dict".
#    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#
# 3) Python Software Foundation. "Built-in Functions" (len(), sum(), min(), max(), sorted()).
#    https://docs.python.org/3/library/functions.html
#
# 4) Sweigart, Al. *Automate the Boring Stuff with Python*, 2nd Edition.
#    No Starch Press, 2019. (Capítulos sobre listas, diccionarios y estructuras de datos)
#
# 5) Lutz, Mark. *Learning Python*, 5th Edition.
#    O’Reilly Media, 2013. (Secciones sobre secuencias, tuplas, listas y diccionarios)

#repositorio
#https://github.com/2530205-web/tarea_charly
#https://github.com/2530205-web/tarea_charly/blob/main/2530205_JorgeCarbajal_tuplas.py