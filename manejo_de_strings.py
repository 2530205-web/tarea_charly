

'''
#resumen ejecutivo
# *¿Qué es un string en Python? Es un tipo de dato que representa texto y es inmutable,
 lo que significa que no puede modificarse directamente una vez creado.
# *¿Qué operaciones básicas se pueden realizar? Se puede concatenar texto,
 obtener su longitud con len(), extraer subcadenas usando slicing,
 buscar patrones con find() o usando "in", y reemplazar partes del texto con replace().
# *¿Por qué es importante validar y normalizar texto de entrada?
 Porque evita errores, asegura que los datos sean correctos (como nombres o correos),
 mejora la seguridad al procesar datos sensibles (como contraseñas),
 y garantiza que el programa funcione correctamente con entradas limpias y consistentes.
#que cubrira este documento:?
Problema 1: Full name formatter
Descripción:
El programa recibe un nombre completo y debe normalizarlo quitando espacios extra y corrigiendo mayúsculas/minúsculas. Luego muestra el nombre en Title Case y genera las iniciales.
Entradas: una cadena de texto con nombre completo.
Salidas: nombre formateado + iniciales.
Validaciones:
No estar vacío.
Debe contener mínimo dos palabras.
Métodos de string usados:
strip(), split(), title(), upper(), len().

Problema 2: Simple email validator
Descripción:
Verifica si un correo tiene formato válido mínimo (parte antes del @, dominio y extensión).
Entradas: correo electrónico.
Salidas: mensaje indicando si es válido o no.
Validaciones:
Debe contener un @.
Debe contener un punto después del @.
No debe iniciar ni terminar con @ o punto.
Métodos de string usados:
strip(), count(), find(), split().

Problema 3: Palindrome checker
Descripción:
Determina si una frase es palíndromo ignorando espacios y mayúsculas.
Entradas: frase.
Salidas: “Es palíndromo” o “No es palíndromo”.
Validaciones:
No estar vacía después de limpiar espacios.
Métodos de string usados:
replace(), lower(), strip(), slicing [:: -1].

Problema 4: Sentence word stats
Descripción:
Recibe una oración y muestra estadísticas: cantidad de palabras, primera, última, palabra más corta y más larga.
Entradas: oración.
Salidas: estadísticas de palabras.
Validaciones:
No estar vacía.
Debe contener al menos una palabra.
Métodos de string usados:
strip(), split(), len(), comparación de longitudes.

Problema 5: Password strength classifier
Descripción:
Clasifica una contraseña como weak, medium o strong según reglas (longitud, mezcla de caracteres, símbolos).
Entradas: contraseña.
Salidas: nivel de fortaleza.
Validaciones:
No vacía.
Revisar longitud y tipos de caracteres.
Métodos de string usados:
len(), isupper(), islower(), isdigit(), búsqueda de símbolos.

Problema 6: Product label formatter
Descripción:
Genera una etiqueta en una línea con formato fijo de 30 caracteres. Si es más corta, se rellena con espacios; si es más larga, se recorta.
Entradas: nombre del producto y precio.
Salidas: cadena formateada de 30 caracteres.
Validaciones:
Nombre y precio no vacíos.
Precio debe ser numérico.
Métodos de string usados:
strip(), concatenación, ljust(), slicing [0:30].
'''



'''
#problem 1: full name formatter(name+initials)
'este programa recibe un nombre completo y debe normalizarlo quitando espacios extra y corrigiendo mayúsculas/minúsculas.'
' Luego muestra el nombre en Title Case y genera las iniciales.'

##full name
full_name = input('Enter your full name: ')
full_name=full_name.strip()
if len(full_name) == 0:
    print('error: cannot be empty')
else:
    print(full_name.title())# title hace la primera mayusucla lo demas minuscula

##initials
initials = full_name.split()
if len(initials) < 2:
    print('error: please enter at least first name and last name')
else:
    for name in initials:
        print(name[0].upper(), end='.') #si no uso end hubiera salido en 2 lineas las iniciales.
'''
'''
#Tabla de Casos de Prueba
caso de prueba normal:               prueba borde:                   caso de prueba erróneo:
entrada: "  juan perez  "            entrada:'JuAn  PeReZ'           entrada: "   "
salida esperada:                     salida esperada:                salida esperada:      
Juan Perez                           Juan Perez                      error: cannot be empty
J.P.                                 J.P.                            error: please enter at least first name and last name
'''
'''
#problem 2: simple email validator

'verifica si un correo tiene formato válido mínimo (parte antes del @, dominio y extensión'

email = input("Enter an email: ")

# Quitar espacios al inicio y al final
email = email.strip()

# Verificar si un correo tiene formato  válido
# (parte antes del @, dominio y extensión)
if email.count("@") != 1:
    print("Invalid email: it must contain exactly one '@'.")
else:
    # Posición de la arroba
    at_pos = email.find("@")

    # Parte antes de la arroba (@)
    local_part = email[:at_pos]
    # Dominio completo (después de la arroba)
    domain = email[at_pos + 1 : ]

    # Validar que haya algo antes del @ y algo después
    if local_part == "":
        print("Invalid email: missing part before '@'.")
    elif domain == "":
        print("Invalid email: missing domain after '@'.")
    else:
        # Buscar el punto en el dominio
        dot_pos = domain.find(".")

        # Verificar que exista un punto en el dominio
        if dot_pos == -1:
            print("Invalid email: domain must contain a dot, e.g. 'gmail.com'.")
        else:
            # Parte del dominio antes del punto
            domain_name = domain[:dot_pos]
            # Extensión (parte después del punto)
            extension = domain[dot_pos + 1 : ]

            # Verificar que haya nombre de dominio y extensión
            if domain_name == "":
                print("Invalid email: missing domain name before the dot.")
            elif extension == "":
                print("Invalid email: missing extension after the dot.")
            else:
                print("Email has a  valid format.")
'''
#Tabla de casos de prueba
'''
Case   | Email               | Result
--------------------------------------------------
Normal | user@gmail.com      | Valid email
Edge   | user@domain         | Invalid: domain must contain a dot
Error  | usergmail.com       | Invalid: must contain exactly one '@'
'''
# Problem 3: Palindrome checker (ignoring spaces and case)

