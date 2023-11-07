numero1 = float(input("Digite um número: "))
número2 = float(input("Digite outro número: "))
número3 = float(input("Digite mais um número: "))
if numero1 > numero2 or numero1 >   numero3: 
    print(f"{número1} foi o maior número digitado.")
elif numero2 > numero1 or numero2 >   numero3: 
    print(f"{número2} foi o maior número digitado.")
else:
    print(f"{número3} foi o maior número digitado.")