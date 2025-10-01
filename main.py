from lib import cuadrado
print('Proyecto Figuras')
print(cuadrado.get_identificador())
lado = 4
print(f'El área de un {cuadrado.get_identificador()} de lado {lado} es:'
      f'{cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro(lado)}')

