#Implementa una solución utilizando estructuras de funciones.
#Define funciones para la entrada de datos diarios (temperaturas) y el cálculo del promedio semanal.
#Organiza el código de manera lógica y funcional utilizando la programación tradicional.

#Función para ingresar las temperaturas diarias de la semana.
def ingresar_temperaturas():

    temperaturas = []
    for dia in range(1, 8):
        while True:

                temp = float(input(f"Ingrese la temperatura del día {dia}: "))
                temperaturas.append(temp)
                break

    return temperaturas

#Función para calcular el promedio semanal de las temperaturas.
def calcular_promedio_semanal(temperaturas):

    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

#Función principal que organiza la entrada de datos y el cálculo del promedio.
def promedio():

    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    promedio()