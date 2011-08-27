#coding: utf-8
# Gestor de plugins

import sys
import os

plugins_dir = "plugins" # Directorio de plugins

# Gestor de plugins
# reune las funciones de todos los plugins en una interfaz
class PluginManager:
    modulos_exportacion = [] # Exportan listas
    modulos_listado     = [] # Generan listas

    # Prepara el gestor del plugin
    def __init__(self, lista):
        for plugin in lista:
            try: # Intentamos importar el plugin
                modulo = __import__(plugin)
                p = modulo.get_plugin()

            except: # Si algo falló
                print >>sys.stderr, "Error importando plugin", plugin

            else: # Si todo fue bien

                # Si no devuelve un plugin
                if p == None:
                    continue # Se ignora

                # Si es un plugin de exportacion
                elif p.plugin_type == p.EXPORT_PLUGIN:
                    self.modulos_exportacion.append(p)

                # Si es uno de listado
                elif p.plugin_type == p.LIST_PLUGIN:
                    self.modulos_listado.append(p)

    # Genera la lista de proxies
    def get_list(self):
        lista = []
        for modulo in self.modulos_listado:
            lista += modulo.get_list()
        return lista

    # Genera la lista de formatos de exportación
    def get_formats(self):
        lista = []
        for modulo in self.modulos_exportacion:
            lista.append(modulo.plugin_export_format)
        return lista

    # Exporta a un archivo con el formato deseado
    def export(self, formato, nombre_archivo, lista):

        # Busca el módulo de exportación
        modulo = None
        for mod in self.modulos_exportacion:
            # Al encontrarlo
            if formato == mod.plugin_export_format:
                modulo = mod # Guardarlo
                break # Y salir del bucle

        # Si no se encontró, mandar una excepción
        if modulo == None:
            raise Exception('Formato inválido')

        # Se abre el archivo
        archivo_salida = open(nombre_archivo, 'w')
        modulo.export_list(archivo_salida, lista)

# Devuelve el gestor de plugins
def plugins():

    # Comprueba la carpeta de plugins
    lista_de_archivos = os.listdir(plugins_dir)
    lista_de_plugins = []

    # Por cada archivo
    for archivo in lista_de_archivos:
        # Se divide en nombre y extensión
        nombre, extension = archivo.rsplit(".", 1)

        # Si es un .py, se añade a la lista de plugins
        if extension == "py":
           lista_de_plugins.append(nombre)

    # Inicia el gestor con la lista de plugins
    manager = PluginManager(lista_de_plugins)

    # Devuelve el gestor
    return manager
