#coding: utf-8

from plugin_base import BasePlugin # Clase base

class PlainExportPlugin(BasePlugin):
    plugin_type = BasePlugin.EXPORT_PLUGIN
    plugin_author = "kenkeiras"
    plugin_version = 0.1
    plugin_export_format = "plano"

    def export_list(self, archivo_salida, lista):
        for proxy in lista:
            archivo_salida.write(' '.join(proxy)+ "\n")

# Devuelve el plugin o None si es una clase de plantilla
def get_plugin():
    return PlainExportPlugin()
