#!/usr/bin/env python
# Lee archivo de texto plano con extension .hxc 
import os
import sys
from plugin_base import BasePlugin

class leerHxC(BasePlugin): # Creo clase que hereda lo importado
    plugin_type = BasePlugin.EXPORT_PLUGIN
    plugin_author = "overload" 
    plugin_version = 1 
    directorio_retorno = os.getcwd()
    #Defino atributos
	
    def __init__(self): #Funcion __init__
        self.ruta = raw_input('Directorio donde se esta el archivo-> ')# Direccion de la ruta
        self.ir_ruta = os.chdir(self.ruta)# Voy a la ruta definida previamente
        self.archivo = raw_input('Archivo-> ')# Introducen el nombre del archivo
        self.op = open(self.archivo, 'r')# Leo el archivo indicado arriba
        self.rea = self.op.read()# Imprimo por pantalla lo leido (aunque supongo que siendo con interfaz se utilizara otra salida)
        print self.rea
        os.chdir(directorio_retorno)#Vuelvo al directorio donde esta alojado HxCadena

def get_plugin():
    return leerHxC() # Devuelve la clase leerHxC()
		
if __name__ == '__main__':
    mostrar2 = get_plugin() # Le asigno una variable a la funcion
    mostrar2.__init__() # Llamo al metodo __init__

	
