def calculadora():
    resultado = float(input("Ingrese un número: "))
    
    while True:
        operacion = input("Ingrese una operación (+, -, *, /) o '=' para obtener el resultado: ").strip()
        
        if operacion == "=":
            break
        
        if operacion not in ('+', '-', '*', '/'):
            print("Operación no válida. Intente de nuevo.")
            continue
        
        try:
            numero = float(input("Ingrese otro número: "))
        except ValueError:
            print("Número no válido. Intente de nuevo.")
            continue
        
        if operacion == '+':
            resultado += numero
        elif operacion == '-':
            resultado -= numero
        elif operacion == '*':
            resultado *= numero
        elif operacion == '/':
            if numero == 0:
                print("Error: No se puede dividir por cero.")
                continue
            resultado /= numero
        
        print(f"Resultado actual: {resultado}")
    
    print(f"Resultado final: {resultado}")

calculadora()