#Actividad 2: valor 20%
## Punto 1: Ejercicio 2.1 página 63 --------------------------------------------------------------------------------------------- 1
class Persona:
  def __init__(self, nombre, apellido, documento, nacimiento, pais, genero):
    self.nombre = nombre
    self.apellido = apellido
    self.documento = documento
    self.nacimiento = nacimiento
    self.pais = pais
    self.genero = genero
  def mostrar_datos(self):
    print(f"Nombre: {self.nombre}")
    print(f"Apellido: {self.apellido}")
    print(f"Documento: {self.documento}")
    print(f"Nacimiento: {self.nacimiento}")
    print(f"País: {self.pais}")
    print(f"Género: {self.genero}")
persona1 = Persona("Santiago", "Alvarez", "1023633994", 2008, "Colombia", "H")
persona2 = Persona("Sara", "Vásquez", "1023040708", 2008, "Alemania", "M")
print("--- Datos de la Persona 1 ---")
persona1.mostrar_datos()
print("--- Datos de la Persona 2 ---")
persona2.mostrar_datos()

print("\n" + "="*40 + "\n")

## Punto 2: Ejercicio 2.2 página 66 ------------------------------------------------------------------------------------------------ 2
from enum import Enum
class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"
class Planeta:
    def __init__(self, nombre=None, satelites=0, masa=0.0, volumen=0.0, diametro=0, 
                 distancia_sol=0, tipo=None, observable=False, periodo_orbital=0.0, periodo_rotacion=0.0):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.observable = observable
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion
    def atributos_planeta(self):
        print(f"Nombre: {self.nombre}")
        print(f"Satélites: {self.satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diámetro: {self.diametro} km")
        print(f"Distancia al Sol: {self.distancia_sol} millones de km")
        print(f"Tipo: {self.tipo.value if self.tipo else None}")
        print(f"Observable a simple vista: {self.observable}")
        print(f"Periodo Orbital: {self.periodo_orbital} años")
        print(f"Periodo de Rotación: {self.periodo_rotacion} días")
    def calcular_densidad(self):
        if self.volumen == 0:
            return 0.0
        densidad = self.masa / self.volumen
        print(f"La densidad de {self.nombre} es: {densidad} kg/km³")
        return densidad
    def es_planeta_exterior(self):
        limite_exterior_millones = 3.4 * 149.597870
        if self.distancia_sol > limite_exterior_millones:
            print(f"El planeta {self.nombre} ES un planeta exterior.")
            return True
        else:
            print(f"El planeta {self.nombre} NO es un planeta exterior.")
            return False
planeta1 = Planeta(
    nombre="Kamikase",
    satelites=23,
    masa=5.97e24,
    volumen=1.08e12,
    diametro=12742,
    distancia_sol=600,
    tipo=TipoPlaneta.GASEOSO,
    observable=True,
    periodo_orbital=12.5,
    periodo_rotacion=0.9
)
planeta1.atributos_planeta()
planeta1.calcular_densidad()
planeta1.es_planeta_exterior()
print("---" * 30)
planeta2 = Planeta(
    nombre="Renacuajo",
    satelites=2,
    masa=2.0e12,
    volumen=1232898.0,
    diametro=140,
    distancia_sol=150,
    tipo=TipoPlaneta.TERRESTRE,
    observable=False,
    periodo_orbital=1.0,
    periodo_rotacion=24.3
)
planeta2.atributos_planeta()
planeta2.calcular_densidad()
planeta2.es_planeta_exterior()

print("="*30)

##Punto 3: Ejercicio 2.3 página 66 ------------------------------------------------------------------------------------------------- 3
from enum import Enum
class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"
class TipoAutomovil(Enum):
    CARRO_CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"
class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"
class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
        numero_puertas, cantidad_asientos, velocidad_maxima, color, velocidad_actual=0, es_automatico=False):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual
        self.es_automatico = es_automatico
        self.multas = 0
        self.valor_multa = 150000
    def set_velocidad_actual(self, velocidad_actual):
        if velocidad_actual < 0:
            print("La velocidad no puede ser negativa.")
        elif velocidad_actual > self.velocidad_maxima:
            print("No se puede superar la velocidad máxima permitida.")
        else:
            self.velocidad_actual = velocidad_actual
    def acelerar(self, incremento):
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            print(
                f"¡Alerta! Intentó superar la velocidad máxima permitida ({self.velocidad_maxima} km/h)."
            )
            self.multas += 1
            print(
                f"Se ha generado una multa. Total de multas acumuladas: {self.multas}"
            )
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual += incremento
    def desacelerar(self, decremento):
        if self.velocidad_actual - decremento < 0:
            print(
                "No es posible desacelerar a una velocidad negativa. El vehículo se detuvo."
            )
            self.velocidad_actual = 0
        else:
            self.velocidad_actual -= decremento
    def frenar(self):
        self.velocidad_actual = 0
    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            print(
                "El vehículo está detenido. No se puede calcular el tiempo estimado de llegada."
            )
            return None
        return distancia / self.velocidad_actual
    def tiene_multas(self):
        return self.multas > 0
    def valor_total_multas(self):
        return self.multas * self.valor_multa
    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(
            f"Tipo de Combustible: {self.tipo_combustible.value if self.tipo_combustible else None}"
        )
        print(
            f"Tipo de Automóvil: {self.tipo_automovil.value if self.tipo_automovil else None}"
        )
        print(f"Número de Puertas: {self.numero_puertas}")
        print(f"Cantidad de Asientos: {self.cantidad_asientos}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.value if self.color else None}")
        print(f"Velocidad Actual: {self.velocidad_actual} km/h")
        print(f"Es Automático: {self.es_automatico}")
        print(f"Tiene Multas: {self.tiene_multas()}")
        print(f"Total a pagar en Multas: ${self.valor_total_multas()}")
