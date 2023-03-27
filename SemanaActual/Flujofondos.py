"""
Revision Codigo en $MAYUSCULA
"""

class FF():
    """ Documentacion que va al __doc__ del objeto
        Poner aqui lo que se quiera explicar en un help.
        Por una cuestion de seguridad, vamos a usar tuplas 
        para garantizar la inmutabilidad del objeto

        $NO HAY DOCUMENTACION DEL OBJETO EN SI Y SU NOMBRE NO ES INTUITIVO
        EN VEZ DE CF USAR 
        Flujo_de_Fondos
        """
    def __init__(self,tupla=tuple()):
        """$NO HAY MENCION DE QUE CONTIENE LA TUPLA Y COMO USAREMOS SUS DATOS"""
         self.flujos=tupla
        
    def van(self,tasa, n=0):
        """ Calculo de valor actual neto recursivo
            Inputs: 
                1 - tasa (posicional) $NO ESPECIFICA TIPO DE VARIABLE
                2 - n posicion en el vector ( default = 0, named argument ). 
                    Sirve para manejar recursivamene las iteraciones 
                    sin alterar la lista del flujo de fondos 
            $NOMBRE DEBERIA SER valor_actual_neto, PRIORIZAR LEGIBILIDAD
            $EXPLICAR EL VAN
            $ARGUMENTOS "TASA" Y "N" NO SE ESPECIFICARON TIPO DE VARIABLE QUE SON
        """
        if len(self.flujos)>0:
            if n==len(self.flujos):
                salida = 0
            else:
                salida = self.flujos[n]+1.0/(1.0+tasa)*self.van(tasa, n=n+1)
        else:
            print('\n',"La tupla de flujo de fondos esta vacia. Se devuelve 0")
            salida = 0
        """$EVITAR IF/ELSE MULTIPLES O NESTING
            REMPLAZAR CON SWITCH FLUJO DE CONTROL DE EJECUCION
            RECURSIVIDAD EN ESTE CASO ES UN PELIGRO SI CUMPLIS
            EL PRINCIPIO KISS KEEP-IT-SIMPLE-S
            SI EL DATO QUE BUSCAS LO PODES GENERAR DENTRO DEL MISMO CACHE
            EVITA USAR RECURSIVIDAD"""
        return salida
    
    def vt(self,tasa,t = 0):
        """$OTRA VEZ NOMBRE FUNCION NO INTUITIVO
            USAR valor_flujo_t"""
        """ Calculo de valor del flujo de fondos a un tiempo t
            Funciona calculando van y luego llevando a tiempo t correspondiente
            Inputs: 
                1 - tasa (posicional)
                2 - t momento de valuacion ( default = 0, named argument ). 
                    
        """
        return self.van(tasa)*(1.0+tasa)**t
    
 
    
    def tir1(self,tmin=0,step=0.1, tol = 1e-07):
        """$NO HAY DOCUMENTACION, NO SE EXPLICA LOS ARGUMENTOS
        NO SE ENTIENDEN SUS NOMBRES Y QUE PROCESO BUSCAN REALIZAR"""
        if(len(list(filter(lambda x:x>0,self.flujos)))*len(list( filter(lambda x:x<0,self.flujos)))>0):
            """$CODIGO OFUSCADO!!!!!!!!!
            ILEGIBLE LO QUE HACE Y PORQUE
            MULTIPLES IF/ELSE Y NO SE DOCUMENTA PASO A PASO"""
            print(tmin,step,self.van(tmin))    # borren chicos esta linea una vez que entiendan como funciona el algoritmo
            if(self.van(tmin)*self.van(tmin+step)>0):
                salida = self.tir1(tmin+step)   
            else:
                if (step<tol):
                    salida =  tmin 
                else:
                    salida = self.tir1(tmin,step/2)
        else:
            print('Los flujos son todos del mismo signo, no se puede encontrar la tir')
            print(self.flujos)    
            salida = None
            
        return salida
    
#%%
if __name__=='__main__':
    
    a = FF((-80,10,10,10,10,10,10,10,10,100))    

    # dos formas de llamar al help    
    print((a.van).__doc__)
    help(a.vt)        
        
    # Busqueda de TIR...
    for x in range(1,20) : print(x, a.van(x/100.0))   
    
    # van a un valor proximo a la tir...
    print('\n',a.van(0.1330055))
    
    # Valor futuro en t a la tir. 
    # Notar que al no ser la tir exacta, 
    # a 25 periodos hacia el futuro, se aleja del 0.
    # Haria falta una funcion para computar la tir.... :) 
    print('\n', a.vt(0.1330055,25))
    
    #calculo de tir
    tir = a.tir1(tmin=0.,step= 0.1)
    
    if tir==None:
        pass
    else:
        print(a.van(tir))
    
    #test caso FF vacio
    a = FF()
    print('\n',a.van(0.0))

    
