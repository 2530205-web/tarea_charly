#nombre: Jorge Candelario Carbajal Carrizales
#matricula: 2530205
#grupo: IM 1-2

# Resumen Ejecutivo
# En Python, los tipos int y float permiten representar cantidades numéricas enteras y
# decimales para realizar cálculos aritméticos reales, mientras que los valores booleanos
# (True/False) se generan principalmente a partir de comparaciones y sirven para tomar
# decisiones dentro de un programa. La validación de datos de entrada es esencial para
# evitar errores comunes, como divisiones entre cero, rangos inválidos o datos imposibles
# de convertir. Este documento desarrolla seis problemas prácticos que integran conversión
# de tipos, operaciones aritméticas, operadores relacionales y lógicos, así como el uso de
# banderas booleanas para controlar la lógica. Cada problema incluye su descripción, las
# entradas y salidas esperadas, las validaciones correspondientes y tres casos de prueba
# que aseguran un comportamiento correcto y robusto del programa.



# =================== Problem 1: Temperature Converter and Range Flag ===================
# Description: Converts a temperature in Celsius (float) to Fahrenheit and Kelvin.
# Additionally, it determines a boolean is_high_temperature that is True if Celsius >= 30.0, otherwise False.

# Inputs:
# - temp_c (float): temperature in Celsius

# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" True|False

# Validations:
# - Check that temp_c can be converted to float
# - Ensure physical temperatures are possible (Kelvin >= 0.0)

# Test cases:
# 1) Normal: temp_c = 25.0 -> Fahrenheit: 77.0, Kelvin: 298.15, High temperature: False
# 2) Border: temp_c = 30.0 -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: True
# 3) Error: temp_c = -300.0 -> Error: invalid input (Kelvin < 0)

def temperature_converter():
    temp_input = input("Enter temperature in Celsius: ")
    
    # Validation: check if input can be converted to float
    try:
        temp_c = float(temp_input)
    except ValueError:
        print("Error: invalid input")
        return
    
    # Convert Celsius to Kelvin
    temp_k = temp_c + 273.15
    
    # Validation: Kelvin cannot be negative
    if temp_k < 0.0:
        print("Error: invalid input")
        return
    
    # Convert Celsius to Fahrenheit
    temp_f = temp_c * 9 / 5 + 32
    
    # Determine if temperature is high
    is_high_temperature = temp_c >= 30.0
    
    # Output results
    print("Fahrenheit:", round(temp_f, 2))
    print("Kelvin:", round(temp_k, 2))
    print("High temperature:", is_high_temperature)

# Run Problem 1
if __name__ == "__main__":
    temperature_converter()


# =================== Problem 2: Work Hours and Overtime Payment ===================
# Description: Calculates the weekly total payment for a worker.
# Regular hours up to 40 are paid at hourly_rate.
# Overtime hours (>40) are paid at 150% of the normal rate.
# Generates a boolean has_overtime indicating if the worker did overtime.

# Inputs:
# - hours_worked (float): hours worked in the week
# - hourly_rate (float): payment per hour

# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" True|False

# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
# - If validation fails, display "Error: invalid input"

# Test cases:
# 1) Normal: hours_worked = 45, hourly_rate = 20 -> Regular: 800, Overtime: 150, Total: 950, Has overtime: True
# 2) Border: hours_worked = 40, hourly_rate = 15 -> Regular: 600, Overtime: 0, Total: 600, Has overtime: False
# 3) Error: hours_worked = -5, hourly_rate = 10 -> Error: invalid input

def work_hours_payment():
    hours_input = input("Enter hours worked: ")
    rate_input = input("Enter hourly rate: ")
    
    # Validation: check if inputs can be converted to float
    try:
        hours_worked = float(hours_input)
        hourly_rate = float(rate_input)
    except ValueError:
        print("Error: invalid input")
        return
    
    # Validation: hours_worked >=0, hourly_rate >0
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
        return
    
    # Calculate regular and overtime hours
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)
    
    # Calculate payments
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    
    # Determine if worker has overtime
    has_overtime = hours_worked > 40
    
    # Output results
    print("Regular pay:", round(regular_pay, 2))
    print("Overtime pay:", round(overtime_pay, 2))
    print("Total pay:", round(total_pay, 2))
    print("Has overtime:", has_overtime)

# Run Problem 2
if __name__ == "__main__":
    work_hours_payment()

