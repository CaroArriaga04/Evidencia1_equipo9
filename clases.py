import datetime
import uuid
from tabulate import tabulate

class Nota:
    def __init__(self, cliente):
        self.folio = str(uuid.uuid4())[:5]
        self.fecha = datetime.date.today().strftime("%d/%m/%Y")
        self.cliente = cliente
        self.servicios = []
    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
    def calcular_monto_total(self):
        total = sum(servicio.costo for servicio in self.servicios)
        return total
    
class Servicio:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo

notas = []

def registrar_nota():
    cliente = input("Nombre del cliente: ")
    nota = Nota(cliente)
    while True:
        nombre_servicio = input("Nombre del servicio requerido (f para finalizar)): ")
        if nombre_servicio.lower() == "f":
            break
        costo_servicio = float(input("Costo del servicio: "))
        while costo_servicio <= 0:
            print("El costo debe ser mayor que 0.")
            costo_servicio = float(input("Ingrese el costo del servicio: "))
        servicio = Servicio(nombre_servicio, costo_servicio)
        nota.agregar_servicio(servicio)
    notas.append(nota)
    monto_total = nota.calcular_monto_total()
    print("\n---------------NOTA-------------")
    print(f"Folio: {nota.folio}")
    print(f"Fecha: {nota.fecha}")
    print(f"Cliente: {nota.cliente}")
    print("--------------------------------")
    print("Servicio:")
    for servicio in nota.servicios:
        print(f"- {servicio.nombre}: ${servicio.costo:.2f}")
    print("--------------------------------")
    print(f"Total a pagar: ${monto_total:.2f}")

def consulta_por_periodo():
    while True:
        try:
            fecha_inicial = input("Ingresa la fecha inicial (dd/mm/aaaa): ")
            fecha_final = input("Ingresa la fecha final (dd/mm/aaaa): ")
            fecha_inicial = datetime.datetime.strptime(fecha_inicial, "%d/%m/%Y").date()
            fecha_final = datetime.datetime.strptime(fecha_final, "%d/%m/%Y").date()
        except Exception:
            print("Las fechas ingresadas deben estar en formato dd/mm/aaaa")
        else: 
            notas_por_periodo = [n for n in notas if fecha_inicial <= datetime.datetime.strptime(n.fecha, "%d/%m/%Y").date() <= fecha_final]
            if notas_por_periodo:
                print("\n---------NOTAS POR PERIODO---------")
                informacion = [[n.folio, n.fecha, n.cliente] for n in notas_por_periodo]
                titulos = ["Folio", "Fecha", "Cliente"]
                print(tabulate(informacion, titulos, tablefmt="fancy_grid"))
            else:
                print("No hay notas registradas en el periodo ingresado")
            break

def consulta_por_folio():
    pass

def cancelar_nota():
    pass

def recuperar_nota():
    pass

def main():
    registrar_nota()
    consulta_por_periodo()

if __name__ == "__main__":
    main()