#nombre: Jorge Candelario Carbajal Carrizales
#matricula: 2530205
#grupo: IM 1-2
#resumen ejecutico: # Resumen Ejecutivo
# Un string en Python es un tipo de dato de texto que representa una secuencia de caracteres
# y es inmutable, lo que significa que cualquier modificación genera una nueva cadena.
# Python ofrece numerosas operaciones útiles para manejar texto: concatenación, obtención
# de longitud, slicing para extraer subcadenas, búsqueda de patrones, reemplazo, división
# y unión de palabras. Validar y normalizar las entradas de usuario es esencial para evitar
# errores, por ejemplo, eliminando espacios extra, ajustando mayúsculas/minúsculas o
# verificando formatos básicos como correos o contraseñas.
# Este documento desarrolla seis problemas que aplican estas técnicas: formateo de nombres,
# validación simple de correos, detección de palíndromos, estadísticas de oraciones,
# clasificación de contraseñas y creación de etiquetas de productos. Cada problema incluye
# descripción, entradas, salidas, validaciones y tres casos de prueba representativos.





# =================== Problem 1: Full Name Formatter (Name + Initials) ===================
# Description: Given a full name as a single string (e.g., "juan carlos tovar"), 
# the program normalizes the text, formats it in Title Case, and displays initials in the format X.X.X.

# Inputs:
# - full_name (str): full name, can be in mixed case, with extra spaces

# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"

# Validations:
# - full_name must not be empty after strip()
# - Must contain at least two words
# - Do not accept strings that are only spaces

# Test cases:
# 1) Normal: full_name="juan carlos tovar" -> Formatted name: "Juan Carlos Tovar", Initials: "J.C.T."
# 2) Border: full_name="ana maria" -> Formatted name: "Ana Maria", Initials: "A.M."
# 3) Error: full_name="    " -> Error: invalid input

def full_name_formatter():
    full_name = input("Enter full name: ").strip()
    
    # Validation: check if input is empty after strip
    if len(full_name) == 0:
        print("Error: invalid input")
        return
    
    # Split the name into words
    name_parts = full_name.split()
    
    # Validation: must contain at least 2 words
    if len(name_parts) < 2:
        print("Error: invalid input")
        return
    
    # Format name in Title Case
    formatted_name = " ".join([part.title() for part in name_parts])
    
    # Generate initials
    initials = ".".join([part[0].upper() for part in name_parts]) + "."
    
    # Output results
    print("Formatted name:", formatted_name)
    print("Initials:", initials)

# Run Problem 1
if __name__ == "__main__":
    full_name_formatter()

# =================== Problem 2: Simple Email Validator (Structure + Domain) ===================
# Description: Validates if an email address has a basic correct format:
# - Contains exactly one '@'
# - After '@' there is at least one '.'
# - No whitespace in the email
# If valid, also displays the domain part (after '@').

# Inputs:
# - email_text (str): email address

# Outputs:
# - "Valid email: True" or "Valid email: False"
# - If valid: "Domain: <domain_part>"

# Validations:
# - email_text must not be empty after strip()
# - Count occurrences of '@'
# - Check for spaces in the email

# Test cases:
# 1) Normal: email_text="user@example.com" -> Valid email: True, Domain: example.com
# 2) Border: email_text="a@b.c" -> Valid email: True, Domain: b.c
# 3) Error: email_text="user@@example.com" -> Valid email: False

def simple_email_validator():
    email_text = input("Enter email address: ").strip()
    
    # Validation: not empty
    if len(email_text) == 0:
        print("Valid email: False")
        return
    
    # Validation: no spaces
    if " " in email_text:
        print("Valid email: False")
        return
    
    # Validation: exactly one '@'
    at_count = email_text.count("@")
    if at_count != 1:
        print("Valid email: False")
        return
    
    # Validation: at least one '.' after '@'
    at_index = email_text.find("@")
    domain_part = email_text[at_index + 1:]
    if "." not in domain_part:
        print("Valid email: False")
        return
    
    # If all checks passed
    print("Valid email: True")
    print("Domain:", domain_part)

# Run Problem 2
if __name__ == "__main__":
    simple_email_validator()

# =================== Problem 3: Palindrome Checker (Ignoring Spaces and Case) ===================
# Description: Determines if a phrase is a palindrome (reads the same forward and backward),
# ignoring spaces and capitalization.

# Inputs:
# - phrase (str): input phrase

# Outputs:
# - "Is palindrome: True" or "Is palindrome: False"
# - (Optional) Normalized phrase for verification

# Validations:
# - phrase must not be empty after strip()
# - Minimum length after removing spaces: at least 3 characters

# Test cases:
# 1) Normal: phrase="Anita lava la tina" -> Is palindrome: True
# 2) Border: phrase="aba" -> Is palindrome: True
# 3) Error: phrase="  " -> Error: invalid input

def palindrome_checker():
    phrase = input("Enter a phrase: ").strip()
    
    # Validation: not empty
    if len(phrase) == 0:
        print("Error: invalid input")
        return
    
    # Normalize: remove spaces and convert to lowercase
    normalized = phrase.replace(" ", "").lower()
    
    # Validation: minimum length
    if len(normalized) < 3:
        print("Error: invalid input")
        return
    
    # Check palindrome
    is_palindrome = normalized == normalized[::-1]
    
    # Output results
    print("Is palindrome:", is_palindrome)
    print("Normalized phrase:", normalized)

# Run Problem 3
if __name__ == "__main__":
    palindrome_checker()

# =================== Problem 4: Sentence Word Stats (Lengths and First/Last Word) ===================
# Description: Given a sentence, normalize spaces, separate words, and display statistics:
# - Total number of words
# - First word
# - Last word
# - Shortest word
# - Longest word