# =================== Problem 3: Discount Eligibility with Booleans ===================
# Description: Determines if a customer is eligible for a discount.
# Eligibility rules:
# - Discount applies if the customer is a student, a senior, or if purchase_total >= 1000.0.
# Calculates the final total with a 10% discount when eligible.

# Inputs:
# - purchase_total (float): total amount of purchase
# - is_student_text (str): "YES" or "NO"
# - is_senior_text (str): "YES" or "NO"

# Outputs:
# - "Discount eligible:" True|False
# - "Final total:" <final_total>

# Validations:
# - purchase_total >= 0.0
# - Convert is_student_text and is_senior_text to uppercase and then to boolean
# - If text is not "YES" or "NO", display "Error: invalid input"

# Test cases:
# 1) Normal: purchase_total=1200, is_student_text="NO", is_senior_text="NO" -> Discount eligible: True, Final total: 1080.0
# 2) Border: purchase_total=500, is_student_text="YES", is_senior_text="NO" -> Discount eligible: True, Final total: 450.0
# 3) Error: purchase_total=-50, is_student_text="MAYBE", is_senior_text="NO" -> Error: invalid input

def discount_eligibility():
    purchase_input = input("Enter purchase total: ")
    student_input = input("Is student? (YES/NO): ")
    senior_input = input("Is senior? (YES/NO): ")
    
    # Validate and convert purchase_total
    try:
        purchase_total = float(purchase_input)
    except ValueError:
        print("Error: invalid input")
        return
    
    if purchase_total < 0.0:
        print("Error: invalid input")
        return
    
    # Normalize text inputs to uppercase
    is_student_text = student_input.strip().upper()
    is_senior_text = senior_input.strip().upper()
    
    # Convert text to boolean
    if is_student_text == "YES":
        is_student = True
    elif is_student_text == "NO":
        is_student = False
    else:
        print("Error: invalid input")
        return
    
    if is_senior_text == "YES":
        is_senior = True
    elif is_senior_text == "NO":
        is_senior = False
    else:
        print("Error: invalid input")
        return
    
    # Determine discount eligibility
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    
    # Calculate final total
    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total
    
    # Output results
    print("Discount eligible:", discount_eligible)
    print("Final total:", round(final_total, 2))

# Run Problem 3
if __name__ == "__main__":
    discount_eligibility()

# =================== Problem 4: Basic Statistics of Three Integers ===================
# Description: Reads three integers and calculates sum, average, maximum, minimum.
# Determines a boolean all_even indicating if all three numbers are even.

# Inputs:
# - n1 (int)
# - n2 (int)
# - n3 (int)

# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" True|False

# Validations:
# - Check that all three inputs can be converted to int

# Test cases:
# 1) Normal: n1=4, n2=6, n3=8 -> Sum: 18, Average: 6.0, Max: 8, Min: 4, All even: True
# 2) Border: n1=1, n2=2, n3=3 -> Sum: 6, Average: 2.0, Max: 3, Min: 1, All even: False
# 3) Error: n1="a", n2=5, n3=6 -> Error: invalid input

def basic_statistics():
    n1_input = input("Enter first integer: ")
    n2_input = input("Enter second integer: ")
    n3_input = input("Enter third integer: ")
    
    # Validation: check if inputs can be converted to int
    try:
        n1 = int(n1_input)
        n2 = int(n2_input)
        n3 = int(n3_input)
    except ValueError:
        print("Error: invalid input")
        return
    
    # Calculate sum
    sum_value = n1 + n2 + n3
    
    # Calculate average
    average_value = sum_value / 3
    
    # Find max and min
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    
    # Determine if all numbers are even
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    
    # Output results
    print("Sum:", sum_value)
    print("Average:", round(average_value, 2))
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)

# Run Problem 4
if __name__ == "__main__":
    basic_statistics()

# =================== Problem 5: Loan Eligibility (Income and Debt Ratio) ===================
# Description: Determines if a person is eligible for a loan based on monthly income, debt, and credit score.
# Calculates the debt ratio and evaluates eligibility according to given criteria.

# Inputs:
# - monthly_income (float): monthly income
# - monthly_debt (float): monthly debt payments
# - credit_score (int): credit score

# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" True|False

