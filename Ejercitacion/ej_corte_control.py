""" Corte de control: DOS CORTES """
"""
    * El formato del archivo de ventas es:
    * CSV: fecha, vendedor, monto
    * Ordenado de menor a mayor por fecha y luego por vendedor
    *
    * Primer corte (mas interno) por vendedor
    * Segundo corte (mas externo) por dia
"""
MAX_DIA = "9999-99-99"
MAX_REG = MAX_DIA + ",xxx,0"

def leer_archivo(archivo):
    linea = archivo.readline()

    if (not (linea)):
        linea = MAX_REG

    return linea.rstrip("\n").split(",")

def dia_vendedor_valor(registro):
    valor = int(registro[2])
    return registro[0], registro[1], valor

def imprimir(leyenda, dato, separador = False):
    print(leyenda, dato)

    if (separador):
        guion = "-" * 55
        print(guion, "\n")

def total_vendedor(registro, archivo):
    dia, vendedor, valor = dia_vendedor_valor(registro)
    dia_actual, vendedor_actual = dia, vendedor
    acum_vendedor = 0

    while (vendedor == vendedor_actual and dia == dia_actual and dia < MAX_DIA):
        acum_vendedor += valor
        registro = leer_archivo(archivo)
        dia, vendedor, valor = dia_vendedor_valor(registro)

    return acum_vendedor, vendedor_actual, registro

def total_dia(registro, archivo):
    dia, vendedor, valor = dia_vendedor_valor(registro)
    dia_actual, vendedor_actual = dia, vendedor
    acum_dia = 0

    while (dia == dia_actual and dia < MAX_DIA):
        acum_vendedor, vendedor_procesado, registro = total_vendedor(registro, archivo)
        leyenda = "--- Acumulado por vendedor: " + vendedor_procesado + "-$"
        imprimir(leyenda, acum_vendedor)
        acum_dia += acum_vendedor
        dia = registro[0]

    return acum_dia, registro

def corte_de_control(archivo):
    registro = leer_archivo(archivo)
    total_acum = 0

    while (registro[0] != MAX_DIA):
        imprimir("\nTotal del dia: ", registro[0])
        acum_dia, registro = total_dia(registro, archivo)
        total_acum += acum_dia
        imprimir("Acumulado por dia: ", acum_dia, True)

    imprimir("\n---- Total acumulado: ", total_acum)


def main():
    with open('ventas.txt') as archivo:
        corte_de_control(archivo)
main()