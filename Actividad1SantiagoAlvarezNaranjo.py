#Actividad 1 17/09/2026
##Punto 1: Ejercicio número 4
class edades:
  def EdAlberto(EdJuan):
    return EdJuan * (2/3)
  def EdAna(EdJuan):
    return EdJuan * (4/3)
  def EdMama(EdJuan, EdAlberto, EdAna):
    return EdJuan + EdAlberto + EdAna
EdJuan = float(input("Ingrese la edad de Juan: "))
EdAlberto = edades.EdAlberto(EdJuan)
EdAna = edades.EdAna(EdJuan)
EdMama = edades.EdMama(EdJuan, EdAlberto, EdAna)
print(f"La edad de Juan es: {EdJuan}")
print(f"La edad de Ana es: {EdAna: .2f}")
print(f"La edad de Alberto es: {EdAlberto: .2f}")
print(f"La edad de la Mama es: {EdMama: .2f}")

##Punto 2: Ejercicio número 5
import math
class PruebaDeEscritorio:
  def ejercicio():
    suma = 0
    x = 20
    suma += x
    y = 40
    x += math.pow(y, 2)
    suma += (x/y)
    return suma
suma = PruebaDeEscritorio.ejercicio()
print(f"El valor de la suma es: {suma}")

##Punto 3: Ejercicio número 12
class Salario:
  def InfEmpleado():
    horas = 48
    valhora = 5000
    prf = 0.125
    salariob = float(horas * valhora)
    retf = salariob * prf
    salarion = salariob - retf
    return salariob, retf, salarion
salariob, retf, salarion = Salario.InfEmpleado()
print(f"El salario bruto es: {salariob}")
print(f"El valor de retención es: {retf}")
print(f"El salario neto es: {salarion}")

##Punto 4: Ejercicio número 14
import math
class Numero:
  def cuadrado(numero):
    return math.pow(numero, 2)
  def cubo(numero):
    return math.pow(numero, 3)
numero = float(input("Ingrese un número: "))
cuadrado = Numero.cuadrado(numero)
cubo = Numero.cubo(numero)
print(f"El cuadrado del número ingresado es: {cuadrado}")
print(f"El cubo del número ingresado es: {cubo}")

##Punto 5: Ejercicio número 17
import math
class Circulo():
  def area(radio):
    return math.pi * math.pow(radio, 2)
  def perimetro(radio):
    return 2 * math.pi * radio
radio = float(input("Ingrese el radio del círculo: "))
area = Circulo.area(radio)
perimetro = Circulo.perimetro(radio)
print(f"El área del círculo es: {area: .3f}")
print(f"El perímetro del círculo es: {perimetro: .3f}")