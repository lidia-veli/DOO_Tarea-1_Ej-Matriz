class Matriz(): # interfaz
    def __init__(self, elementos):
        self.elementos = elementos
    
    def transponer(self):
        pass 

    def imprimir(self):
        pass


class Transpuesta(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)
    
    def transponer(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])
    # usamos una funcion lambda en lugar de un bucle for
    #   para optimizar el tiempo de ejecucion y el espacio de memoria
    # crear una funcion recursiva cuando estemos tratando con grandes cantidades de datos 


class ImprimirMatriz():
    def __init__(self, matriz):
        self.matriz = matriz
    
    def imprimir(self):
        for fila in self.matriz.elementos:
            print(fila)


# hacer clase lanzador para lanzar el main
class Lanzador():
    # crear metodo que llame a la funcion transpuesta y funcion imprimir y lo recoja con un input y un oputput

    def __init__(self):
        self.num_filas = int(input('Ingrese la cantidad de filas: '))
        self.num_columnas = int(input('Ingrese la cantidad de columnas: '))
        self.elementos = []  # la vamos a llenar en crear_matriz()
        self.crear_matriz()
        self.matriz = Matriz(self.elementos)  # ponemos los elementos en forma de obj Matriz
        self.transpuesta = Transpuesta(self.matriz.elementos)  # que la podemos hacer obj Transpuesta
        self.imprimir_matriz = ImprimirMatriz(self.matriz)  # y obj ImprimirMatriz
        

    def crear_matriz(self):
        '''Función que crea una matriz en forma de lista de listas, según los datos ingresados por el usuario'''
        for i in range(self.num_filas):
            fila = []
            for j in range(self.num_columnas):
                fila.append(int(input(f'Ingrese el elemento ({i+1},{j+1}): ')))  # metemos el elemento en la fila
            self.elementos.append(fila)  # y la fila en la lista de elementos de las matriz
    
    def lanzar(self):
        print('La matriz es: ')
        self.imprimir_matriz.imprimir()
        print()
        print('La matriz transpuesta es: ')
        m_trans = self.transpuesta.transponer()  # transponemos la matriz
        imprimir_m_trans = ImprimirMatriz(m_trans)
        imprimir_m_trans.imprimir()  # y la imprimimos


# clase Main que llama a la funcion lanzar
class Main():
    def __init__(self):
        self.lanzador = Lanzador()
        self.lanzador.lanzar()



# CODIGO EJECUTABLE ----------------------------------------------------------------
if __name__ == '__main__':
    Main()
