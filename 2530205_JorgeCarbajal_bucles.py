#nombre: Jorge Candelario Carbajal Carrizales
#matricula: 2530205
#grupo: IM 1-2

# Resumen Ejecutivo
# En Python, los bucles for y while permiten repetir instrucciones de forma controlada para
# recorrer secuencias, generar rangos numéricos, procesar entradas repetidas y construir
# menús interactivos. El bucle for se usa típicamente cuando se conoce de antemano la
# cantidad de iteraciones, mientras que el bucle while es más adecuado cuando la repetición
# depende de una condición dinámica o de un sentinela definido por el usuario. Los
# contadores y acumuladores facilitan el seguimiento de cantidades y la suma de valores
# durante la ejecución del bucle. Es fundamental establecer condiciones de salida claras
# para evitar ciclos infinitos y garantizar programas seguros. Este documento aborda seis
# problemas que aplican estas estructuras en escenarios prácticos como sumas, tablas,
# lectura de datos, intentos de contraseña, menús y patrones impresos, incluyendo
# validaciones, entradas, salidas y casos de prueba completos.


# =================== Problem 1: Sum of Range with For ===================
# Description: Calculates the sum of all integers from 1 to n (inclusive).
# Additionally, calculates the sum of even numbers in that range using a for loop.

# Inputs:
# - n (int): upper limit of the range

# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>

# Validations:
# - Check that n can be converted to int
# - n >= 1; if not, display "Error: invalid input"

# Test cases:
# 1) Normal: n = 5 -> Sum 1..n: 15, Even sum 1..n: 6
# 2) Border: n = 1 -> Sum 1..n: 1, Even sum 1..n: 0
# 3) Error: n = -3 -> Error: invalid input

def sum_of_range():
    n_input = input("Enter an integer n: ")
    
    # Validation: check if input can be converted to int
    try:
        n = int(n_input)
    except ValueError:
        print("Error: invalid input")
        return
    
    # Validation: n must be >= 1
    if n < 1:
        print("Error: invalid input")
        return
    
    # Initialize sums
    total_sum = 0
    even_sum = 0
    
    # Calculate sums using for loop
    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i
    
    # Output results
    print("Sum 1..n:", total_sum)
    print("Even sum 1..n:", even_sum)

# Run Problem 1
if __name__ == "__main__":
    sum_of_range()

# =================== Problem 2: Multiplication Table with For ===================
# Description: Generates and displays the multiplication table of a base number from 1 to m.
# For example, if base = 5 and m = 4, it displays:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20

# Inputs:
# - base (int): the base number
# - m (int): upper limit of the table

# Outputs:
# - One line per multiplication, e.g. "5 x 1 = 5"

# Validations:
# - Check that base and m can be converted to int
# - m >= 1; if not, display "Error: invalid input"

# Test cases:
# 1) Normal: base = 5, m = 4 -> prints 5 x 1 = 5 ... 5 x 4 = 20
# 2) Border: base = 3, m = 1 -> prints 3 x 1 = 3
# 3) Error: base = 7, m = 0 -> Error: invalid input

def multiplication_table():
    base_input = input("Enter the base number: ")
    m_input = input("Enter the table limit m: ")
    
    # Validation: convert inputs to int
    try:
        base = int(base_input)
        m = int(m_input)
    except ValueError:
        print("Error: invalid input")
        return
    
    # Validation: m must be >= 1
    if m < 1:
        print("Error: invalid input")
        return
    
    # Generate multiplication table
    for i in range(1, m + 1):
        product = base * i
        print(f"{base} x {i} = {product}")

# Run Problem 2
if __name__ == "__main__":
    multiplication_table()

# =================== Problem 3: Average of Numbers with While and Sentinel ===================
# Description: Reads numbers one by one until a sentinel value is entered (e.g., -1).
# Calculates the average of valid numbers and the count of numbers read.
# If only the sentinel is entered without valid numbers, displays an error.

# Inputs:
# - number (float): repeatedly entered by user
# - sentinel_value (float): fixed in code, e.g., -1

# Outputs:
# - "Count:" <count>
# - "Average:" <average_value>
# - If no valid numbers entered: "Error: no data"

# Validations:
# - Each input should be convertible to float
# - Sentinel value is ignored in calculations

# Test cases:
# 1) Normal: 5, 10, -1 -> Count: 2, Average: 7.5
# 2) Border: -1 -> Error: no data
# 3) Error: non-numeric input -> skips or displays error

def average_with_sentinel():
    SENTINEL = -1
    total = 0.0
    count = 0
    
    while True:
        user_input = input("Enter a number (-1 to stop): ")
        try:
            number = float(user_input)
        except ValueError:
            print("Error: invalid input")
            continue
        
        if number == SENTINEL:
            break
        
        total += number
        count += 1
    
    if count == 0:
        print("Error: no data")
    else:
        average = total / count
        print("Count:", count)
        print("Average:", round(average, 2))

# Run Problem 3
if __name__ == "__main__":
    average_with_sentinel()