# Inputs:
# - sentence (str): input sentence

# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"

# Validations:
# - sentence must not be empty after strip()
# - Must contain at least one valid word after split()

# Test cases:
# 1) Normal: sentence="The quick brown fox" -> Word count: 4, First: "The", Last: "fox", Shortest: "The", Longest: "quick"
# 2) Border: sentence="Hello" -> Word count: 1, First: "Hello", Last: "Hello", Shortest: "Hello", Longest: "Hello"
# 3) Error: sentence="   " -> Error: invalid input

def sentence_word_stats():
    sentence = input("Enter a sentence: ").strip()
    
    # Validation: not empty
    if len(sentence) == 0:
        print("Error: invalid input")
        return
    
    # Split into words
    words = sentence.split()
    
    # Validation: must have at least one word
    if len(words) == 0:
        print("Error: invalid input")
        return
    
    # Count words
    word_count = len(words)
    
    # First and last word
    first_word = words[0]
    last_word = words[-1]
    
    # Find shortest and longest word
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    
    # Output results
    print("Word count:", word_count)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)

# Run Problem 4
if __name__ == "__main__":
    sentence_word_stats()

# =================== Problem 5: Password Strength Classifier ===================
# Description: Classifies a password as "weak", "medium", or "strong" based on minimal rules.
# Rules used:
# - Weak: length < 8 or all lowercase or very simple
# - Medium: length >= 8 and mix of letters (upper/lower) or digits
# - Strong: length >= 8 and contains at least one uppercase, one lowercase, one digit, and one symbol

# Inputs:
# - password_input (str): password string

# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"

# Validations:
# - Password must not be empty
# - Check length using len()

# Test cases:
# 1) Normal: password_input="Abc123!" -> Password strength: strong
# 2) Border: password_input="abcdefg" -> Password strength: weak
# 3) Error: password_input="" -> Error: invalid input

def password_strength_classifier():
    password_input = input("Enter a password: ").strip()
    
    # Validation: not empty
    if len(password_input) == 0:
        print("Error: invalid input")
        return
    
    length = len(password_input)
    
    # Initialize flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    
    # Check each character
    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True
    
    # Determine strength
    if length < 8 or (has_lower and not (has_upper or has_digit or has_symbol)):
        strength = "weak"
    elif length >= 8 and ((has_upper or has_lower) and has_digit):
        # Medium if meets length and has letters+digits but not all conditions for strong
        if has_upper and has_lower and has_digit and has_symbol:
            strength = "strong"
        else:
            strength = "medium"
    else:
        strength = "weak"
    
    # Output result
    print("Password strength:", strength)

# Run Problem 5
if __name__ == "__main__":
    password_strength_classifier()

# =================== Problem 6: Product Label Formatter (Fixed-Width Text) ===================
# Description: Given a product name and its price, generate a single-line label:
# Product: <NAME> | Price: $<PRICE>
# The label must be exactly 30 characters:
# - Pad with spaces if shorter
# - Truncate if longer

# Inputs:
# - product_name (str)
# - price_value (float or string convertible to float)

# Outputs:
# - "Label: <exactly 30 characters>"

# Validations:
# - product_name must not be empty after strip()
# - price_value must be convertible to a positive number

# Test cases:
# 1) Normal: product_name="Apple", price_value=2.5 -> Label: "Product: Apple | Price: $2.5      "
# 2) Border: product_name="LongProductNameExceeding", price_value=123.45 -> Label truncated to 30 chars
# 3) Error: product_name="   ", price_value=-5 -> Error: invalid input

def product_label_formatter():
    product_name = input("Enter product name: ").strip()
    price_input = input("Enter price: ").strip()
    
    # Validation: product_name not empty
    if len(product_name) == 0:
        print("Error: invalid input")
        return
    
    # Validation: price convertible to float and positive
    try:
        price_value = float(price_input)
        if price_value < 0:
            print("Error: invalid input")
            return
    except ValueError:
        print("Error: invalid input")
        return
    
    # Form label
    label = f"Product: {product_name} | Price: ${price_value}"
    
    # Adjust to exactly 30 characters
    if len(label) < 30:
        label = label + " " * (30 - len(label))
    elif len(label) > 30:
        label = label[:30]
    
    # Output
    print(f'Label: "{label}"')  # quotes to visualize spaces

# Run Problem 6
if __name__ == "__main__":
    product_label_formatter()


# =================== Conclusions ===================
# Strings are essential for input and output formatting in programs.
# Functions like strip(), lower(), split(), join() help normalize and process text reliably.
# Normalizing text before comparisons avoids unexpected mismatches.
# Proper validations prevent errors and garbage data from entering calculations or outputs.
# String immutability requires creating new strings when slicing, padding, or concatenating.
# Using slices and length checks allows precise control over display formats and alignment.
# These principles are critical when generating labels, formatting names, or processing user input.

# References:
# 1) Python Software Foundation. "Built-in Types — str". En: Python Documentation.
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# 2) Python Software Foundation. "String Methods". En: Python Documentation.
#    https://docs.python.org/3/library/stdtypes.html#string-methods
#
# 3) Sweigart, Al. "Automate the Boring Stuff with Python", 2nd Edition.
#    No Starch Press, 2019. (Capítulo 6: Manipulating Strings)
#
# 4) Lutz, Mark. "Learning Python", 5th Edition.
#    O’Reilly Media, 2013. (Sección sobre tipos de datos y strings)
#
# 5) Real Python. "Guide to String Manipulation in Python".
#    https://realpython.com/python-strings/