auto1 = Automovil(
        marca="Toyota",
        modelo=2022,
        motor=2.0,
        tipo_combustible=TipoCombustible.GASOLINA,
        tipo_automovil=TipoAutomovil.COMPACTO,
        numero_puertas=4,
        cantidad_asientos=5,
        velocidad_maxima=180,
        color=Color.ROJO,
        velocidad_actual=0,
        es_automatico=True
        )

print("--- Datos iniciales del Automóvil ---")
auto1.mostrar_datos()
print("\n--- Pruebas de velocidad ---")
auto1.set_velocidad_actual(100)
print(f"Velocidad actual: {auto1.velocidad_actual} km/h")
auto1.acelerar(20)
print(f"Velocidad actual tras acelerar 20 km/h: {auto1.velocidad_actual} km/h")
auto1.desacelerar(50)
print(f"Velocidad actual tras desacelerar 50 km/h: {auto1.velocidad_actual} km/h")
distancia = 250
tiempo = auto1.calcular_tiempo_llegada(distancia)
if tiempo:
    print(f"Tiempo estimado para recorrer {distancia} km: {tiempo:.2f} horas")
print("\n--- Prueba de exceso de velocidad ---")
auto1.acelerar(120)
print(f"Velocidad actual tras el intento: {auto1.velocidad_actual} km/h")
auto1.frenar()
print(f"Velocidad actual tras frenar: {auto1.velocidad_actual} km/h")
print("\n--- Estado final del Automóvil ---")
auto1.mostrar_datos()

##Punto 4: Ejercicio 2.4 página 86.---------------------------------------------------------------------------------------------------- 4
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return math.pi * (self.radio**2)
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado**2
    def calcular_perimetro(self):
        return 4 * self.lado
class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2
    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)
    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()
    def tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura and self.altura == hipotenusa:
            return "Equilátero"
        elif (
            self.base == self.altura
            or self.base == hipotenusa
            or self.altura == hipotenusa
        ):
            return "Isósceles"
        else:
            return "Escaleno"
class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor, lado):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
        self.lado = lado
    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2
    def calcular_perimetro(self):
        return 4 * self.lado
class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2
    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2
figura1 = Circulo(2)
figura2 = Rectangulo(1, 2)
figura3 = Cuadrado(3)
figura4 = TrianguloRectangulo(3, 5)
figura5 = Rombo(8, 6, 5)
figura6 = Trapecio(10, 6, 4, 5, 5)
print("--- Círculo ---")
print(f"Área: {figura1.calcular_area():.2f}")
print(f"Perímetro: {figura1.calcular_perimetro():.2f}")
print("\n--- Rectángulo ---")
print(f"Área: {figura2.calcular_area()}")
print(f"Perímetro: {figura2.calcular_perimetro()}")
print("\n--- Cuadrado ---")
print(f"Área: {figura3.calcular_area()}")
print(f"Perímetro: {figura3.calcular_perimetro()}")
print("\n--- Triángulo Rectángulo ---")
print(f"Área: {figura4.calcular_area()}")
print(f"Hipotenusa: {figura4.calcular_hipotenusa():.2f}")
print(f"Perímetro: {figura4.calcular_perimetro():.2f}")
print(f"Tipo de triángulo: {figura4.tipo_triangulo()}")
print("\n--- Rombo ---")
print(f"Área: {figura5.calcular_area()}")
print(f"Perímetro: {figura5.calcular_perimetro()}")
print("\n--- Trapecio ---")
print(f"Área: {figura6.calcular_area()}")
print(f"Perímetro: {figura6.calcular_perimetro()}")

##Punto 5: Ejercicio 2.5 página 95 -------------------------------------------------------------------------------------------------- 5
from enum import Enum
class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"
class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta, porcentaje_interes=0.0,):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0
        self.porcentaje_interes = porcentaje_interes
    def imprimir_datos(self):
        print(f"Titular: {self.nombres_titular} {self.apellidos_titular}")
        print(f"Número de Cuenta: {self.numero_cuenta}")
        print(
            f"Tipo de Cuenta: {self.tipo_cuenta.value if self.tipo_cuenta else None}"
        )
        print(f"Saldo: ${self.saldo:.2f}")
        print(f"Porcentaje Interés Mensual: {self.porcentaje_interes}%")
    def consultar_saldo(self):
        print(f"El saldo actual de la cuenta es: ${self.saldo:.2f}")
        return self.saldo
    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Se consignaron ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("El valor a consignar debe ser mayor a cero.")
    def retirar(self, valor):
        if valor > self.saldo:
            print("No se puede realizar el retiro. El valor supera el saldo actual.")
        elif valor <= 0:
            print("El valor a retirar debe ser mayor a cero.")
        else:
            self.saldo -= valor
            print(f"Se retiraron ${valor:.2f}. Nuevo saldo: ${self.saldo:.2f}")
    def aplicar_interes_mensual(self):
        interes = self.saldo * (self.porcentaje_interes / 100)
        self.saldo += interes
        print(
            f"Interés aplicado (${interes:.2f}). Nuevo saldo tras interés: ${self.saldo:.2f}"
        )

cuenta1 = CuentaBancaria("Carlos", "Gómez", "1028394857", TipoCuenta.AHORROS, 1.5)
print("--- Datos Iniciales de la Cuenta ---")
cuenta1.imprimir_datos()
print("\n--- Operaciones ---")
cuenta1.consignar(500000)
cuenta1.retirar(100000)
cuenta1.retirar(600000) 
cuenta1.aplicar_interes_mensual()
print("\n--- Estado Final de la Cuenta ---")
cuenta1.imprimir_datos()