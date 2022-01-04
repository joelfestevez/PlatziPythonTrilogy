#Funciones
def conversor(tipo_moneda, valor_dolar):
    pesos = input("¿Cúantos pesos " + tipo_moneda + " tienes?: ")
    pesos = float(pesos)
    dolares1 = pesos/valor_dolar
    dolares1 = round(dolares1,2)
    dolares1 = str(dolares1)
    print("Tienes $"+ dolares1 + " dólares")

menu = """
Bienvenido al conversor de monedas 💰
Presiona el número con la opcion deseada y luego enter

1 - Pesos colombianos a dolares
2 - Pesos mexicanos a dolares
3 - Dolares a pesos colombianos y mexicanos

Elige una opción: """

opcion = float(input(menu))

valor_dolar_mex = 20.14
if opcion == 1:
    conversor("colombianos", 3875)

elif opcion == 2:
    conversor("mexicanos", 20.14)

elif opcion == 3:
    #De Dolares a Mexicanos y Colombianos
    dolares_a = input("¿Cuántos dolares tienes?: ")
    dolares_a = float(dolares_a)
    dolares_convertidos1 = dolares_a*(valor_dolar)
    dolares_convertidos2 = dolares_a*(valor_dolar_mex)
    dolares_convertidos1 = round (dolares_convertidos1,2)
    dolares_convertidos2 = round (dolares_convertidos2,2)
    dolares_convertidos1 = str(dolares_convertidos1)
    dolares_convertidos2 = str(dolares_convertidos2)
    print("Tienes $"+ dolares_convertidos1 + " pesos colombianos y $" + dolares_convertidos2 + " pesos mexicanos")
else:
    print("Ingresa una opciòn correcta por favor.")