# Validations:
# - monthly_income > 0.0 (to avoid division by zero)
# - monthly_debt >= 0.0
# - credit_score >= 0
# - If validation fails, display "Error: invalid input"

# Test cases:
# 1) Normal: monthly_income=10000, monthly_debt=3000, credit_score=700 -> Debt ratio: 0.3, Eligible: True
# 2) Border: monthly_income=8000, monthly_debt=3200, credit_score=650 -> Debt ratio: 0.4, Eligible: True
# 3) Error: monthly_income=0, monthly_debt=500, credit_score=-50 -> Error: invalid input

def loan_eligibility():
    income_input = input("Enter monthly income: ")
    debt_input = input("Enter monthly debt: ")
    score_input = input("Enter credit score: ")
    
    # Validate and convert inputs
    try:
        monthly_income = float(income_input)
        monthly_debt = float(debt_input)
        credit_score = int(score_input)
    except ValueError:
        print("Error: invalid input")
        return
    
    # Validate ranges
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return
    
    # Calculate debt ratio
    debt_ratio = monthly_debt / monthly_income
    
    # Determine eligibility
    eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
    
    # Output results
    print("Debt ratio:", round(debt_ratio, 2))
    print("Eligible:", eligible)

# Run Problem 5
if __name__ == "__main__":
    loan_eligibility()

# =================== Problem 6: Body Mass Index (BMI) and Category Flag ===================
# Description: Calculates the Body Mass Index (BMI) of a person and determines weight category.
# Generates booleans indicating underweight, normal, or overweight.

# Inputs:
# - weight_kg (float): weight in kilograms
# - height_m (float): height in meters

# Outputs:
# - "BMI:" <bmi_rounded>
# - "Underweight:" True|False
# - "Normal:" True|False
# - "Overweight:" True|False

# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
# - If validation fails, display "Error: invalid input"

# Test cases:
# 1) Normal: weight_kg=70, height_m=1.75 -> BMI: 22.86, Underweight: False, Normal: True, Overweight: False
# 2) Border: weight_kg=50, height_m=1.60 -> BMI: 19.53, Underweight: False, Normal: True, Overweight: False
# 3) Error: weight_kg=-10, height_m=0 -> Error: invalid input

def bmi_calculator():
    weight_input = input("Enter weight in kg: ")
    height_input = input("Enter height in meters: ")
    
    # Validate and convert inputs
    try:
        weight_kg = float(weight_input)
        height_m = float(height_input)
    except ValueError:
        print("Error: invalid input")
        return
    
    # Validate positive values
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
        return
    
    # Calculate BMI
    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)
    
    # Determine category booleans
    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0
    
    # Output results
    print("BMI:", bmi_rounded)
    print("Underweight:", is_underweight)
    print("Normal:", is_normal)
    print("Overweight:", is_overweight)

# Run Problem 6
if __name__ == "__main__":
    bmi_calculator()

# =================== Conclusions ===================
# In these exercises, we observed how integers (int) and floating-point numbers (float)
# work together to perform accurate calculations, such as sums, averages, payments, and BMI.
# Comparisons between numbers generate boolean values (True/False), which are fundamental
# for making decisions using conditional statements like if and for evaluating eligibility rules.
# Validating input ranges and avoiding division by zero is crucial to prevent runtime errors
# and ensure realistic results, especially in financial and scientific calculations.
# Designing combined conditions with and, or, and not allows us to handle complex rules
# like discount eligibility, overtime detection, or loan approval in a clear and logical way.
# These patterns repeat across various real-world problems such as payroll, discounts, loans,
# and health metrics, highlighting the importance of precise data handling and logical reasoning.

# References:
# 1) Python Software Foundation. "Numeric Types — int, float, complex". 
#    Documentación oficial de Python.
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
#
# 2) Python Software Foundation. "Boolean Values — bool".
#    https://docs.python.org/3/library/stdtypes.html#boolean-values
#
# 3) Python Software Foundation. "Built-in Functions" (int(), float(), round(), etc.).
#    https://docs.python.org/3/library/functions.html
#
# 4) Sweigart, Al. "Automate the Boring Stuff with Python", 2nd Edition.
#    No Starch Press, 2019. (Capítulos sobre operadores y tipos numéricos)
#
# 5) Lutz, Mark. "Learning Python", 5th Edition.
#    O’Reilly Media, 2013. (Secciones sobre tipos numéricos, lógica y operadores)
