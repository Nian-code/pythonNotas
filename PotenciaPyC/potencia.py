LIMITE    = 1000000
potencia  = 2
exponente = 0
resultado = 2 ** 0

while resultado < LIMITE:
        print("Potencia de {} elevado a {} es {}\n".format(potencia, exponente, resultado))
        exponente+=1
        resultado = pow( potencia, exponente)

        

        
