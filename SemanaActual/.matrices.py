class Matrix():
  """
  Descripcion del TP transcribiendo las consignas a 
  pseudo codigo
  Configurar una matriz
  indicador cantidad de filas rows
  indicador cantidad de columnas columns 
  CURSOR 
  
  by_row ubicacion fila
  by_column ubicacion columna
  
  instancia __init__(self,lista,row,column,by_row=0)
  setear by_column =  0 
  DONE
  field_oculto CURSOR variable que va a interactuar posicion
      self.row = int
      self.column = int 
      {"row":row,"column":column}
  DONE
  funciones 
  get_position(self,j=self.row,k=self.column)
  setea ubicacion
  DONE
  get_coordinates(self,m=print([self.row,self.column]))
  la imprime
  DONE CON PRINT()
  # switch intercambio de posicion fila columna, reasigno valores
  switch(get_position(self,j=self.column,k=self.row))
  ESTO AL FINAL ES AL PEDO EL BOOLEANO NO TIENE SENTIDO DE ESTAR AHI
  # imprimo contenido fila en que estoy ubicado
  get_row(self, print(self.row))
  LISTO
  # imprimo contenido de la columna en que estoy ubicado
  get_column(self, print(self.column))
  LISTO
  # borrar fila columna seleccionada
  del_row(self,del(self.row)) | del_column(self,del(self.column))
  LISTO
  # swap repetimos el switch intercambio orden filas y columnas
  swap(get_position(self,j=self.column,k=self.row))
  ESTO ES LO MISMO QUE EL TRANSPOSE
  # scale multiplicar los valores de la fila o columna elegida
  scale(self,factor:int a multiplicar,j,k)
  
  # Transpose transponer la matriz
  transpone(self,self.rows=self.columns,self.columns=self.rows)
  LISTO CON SWAP
  # Flip no te entendi reflejar espectacularmente
  print de acorde la posicion copia simetrica
  
  # det calcular la determinante de la matriz, en caso de ser cuadrada 
  # len(self.rows) == len(self.columns)
  det(self)
  if len(self.rows) != len(self.columns):
      print("No puede calcularse determinante de matriz no cuadrada")
  else:
  
  
  # suma, resta, producto a derecha, producto izquierda, potenciacion escalar 
  add/substraction/right_product/left_product/pow(self,B)
  B no se que quisiste decir 
  """


    def __init__(self,lista):
        """matriz[row][column]"""
        self.lista = lista
        self.row = 0
        self.column = 0
        self.len_row = len(self.lista)
        self.len_column = len(self.lista[0])
        # punto de partida del indicador de posicion [0][0]
        self.cursor = {"position": [self.row,self.column],
                       "value": lista[self.row][self.column],
                       "row": self.lista[0],
                       "column": [i[0] for i in self.lista]}
        
    def print(self):
        lista = self.lista 
        cursor = self.cursor
        len_row, len_column = self.len_row, self.len_column
        print(f"La Matriz es {len_row} x {len_column}\n")
        print(*lista,sep='\n')
        print('\n\nCursor Data')
        for key, value in cursor.items():
            print(key,':=>\t',value)
    
    def get_position(self,row,column):
        """Funcion para setear una ubicacion 
        en caso de especificar solo row o column
        afectara la variable mencionada
        sin alterar la no mencionada"""
        self.row = row
        self.column = column
        # tengo que actualizar el cursor
        self.cursor = {"position": [self.row,self.column],
                       "value": lista[self.row][self.column],
                       "row": self.lista[0],
                       "column": [i[0] for i in self.lista]}
        # si, puedo llamar a otra funcion y compruebo si ejecuto los cambios
        self.print()
    
    def get_row(self):
        """Imprimo la lista ubicada"""
        cursor = self.cursor
        print(cursor['row'])
        self.print()
    
    def get_colum(self):
        """Imprimo la lista ubicada"""
        cursor = self.cursor
        print(cursor['column'])
        self.print()
        
    def del_row(self,row):
        """Borrar Fila"""
        del self.lista[0]
        self.print()
        
    def del_column(self,column):
        """Borrar Fila"""
        column = self.column
        lista = self.lista 
        for i in range(len(lista)):
            del lista[i][column]
        
        self.print()
            
    def swap(self):
        """Funcion para intercambiar los valores del cursor"""
        self.row, self.column = self.column, self.row
        # actualizo el cursor
        self.cursor = {"position": [self.row,self.column],
                       "value": lista[self.row][self.column],
                       "row": self.lista[0],
                       "column": [i[0] for i in self.lista]}
        self.print()
        
    def transpose(self):
        """Transpose matrix"""
        lista = self.lista 
        self.lista = [[i[j] for i in self.lista] for j in range(len(lista))]
        # si, puedo llamar a una otra funcion dentro del mismo objeto
        self.swap()
        self.print()
        
    def add_substract(self,value):
        lista = self.lista 
        for i in range(len(lista)):
            lista[i] = [j + value for j in lista[i]]
        
        self.print()


lista = [[9, 8, 10, 5], [8, 5, 7, 4],[ 6, 6, 7, 6],[3, 10, 4, 10]]

matriz = Matrix(lista)
        