# =================== Problem 4: Password Attempts with While ===================
# Description: Implements a simple password attempt system.
# The user has a limited number of attempts to enter the correct password.
# Success or account locked messages are displayed accordingly.

# Inputs:
# - user_password (string): entered by user in each attempt

# Outputs:
# - If correct: "Login success"
# - If all attempts fail: "Account locked"

# Validations:
# - MAX_ATTEMPTS > 0 (defined in code)
# - Count attempts correctly

# Test cases:
# 1) Normal: correct password on 2nd attempt -> Login success
# 2) Border: correct password on 1st attempt -> Login success
# 3) Error: all attempts incorrect -> Account locked

def password_attempts():
    CORRECT_PASSWORD = "admin123"
    MAX_ATTEMPTS = 3
    attempts = 0
    
    while attempts < MAX_ATTEMPTS:
        user_input = input("Enter password: ").strip()
        attempts += 1
        
        if user_input == CORRECT_PASSWORD:
            print("Login success")
            break
    else:
        # Executed if while loop completes without break
        print("Account locked")

# Run Problem 4
if __name__ == "__main__":
    password_attempts()

# =================== Problem 5: Simple Menu with While ===================
# Description: Implements a text menu that repeats until the user selects the exit option.
# Executes the action corresponding to each option and redisplays the menu until 0 is chosen.

# Inputs:
# - option (string or int): user's choice

# Outputs:
# - "Hello!" for greeting
# - "Counter:" <counter_value> to show counter
# - "Counter incremented" after increment
# - "Bye!" when exiting
# - "Error: invalid option" for invalid selections

# Validations:
# - Convert option to int safely
# - Accept only 0, 1, 2, 3 as valid options

# Test cases:
# 1) Normal: choose 1, 2, 3, then 0 -> proper messages displayed
# 2) Border: choose 0 immediately -> "Bye!"
# 3) Error: choose 5 -> "Error: invalid option"

def simple_menu():
    counter = 0
    
    while True:
        print("\nMenu:")
        print("1) Show greeting")
        print("2) Show current counter value")
        print("3) Increment counter")
        print("0) Exit")
        
        option_input = input("Select an option: ").strip()
        
        # Validation: convert to int
        try:
            option = int(option_input)
        except ValueError:
            print("Error: invalid option")
            continue
        
        if option == 1:
            print("Hello!")
        elif option == 2:
            print("Counter:", counter)
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
            break
        else:
            print("Error: invalid option")

# Run Problem 5
if __name__ == "__main__":
    simple_menu()


# =================== Problem 6: Pattern Printing with Nested Loops ===================
# Description: Uses nested for loops to print a right-angled triangle of asterisks.
# Optionally prints an inverted triangle pattern (documented in code).

# Inputs:
# - n (int): number of rows of the pattern

# Outputs:
# - Line by line:
#   "*"
#   "**"
#   "***"
#   "****"
# - (Optional) inverted pattern if implemented

# Validations:
# - n must be convertible to int
# - n >= 1, otherwise "Error: invalid input"

# Test cases:
# 1) Normal: n = 4 -> prints triangle with 4 rows
# 2) Border: n = 1 -> prints single "*"
# 3) Error: n = 0 or n = -3 -> Error: invalid input

def pattern_printing():
    n_input = input("Enter number of rows for pattern: ").strip()
    
    # Validation: convert to int
    try:
        n = int(n_input)
        if n < 1:
            print("Error: invalid input")
            return
    except ValueError:
        print("Error: invalid input")
        return
    
    # Right-angled triangle
    print("\nRight-angled triangle:")
    for i in range(1, n + 1):
        print("*" * i)
    
    # Optional inverted triangle
    print("\nInverted triangle:")
    for i in range(n, 0, -1):
        print("*" * i)

# Run Problem 6
if __name__ == "__main__":
    pattern_printing()

# =================== Conclusions ===================
# - For loops are ideal when the number of iterations is known; while loops work well with unknown iterations or sentinel values.
# - Counters and accumulators inside loops are key for summing, counting, or tracking state.
# - While loops carry the risk of infinite loops if the termination condition is never met.
# - Menus and password attempts are classic examples of while loops in practice.
# - Nested loops are powerful for generating patterns, such as triangles, grids, or tables.

# References:
# 1) Python Software Foundation. "The for statement — Python Docs".
#    https://docs.python.org/3/tutorial/controlflow.html#for-statements
#
# 2) Python Software Foundation. "The while statement — Python Docs".
#    https://docs.python.org/3/tutorial/controlflow.html#the-while-statement
#
# 3) Python Software Foundation. "Built-in Functions (range, len, sum)".
#    https://docs.python.org/3/library/functions.html
#
# 4) Sweigart, Al. *Automate the Boring Stuff with Python*, 2nd Edition.
#    No Starch Press, 2019. (Capítulos sobre bucles, control de flujo y lógica repetitiva)
#
# 5) Lutz, Mark. *Learning Python*, 5th Edition.
#    O’Reilly Media, 2013. (Secciones sobre for, while, iteraciones y patrones de programación)
