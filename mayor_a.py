import sys
import math

filter_value = int(sys.argv[1])

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

filter_dict = {key:ventas[key] for key in ventas if ventas[key] >= filter_value}
print(filter_dict)

