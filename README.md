link repositorio: https://github.com/lidia-veli/DOO_Tarea-1_Ej-Matriz
# Ejercicio 1: Creación de una clase en Python que representa una matriz.
Para este ejercicio, deberás crear una clase que representa una matriz. Las operaciones que esta clase debe permitir son la creación de una matriz a partir de una lista de listas, la impresión de la matriz en una forma legible, y el cálculo de la transpuesta de la matriz. Asegúrate de que cada método tenga una única responsabilidad.

```python
class Matriz:
    def __init__(self, elementos):
        self.elementos = elementos

    def imprimir(self):
        for fila in self.elementos:
            print(fila)

    def transpuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
```

Este código define una clase Matriz con tres métodos. El método __init__ crea una nueva matriz a partir de una lista de listas. El método imprimir imprime la matriz en una forma legible. El método transpuesta crea una nueva matriz que es la transpuesta de la matriz original.

Un buen ejemplo para este ejercicio podría ser la creación de una matriz 2x2, su impresión y la impresión de su transpuesta. Aquí tienes un ejemplo de cómo usar la clase Matriz para hacer esto:

```python
m = Matriz([[1, 2], [3, 4]])
m.imprimir()
print()
m_transpuesta = m.transpuesta()
m_transpuesta.imprimir()
```
Esto debería dar como resultado:
```
[1, 2]
[3, 4]

[1, 3]
[2, 4]
```
Se debe evaluar la implementación correcta de la responsabilidad única (cada método hace una sola cosa), la claridad del código y la correcta utilización de las características de Python.
