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
# The Fibonacci series is a sequence where each term is the sum of the
# previous two. Calculating the series up to n terms means generating
# the first n values starting from 0 and 1. This program reads an integer,
# validates it, and prints the first n Fibonacci terms. It demonstrates
# input validation, loop usage, and structured program design.

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

# ================================================================
# REFERENCES
# ================================================================
# 1) Python Documentation - For and While Loops.
# 2) Fibonacci sequence tutorials (RealPython, W3Schools).
# 3) Class notes and official course materials.

# ================================================================
# GITHUB REPOSITORY URL
# ================================================================
# Add your repository URL here:
# https://github.com/_________________________