'''
Descripción:
Determina si una frase es un palíndromo, es decir, se lee igual de izquierda
a derecha y de derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.
'''
'''
phrase= input('enter a phrase:')
# Limpiar espacios y convertir a minúsculas
phrase=phrase.replace(' ','').lower().strip()
print('your phrase is:', phrase)
if len(phrase) < 3:
    print('error: invalid length')
else:
    # Verificar si es palíndromo
    if phrase == phrase[::-1]: #los :: indican que se tome toda la cadena de inicio a fin y el -1 indica que se lea al revés
        print('your phrose is palíndromo')
    else:
        print('your phrose is not a palindromo ')
'''
##tabla de casos de prueba
'''
Case   | Input      | Cleaned    | Result
--------------------------------------------------
Normal | Ana        | ana        | palindrome
error  | ab         | ab         | error: invalid length
edge   | Hello      | hello      | not palindrome


'''
#Problem 4: Sentence word stats (lengths and first/last word)
'''
Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).
'''   
'''
sentence=input('enter your sentence:')
sentence=sentence.strip()

if sentence == ' ':
    print('error: it cnnot be empty')
else:
    words=sentence.split()
    print('totatl words:', len(words))
    print('your first word is:', words[0])
    print('your last word is:', words[-1])
    sorted_words = sorted(words, key=len) #key indica que se ordene por longitd
    shortest = sorted_words[0]
    longest = sorted_words[-1]

    print('your shortest word:', shortest)
    print('your longest word:', longest)
'''
##tabla de casos de prueba
'''
Case       | Total Words  | First      | Last       | Shortest   | Longest    | Error
--------------------------------------------------------------------------------
Normal     | 4            | hello      | python     | from       | python     | 
Edge       | 1            | hello      | hello      | hello      | hello      | 
Error      | -            | -          | -          | -          | -          | cannot be empty
'''

#Problem 5: Password strength classifier (weak, medium, strong)
'''
Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas 
(puedes afinarlas, pero documéntalas en los comentarios).
'''
'''
simple_passwords = ('password', '123456', 'qwerty', 'abc123', '111111')
special_symbols = "!@#$%&*?"

password = input("Enter your password: ").strip()

if len(password) == 0:
    print("Error: Password cannot be empty.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    
    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c in special_symbols:
            has_symbol = True
    
    if len(password) < 8 or password in simple_passwords or (has_lower and not has_upper and not has_digit and not has_symbol):
        print("Password strength: WEAK")
    elif len(password) >= 8 and ((has_lower + has_upper + has_digit + has_symbol) < 4):
        print("Password strength: MEDIUM")
    else:
        print("Password strength: STRONG")

#tabla de casos de prueba
+--------+------------+----------------------------------------------------+------------------------------------------+
| Tipo   | Entrada    | Descripción                                        | Salida esperada                           |
+--------+------------+----------------------------------------------------+------------------------------------------+
| Normal | Abc123$%   | Contraseña fuerte con mayúscula, minúscula, número y símbolo | Password strength: STRONG               |
| Borde  | password   | Contraseña simple incluida en simple_passwords    | Password strength: WEAK                  |
| Error  |            | Entrada vacía                                     | Error: Password cannot be empty.        |
+--------+------------+----------------------------------------------------+------------------------------------------+
'''

#Problem 6: Product label formatter (fixed length with padding or truncation)

'''
Descripción:
Genera una etiqueta para un producto en una sola línea con un formato fijo de 30 caracteres.
'''
'''
# Get user input and remove leading/trailing spaces
product_name = input("Enter product name: ").strip()

# Get product price input
price_value = input("Enter product price: ").strip()

# Validate that the product name is not empty
if not product_name:
    print("Error: Product name cannot be empty.")
else:
    try:
        # Convert price to float and take absolute value (to handle negative numbers)
        price = abs(float(price_value)) #float is so you know that it can hold decimal values and abs is to avoid negative prices
        
        # Create the label string
        label = f"Product: {product_name} | Price: ${price}"
        
        # Adjust the label to exactly 30 characters
        if len(label) > 30:
            label = label[:30]       # Trim if longer
        else:
            label = label.ljust(30)  # Pad with spaces if shorter #ljust adds spaces to the right until it reaches the specified length
        
        # Print the label with quotes to show spaces clearly
        print(f'"{label}"')
        
    except ValueError:
        # Handle errors if the price is not a number
        print("Error: Price must be a number.")

##test case table
+--------+----------------------+--------+----------------------------------------------+------------------------------------------+
| Type   | Product              | Price  | Description                                  | Expected Output (30 chars)               |
+--------+----------------------+--------+----------------------------------------------+------------------------------------------+
| Normal | Apple                | 2.5    | Normal product name, positive price         | Product: Apple | Price: $2.5     |
| Border | ExtraLongProductName | 12.99  | Long name exceeding 30 characters           | Product: ExtraLongProductName | Pr       |
| Error  |                      | 5      | Empty product name                           | Error: Product name cannot be empty.     |
+--------+----------------------+--------+----------------------------------------------+------------------------------------------+
'''