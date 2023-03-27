# # Caminata Python 
# 
# 0. Características de Python.
# 1. Tipos de Datos.
# 2. Operadores Basicos.
# 3. Ejecución Condicional. Mención a Loops e Iteraciones. 
# 4. Funciones.
# 5. Objetos.
# 6. Estructura de Datos. Listas, Diccionarios y Tuplas.
# 7. Lo demás es seguir practicando.

# ### Características de Python como lenguaje:
# #### Es de propósito general => Puede ser usado para muchos campos, siendo idóneo para el análisis de datos
# #### Es un lenguaje interpretado => Esta escrito en C, siendo un interfaz práctico de este lenguaje
# #### Es interpretativo => nos permite probar nuestro código linea por linea sin necesidad de compilar cada cambio
# #### Python es un lenguaje de alto nivel ==> implica un nivel de abstracción que nosotros 
# #### escribimos en un nivel que entendemos y no tan bajo como hablar en binario a la maquina
# #### Es un Lenguaje Orientado a Objetos ==> cada variable en Python es un objeto y como tal 
# #### es una estructura de datos, con la que podemos utilizar sus funciones o agregar nuevas
# 

# In[8]:


# esto es un comentario, una anotación que sirve a futuro para aclarar aglo en el código error a ver si leen.

# tipos de datos de Python

"texto", 2, 3.14


# #### Sí le damos los datos así a Python, el prompt simplemente por defecto los va a imprimir
# #### y tales datos no quedan asignados bajo una variable cuyo nombre utilizaremos para usarlos

# In[9]:


'''Esto tambien es un comentario, 
multilinea
para marcar una zona que el lenguaje va a ignorar

Ahora creamos nombres y guardamos los datos de las variables'''
texto = "this is a string"
numero = 2
numero_pi = 3.141592


# # Preguntamos que tipo de Dato son con el keyword "type"

# In[7]:


type(texto),type(numero),type(numero_pi)


# # Los imprimimos con "print"

# In[10]:


print(texto,numero,numero_pi)


# #### Pasamos las Variables a una [lista] y la iteeramos con un for loop
# #### para que haga una serie de acciones sobre algo que le pedimos trabajar
# #### en este caso preguntarle la variable dentro de la lista, imprimirla y ver sus builtin functions

# In[4]:


lista = [texto,numero,numero_pi]

for i in range(len(lista)):
    print("La variable de la lista es ",lista[i], "\ny sus builtin functions son", dir(lista[i]))


# # Operadores Basicos
# 
# # Creamos variables a y b iguales a 2 y 4
# 
# ##### a, b = 2, 4
# ##### Suma           => a +  b
# ##### Resta          => a -  b
# ##### Multiplicar    => a *  b
# ##### División       => a /  b 
# ##### Modulo         => a % b
# ##### Exponencial    => a ** b
# ##### Raiz Cuadrada  => a ** 1/b  # *si, asi de facil, es matematica*
# 
# ###### -------------------------------------------------------------------
# ###### -------------------------------------------------------------------
# 
# # Operadores Lógicos. Usados para comparar datos 
# # la respuesta sera booleana (verdadero o falso)
# ##### Igualdad, a == b, *sí a es igual a b nos va a devolver un True, sino un False*
# ##### Distinto, a != b,
# ##### Mayor, a > b
# ##### Menor, a < b
# ##### Mayor igual, a >= b
# ##### Menor igual, a <= b
# 

# # Ejecución Condicional

# In[12]:


'''Vamos a ejecutar una secuencia del rango de 0 al 9
creamos condiciones, (if) como primaria, (elif) como secundaria, y else para los demas casos'''

for i in range(10):
    if i < 3:
        print('El valor de i menor a 3 y es: ', i) # comillas simples
    elif i >=3 and i < 8:
        print("i esta entre el rango de 3 y 8") # notar print doble comillas
    else:
        print(f"{i} al cuadrado es {i**2}") #uso de print.format, {entre} va el nombre de variable a tratar
        


# # Funciones
# ### nos permite encapsular un bloque de codigo, que realizara cada vez que lo utilicemos
# ### y nos devolvera lo que le pedimos al final, con la palabra clave "return"
# ### Nos permite reutilizar nuestro codigo sin repetirnos

# In[15]:


# Funcion de Fibonacci

def fibonnaci(n):
    '''Documentamos que hace la función. Ejecución de la secuencia de Fibonacci'''
    # Chequeamos que el número sea positivo
    a,b = 0,1
    if n < 0:
        return "No hay Fibonacci de números negativos. Intenta de nuevo"
    elif n == 1:
        return 1
    else:
        for i in range(1,n): # Secuencia Fibonacci
            c = a + b
            a = b
            b = c   
        return b


# In[16]:


# lo usamos

fibonnaci(9)


# In[18]:


# Reutilizamos
fibonnaci(-1), fibonnaci(1), fibonnaci(30)


# In[19]:


fibonnaci(10)


# # Estructuras de Datos
# 
# # [Lists], {Dictionaries} y (tuples)
# 
# 

# # Nos permiten almacenar información de distintas formas
# 
# 
