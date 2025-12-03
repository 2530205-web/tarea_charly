#nombre: Jorge Candelario Carbajal Carrizales
#matricula: 2530205
#grupo: IM 1-2

# Resumen Ejecutivo
# En Python, una función es una unidad de código reutilizable que encapsula una tarea y
# permite organizar programas de forma más clara y modular. Los parámetros se definen en la
# función y representan los valores que ésta necesita, mientras que los argumentos son los
# datos reales que se envían al llamarla. Separar la lógica en funciones mejora la
# legibilidad, evita duplicación de código y facilita las pruebas individuales. El valor de
# retorno permite enviar resultados de manera controlada, lo cual es más flexible que
# imprimir directamente dentro de la función. Este documento presenta seis problemas que
# ilustran el uso de funciones con parámetros, valores por defecto, argumentos posicionales
# y nombrados, además de validaciones y casos de prueba que demuestran su comportamiento en
# contextos como cálculos geométricos, clasificación, estadísticas, descuentos, saludos y
# factoriales.


# =================== Problem 1: Rectangle Area and Perimeter ===================
# Description: Defines two functions to calculate the area and perimeter of a rectangle.
# The main code reads or defines width and height, calls the functions, and shows the results.

# Inputs:
# - width (float)
# - height (float)

# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>

# Validations:
# - width > 0
# - height > 0
# - If invalid, print "Error: invalid input" and do not call the functions

