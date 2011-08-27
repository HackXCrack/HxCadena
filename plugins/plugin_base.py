# coding: utf-8
# Clase básica de plugins

class BasePlugin:
    # Posibles tipos de plugin
    TEMPLATE_PLUGIN = 0 # No se usa directamente, es una plantilla
    EXPORT_PLUGIN   = 1 # Sirve para exportar las listas
    LIST_PLUGIN     = 2 # Genera una lista de proxies

    plugin_type = TEMPLATE_PLUGIN # Tipo de plugin
    plugin_author = "" # Autor del plugin
    plugin_version = 1 # Versión del plugin

    # Para los plugins de exportación
    plugin_export_format = ""

    # Función de los plugins que exportan
    def export_list(self, archivo_salida, list):
        raise Exception('Este no es un plugin de exportacion')

    # Función de los plugins que generan una lista
    def get_list(self):
        raise Exception('Este no es un plugin de listado')

# Función que devuelve el objeto de plugin
def get_plugin():
    return None # El plugin no se usará, así que no devuelve nada
