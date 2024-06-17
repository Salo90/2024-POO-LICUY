# Implementa una solución utilizando estructuras de funciones.
# Define funciones para la entrada de datos diarios (temperaturas) y el cálculo del promedio semanal.
# Organiza el código de manera lógica y funcional utilizando la POO.

class Registro_Temperaturas:
    def __init__(self):
        # Atributo del objeto para almacenar las temperaturas
        self.temperaturas = []

    # Método para ingresar las temperaturas diarias de la semana.
    def ingresar_temperaturas(self):

        for dia in range(1, 8):
            while True:

                    temp = float(input(f"Ingrese la temperatura del día {dia}: "))
                    self.temperaturas.append(temp)
                    break

    # Método para calcular el promedio semanal de las temperaturas.
    def calcular_promedio_semanal(self):

        if not self.temperaturas:
            return 0
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio

    # Método para mostrar las temperaturas ingresadas y el promedio semanal.
    def mostrar_resultados(self):
        promedio = self.calcular_promedio_semanal()
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

#Función principal que organiza la entrada de datos y el cálculo del promedio.
def promedio():

    print("Cálculo de promedio de temperaturas semanales.")

    # Creación del objeto registro de la clase RegistroTemperaturas
    registro = Registro_Temperaturas()

    # Uso del objeto registro para ingresar temperaturas
    registro.ingresar_temperaturas()

    # Uso del objeto registro para mostrar resultados
    registro.mostrar_resultados()


if __name__ == "__main__":
    promedio()