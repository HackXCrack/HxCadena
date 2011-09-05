#coding: utf-8
# Interfaz de ejemplo

class ui(object):
    def __init__(self, argv, plugin_manager):
        self.argv = argv
        self.plugins = plugin_manager

    def run(self):
        seleccion = ''
        proxies = self.plugins.get_list()
        while seleccion != 'q':
            print len(proxies), "proxies"
            muestra_menu() # Se muestra el menú
            seleccion = raw_input(">> ") # Se lee lo que introduce el usuario
            seleccion = seleccion.lower() #

            if seleccion == 'a':
                menu_guardar(self.plugins, proxies)
            elif seleccion == 'b':
                proxies = self.plugins.filter_list(proxies)
            else:
                print "" # Nueva línea

# Opciones del menú
def muestra_menu():
    print "HxCadena"
    print "--------"
    print "a) Guardar la lista de proxies"
    print "b) Filtrar"
    print "q) Salir"

# Menú 'principal'
def menu_guardar(plugin, proxies):
     print "Selecciona formato:"
     print "-------------------"
     print "0 ) salir"

     formatos = plugin.get_formats() # Posibles formatos

     i = 1
     for formato in formatos:
         print i, ")", formato
         i += 1

     sel = -1
     while sel < 0 or sel > len(formatos):
        sel_in = raw_input(">> ")

        try: # Intentamos convertirlo en un entero
            sel = int(sel_in)
        except: # Si no es posible
            print "Por favor, introduce un número"

     if sel == 0: # Si selecciona 0, salir
        return

     formato = formatos[sel - 1] # Formato seleccionado
     nombre  = raw_input("Nombre del archivo: ")

     # Por fin, exportamos el archivo
     plugin.export(formato, nombre, proxies)
