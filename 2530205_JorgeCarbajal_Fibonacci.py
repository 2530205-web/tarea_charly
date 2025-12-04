#nombre: Jorge Candelario Carbajal Carrizales
#matricula: 2530205
#grupo: IM 1-2

# Resumen ejecutivo
# --------------------------------------------------
# Este documento presenta la resolución de seis problemas de programación usando funciones en Python.
# Una función en Python es un bloque de código reutilizable que recibe entradas (parámetros) y puede devolver resultados (return).
# Los parámetros son variables definidas en la función, mientras que los argumentos son los valores que se pasan al llamar la función.
# Separar la lógica en funciones permite organizar el código, evitar repeticiones y facilitar pruebas y mantenimiento.
# Se utilizan valores por defecto en parámetros para mayor flexibilidad y argumentos nombrados para mayor claridad.
# El documento incluye la definición de funciones, validaciones de entradas, pruebas con casos normales, borde y de error.
# Se aplican funciones puras cuando es posible, evitando efectos secundarios innecesarios y asegurando resultados consistentes.
# Los problemas abordan cálculo de áreas, clasificación de calificaciones, estadísticas de listas, aplicación de descuentos, saludos personalizados y cálculo de factoriales.

# ================================================================
# PROBLEM 1: Fibonacci series generator
# ================================================================
# Description:
# Program that reads an integer n and prints the first n terms of the
# Fibonacci series starting at 0 and 1.
#
# Inputs:
# - n (int; number of terms to generate)
#
# Outputs:
# - "Fibonacci series:" followed by the n terms separated by spaces
#
# Validations:
# - n must be an integer
# - n must be >= 1
# - (Optional) n <= 50 to avoid extremely large outputs
#
# Test cases:
# 1) Normal case:
#    n = 7 → output: 0 1 1 2 3 5 8
# 2) Border case:
#    n = 1 → output: 0
# 3) Error case:
#    n = -3 → "Error: invalid input"
#
# (Optional diagrams)
# - Flowchart (described):
#   "Start → Read n → Validate n → Loop to generate series → Print result → End"


def fibonacci_program():
    user_input = input("Enter the number of terms: ").strip()

    # Validate integer
    if not user_input.isdigit():
        print("Error: invalid input")
        return

    n = int(user_input)

    # Validate valid range
    if n < 1 or n > 50:
        print("Error: invalid input")
        return

    # Generate Fibonacci series
    fib_series = []

    if n >= 1:
        fib_series.append(0)
    if n >= 2:
        fib_series.append(1)

    # Loop to generate the series
    for _ in range(2, n):
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)

    print("Fibonacci series:", *fib_series)


# Run program
if __name__ == "__main__":
    fibonacci_program()


# ================================================================
# CONCLUSIONS
# ================================================================
# Using a loop made it easier to generate each Fibonacci term efficiently.
# Handling special cases like n = 1 and n = 2 ensures correct program behavior.
# The logic for Fibonacci can be reused in other algorithms involving sequences.
# Input validation is crucial to avoid incorrect or unpredictable results.
# Separating logic and documentation helps maintain clarity in program design.

# Referencias
# --------------------------------------------------
# 1) Python Software Foundation. "Functions — Python 3 Documentation." https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) Zelle, J. "Python Programming: An Introduction to Computer Science." 3rd Edition. Franklin, Beedle & Associates, 2017.
# 3) W3Schools. "Python Functions." https://www.w3schools.com/python/python_functions.asp

#repositorio
#https://github.com/2530205-web/tarea_charly
#https://github.com/2530205-web/tarea_charly/blob/main/2530205_JorgeCarbajal_Fibonacci.py