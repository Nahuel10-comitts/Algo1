"""Ejercicio de Stock:
Se tiene cargado en memoria un diccionario llamado Stcok con clave Producto y valores cantidad
y precio. Se pide calcular el valor total del inventario"""

# disdesc = {}
# descripciones = [(1, "martillo"),(2, "tornillo"),(5, "mechas")]
#  stock = {1 : [2, 300],
#          2 : [5000, 3],
#          5 : [60, 400]}
# for cod,desc in descripciones:
#     disdesc[cod] = desc
#     valor_inventario = 0
# for codigo in stock:
#     valor_prod = stock[codigo][0] * stock[codigo][1]
#     valor_inventario += valor_prod
#     print("El valor total del producto", disdesc[codigo], "es", valor_prod)
# 
# print("El valor total del inventario es", valor_inventario)    
    
stock = {1 : [2, 300],
         2 : [5000, 3],
         5 : [60, 400]}
valor_inventario = 0
for codigo in stock:
    valor_inventario += stock[codigo][0] * stock[codigo][1]
    print("El valor del inventario es: ", valor_inventario)