#Actividad 1 17/09/2026
##Punto 1: Ejercicio número 4
class Edades:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan
        self.edad_alberto = self.calcular_edad_alberto()
        self.edad_ana = self.calcular_edad_ana()
        self.edad_mama = self.calcular_edad_mama()
    def calcular_edad_alberto(self):
        return self.edad_juan * (2/3)
    def calcular_edad_ana(self):
        return self.edad_juan * (4/3)
    def calcular_edad_mama(self):
        return self.edad_juan + self.edad_alberto + self.edad_ana
    def mostrar_edades(self):
        print(f"La edad de Juan es: {self.edad_juan}")
        print(f"La edad de Ana es: {self.edad_ana:.2f}")
        print(f"La edad de Alberto es: {self.edad_alberto:.2f}")
        print(f"La edad de la Mama es: {self.edad_mama:.2f}")
edad_juan = float(input("Ingrese la edad de Juan: "))
familia = Edades(edad_juan)
familia.mostrar_edades()

##Punto 2: Ejercicio número 5
import math
class PruebaDeEscritorio:
    def __init__(self, x_inicial=20, y_inicial=40):
        self.x = x_inicial
        self.y = y_inicial
        self.suma = 0
        self.resultado = self.ejecutar()
    def ejecutar(self):
        self.suma += self.x
        self.x += math.pow(self.y, 2)
        self.suma += (self.x / self.y)
        return self.suma
    def mostrar_resultado(self):
        print(f"El valor de la suma es: {self.resultado}")
prueba = PruebaDeEscritorio()
prueba.mostrar_resultado()

##Punto 3: Ejercicio número 12
class Salario:
    def __init__(self, horas, valhora, porcentaje_retencion=0.125):
        self.horas = horas
        self.valhora = valhora
        self.porcentaje_retencion = porcentaje_retencion
        self.salario_bruto = self.calcular_salario_bruto()
        self.retencion = self.calcular_retencion()
        self.salario_neto = self.calcular_salario_neto()
    def calcular_salario_bruto(self):
        return float(self.horas * self.valhora)
    def calcular_retencion(self):
        return self.salario_bruto * self.porcentaje_retencion
    def calcular_salario_neto(self):
        return self.salario_bruto - self.retencion
    def mostrar_resultados(self):
        print(f"El salario bruto es: {self.salario_bruto}")
        print(f"El valor de retención es: {self.retencion}")
        print(f"El salario neto es: {self.salario_neto}")
empleado = Salario(48, 5000)
empleado.mostrar_resultados()

##Punto 4: Ejercicio número 14
import math
class Numero:
  def __init__(self, numero):
    self.numero = numero
    self.cuadrado = self.calcular_cuadrado()
    self.cubo = self.calcular_cubo()
  def calcular_cuadrado(self):
    return math.pow(self.numero, 2)
  def calcular_cubo(self):
    return math.pow(self.numero, 3)
  def mostrar_resultados(self):
    print(f"El número ingresado es: {self.numero}")
    print(f"El cuadrado del número es: {self.cuadrado}")
    print(f"El cubo del número es: {self.cubo}")
num1 = float(input("Ingrese un número: "))
num1 = Numero(num1)
num1.mostrar_resultados()

##Punto 5: Ejercicio número 17
import math
class Circulo:
  def __init__(self, radio):
    self.radio = radio
    self.area = self.calcular_area()
    self.perimetro = self.calcular_perimetro()
  def calcular_area(self):
    return math.pi * math.pow(self.radio, 2)
  def calcular_perimetro(self):
    return 2 * math.pi * self.radio
  def mostrar_resultados(self):
    print(f"El área del círculo es: {self.area}")
    print(f"El perímetro del círculo es: {self.perimetro}")
radio = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio)
circulo.mostrar_resultados()
