
from lib import cuadrado, rectangulo, triangulo, circunferencia
base = 4
lado = 4
altura = 2

print('Proyecto Figuras')

print(cuadrado.get_identificador())
print(f'El área de un {cuadrado.get_identificador()} de lado {lado} es:\
      {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}')

print(triangulo.get_identificador())
print(f'El área de un {triangulo.get_identificador()} de base {base}\
      y altura {altura} es: {triangulo.get_area(base, altura)}\
      y el perímetro es {triangulo.get_perimetro(base, base, base)}')

print(rectangulo.get_identificador())
print(f'El área de un {rectangulo.get_identificador()} de base {base}\
      y altura {altura} es: {rectangulo.get_area(base, altura)}\
      y el perímetro es {rectangulo.get_perimetro(base, altura)}')

print('Circunferencia')
print(f'El área de una circunferencia de radio {base}\
      es: {circunferencia.get_area(base)}')