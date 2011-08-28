#!/usr/bin/env python
#coding: utf-8

import sys
import os

core_dir    = "core"
plugins_dir = "plugins"
ui_dir      = "ui"

main_dir   = os.getcwd()

uis = {'text':'text_interface',
      'gtk':'gtk_ui',
       'ncurses': 'ncurses'
     }
# Función principal
def main():
    # Añadimos los módulos de 'core', 'plugins' y 'ui' a los importables
    sys.path.append(core_dir)
    sys.path.append(plugins_dir)
    sys.path.append(ui_dir)

    # Importamos el módulo plugin, para manejarlos sencillamente
    from plugins import plugins
    plugin_manager = plugins()

    # Iniciamos la ui
    ui = __import__(uis['text'])
    ui.ui(sys.argv, plugin_manager).run()
    #text_interface.init_ui(sys.argv, plugin_manager)

# Si se ejecuta directamente
if __name__=="__main__":
    main()