# Test cases:
# 1) Normal: width = 5, height = 3 -> Area: 15, Perimeter: 16
# 2) Border: width = 0.1, height = 0.1 -> Area: 0.01, Perimeter: 0.2
# 3) Error: width = -2, height = 5 -> Error: invalid input

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def rectangle_calculations():
    try:
        width = float(input("Enter rectangle width: ").strip())
        height = float(input("Enter rectangle height: ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    if width <= 0 or height <= 0:
        print("Error: invalid input")
        return

    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    print("Area:", round(area, 2))
    print("Perimeter:", round(perimeter, 2))

# Run Problem 1
if __name__ == "__main__":
    rectangle_calculations()

# =================== Problem 2: Grade Classifier ===================
# Description: Defines a function classify_grade(score) that returns a letter grade based on numeric score.

# Inputs:
# - score (float or int)

# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>

# Validations:
# - 0 <= score <= 100
# - If invalid, print "Error: invalid input"

# Test cases:
# 1) score = 95 -> Category: A
# 2) score = 82 -> Category: B
# 3) score = 73 -> Category: C
# 4) score = 67 -> Category: D
# 5) score = 50 -> Category: F
# 6) score = -5 -> Error: invalid input
# 7) score = 105 -> Error: invalid input

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def grade_classification():
    try:
        score = float(input("Enter the score (0-100): ").strip())
    except ValueError:
        print("Error: invalid input")
        return

    if score < 0 or score > 100:
        print("Error: invalid input")
        return

    grade = classify_grade(score)
    print("Score:", score)
    print("Category:", grade)

# Run Problem 2
if __name__ == "__main__":
    grade_classification()

# =================== Problem 3: List Statistics Function ===================
# Description: Defines a function summarize_numbers(numbers_list) that returns
# a dictionary with minimum, maximum, and average of a list of numbers.

# Inputs:
# - numbers_text (string; e.g., "10,20,30")

# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>

# Validations:
# - numbers_text not empty after strip()
# - All elements convertible to float
# - List not empty after conversion

# Test cases:
# 1) numbers_text = "10,20,30" -> Min: 10.0, Max: 30.0, Average: 20.0
# 2) numbers_text = "5" -> Min: 5.0, Max: 5.0, Average: 5.0
# 3) numbers_text = "" -> Error: invalid input
# 4) numbers_text = "10,abc,30" -> Error: invalid input

def summarize_numbers(numbers_list):
    if not numbers_list:
        return None
    summary = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return summary

def list_statistics():
    numbers_text = input("Enter numbers separated by commas: ").strip()
    if not numbers_text:
        print("Error: invalid input")
        return

    number_strs = numbers_text.split(",")
    numbers_list = []
    for num_str in number_strs:
        num_str = num_str.strip()
        try:
            number = float(num_str)
        except ValueError:
            print("Error: invalid input")
            return
        numbers_list.append(number)

    if not numbers_list:
        print("Error: invalid input")
        return

    stats = summarize_numbers(numbers_list)
    print("Min:", stats["min"])
    print("Max:", stats["max"])
    print("Average:", round(stats["average"], 2))

# Run Problem 3
if __name__ == "__main__":
    list_statistics()

# =================== Problem 4: Apply Discount List (Pure Function) ===================
# Description:
# Defines a function apply_discount(prices_list, discount_rate) that returns
# a NEW list with discounted prices, without modifying the original list.
#
# Inputs:
# - prices_text (string; e.g., "100,200,300")
# - discount_rate (float between 0 and 1)
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
#
# Validations:
# - prices_text not empty after strip()
# - List not empty after conversion
# - All prices > 0
# - 0 <= discount_rate <= 1, otherwise: "Error: invalid input"
#
# Suggested operations:
# - Build list of floats from input text
# - Pure function must create a new list using:
#       discounted_price = price * (1 - discount_rate)


def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted


def discount_program():
    prices_text = input("Enter prices separated by commas: ").strip()
    if not prices_text:
        print("Error: invalid input")
        return

    discount_input = input("Enter discount rate (0 to 1): ").strip()
    try:
        discount_rate = float(discount_input)
    except ValueError:
        print("Error: invalid input")
        return

    if discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
        return

    price_strs = prices_text.split(",")
    prices_list = []

    for p_str in price_strs:
        p_str = p_str.strip()
        try:
            price = float(p_str)
        except ValueError:
            print("Error: invalid input")
            return
        if price <= 0:
            print("Error: invalid input")
            return
        prices_list.append(price)

    if not prices_list:
        print("Error: invalid input")
        return

    discounted_prices = apply_discount(prices_list, discount_rate)

    print("Original prices:", prices_list)
    print("Discounted prices:", discounted_prices)


# Run Problem 4
if __name__ == "__main__":
    discount_program()

# =================== Problem 5: Greeting Function with Default Parameters ===================
# Description:
# Defines a function greet(name, title="") that optionally adds a title before a name.
# Returns: "Hello, <full_name>!"
#
# Inputs:
# - name (string)
# - title (optional string)
#
# Outputs:
# - "Greeting:" <greeting_message>
#
# Validations:
# - name not empty after strip()
# - title may be empty, but if provided it should be stripped
#
# Suggested operations:
# - Use default parameter: def greet(name, title="")
# - Use named arguments: greet(name="Alice", title="Dr.")


def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if not name:
        return None

    if title:
        full_name = title + " " + name
    else:
        full_name = name

    return f"Hello, {full_name}!"


def greeting_program():
    name_input = input("Enter a name: ").strip()
    if not name_input:
        print("Error: invalid input")
        return

    title_input = input("Enter a title (optional): ").strip()

    # Call function using positional arguments
    greeting1 = greet(name_input, title_input)

    if greeting1 is None:
        print("Error: invalid input")
        return

    print("Greeting:", greeting1)

    # Demonstration using named arguments
    # (this will always run with fixed example values)
    example_greeting = greet(name=name_input, title=title_input)
    # Or default title:
    # example_greeting = greet(name=name_input)

    print("Greeting (named args):", example_greeting)


# Run Problem 5
if __name__ == "__main__":
    greeting_program()

# =================== Problem 6: Factorial Function (Iterative Implementation) ===================
# Description:
# Defines a function factorial(n) that returns n! (n factorial).
# Implementation choice: ITERATIVE (using a for loop) for simplicity and to avoid recursion limits.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be an integer
# - n >= 0
# - Optional safety limit: n <= 20 to avoid excessively large results
#   If not valid → print "Error: invalid input"
#
# Suggested operations:
# Iterative version:
#   result = 1
#   for i in range(1, n + 1): result *= i


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_program():
    n_input = input("Enter a non-negative integer: ").strip()

    # Validate integer
    if not n_input.isdigit():
        print("Error: invalid input")
        return

    n = int(n_input)

    # Validate non-negative
    if n < 0 or n > 20:
        print("Error: invalid input")
        return

    fact_value = factorial(n)

    print("n:", n)
    print("Factorial:", fact_value)


# Run Problem 6
if __name__ == "__main__":
    factorial_program()



# =================== 8. CONCLUSIONES ===================
# Las funciones permiten organizar mejor el código, separando tareas específicas.
# Esto hace que el programa sea más claro y fácil de mantener.
# Usar return es útil porque nos permite reutilizar los valores sin depender de prints.
# Los parámetros y valores por defecto vuelven las funciones más flexibles.
# Encapsular lógica en funciones es especialmente útil en cálculos repetidos o validaciones.
# Aprendí a distinguir entre la lógica principal (flujo del programa) y las funciones de apoyo.
# Este proyecto mostró cómo dividir el código en componentes reutilizables mejora la claridad.
# También comprendí la importancia de validar entradas antes de procesarlas.

# References
# 1. Python Official Documentation – Functions
#    Python Software Foundation. 
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 2. Real Python – Defining Your Own Python Function
#    Real Python, 2023.
#    https://realpython.com/defining-your-own-python-function/
#
# 3. W3Schools – Python Functions
#    W3Schools
#    https://www.w3schools.com/python/python_functions.asp
#
# 4. Think Python: How to Think Like a Computer Scientist
#    Allen B. Downey, 2nd Edition, 2015. Chapter 4: Functions
#
# 5. GeeksforGeeks – Python Functions
#    GeeksforGeeks, 2023
#    https://www.geeksforgeeks.org/python-functions/

