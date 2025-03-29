import re

def calcular_expresion(expresion):
    try:
        # Tokenizar la expresión manteniendo operadores y números
        tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/]', expresion)
        
        # Primero resolver multiplicaciones y divisiones
        i = 0
        while i < len(tokens):
            if tokens[i] in ('*', '/'):  
                if tokens[i] == '*':
                    resultado = float(tokens[i-1]) * float(tokens[i+1])
                else:
                    if float(tokens[i+1]) == 0:
                        return "Error: No se puede dividir por cero."
                    resultado = float(tokens[i-1]) / float(tokens[i+1])
                
                tokens[i-1:i+2] = [str(resultado)]
                i -= 1  # Retroceder para revalidar el índice tras la modificación
            i += 1
        
        # Luego resolver sumas y restas
        resultado = float(tokens[0])
        i = 1
        while i < len(tokens):
            if tokens[i] == '+':
                resultado += float(tokens[i+1])
            elif tokens[i] == '-':
                resultado -= float(tokens[i+1])
            i += 2
        
        return resultado
    except Exception as e:
        return f"Error en la expresión: {e}"

def calculadora():
    expresion = input("Ingrese un número: ")
    
    while True:
        operacion = input("Ingrese una operación (+, -, *, /) o '=' para obtener el resultado: ").strip()
        
        if operacion == "=":
            break
        
        if operacion not in ('+', '-', '*', '/'):
            print("Operación no válida. Intente de nuevo.")
            continue
        
        numero = input("Ingrese otro número: ")
        
        if not numero.replace('.', '', 1).isdigit():
            print("Número no válido. Intente de nuevo.")
            continue
        
        expresion += f" {operacion} {numero}"
    
    resultado = calcular_expresion(expresion)
    print(f"Resultado final: {resultado}")

calculadora()
