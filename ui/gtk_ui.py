import os
import sys
import gtk
#import Plugins

#http://www.pygtk.org/docs/pygtk/class-gtkwindow.html

class ui(gtk.Window):
    def __init__(self,argv, plugin_manager):
        #rc_string = 'gtk-theme-name = "Ambiance"'
        #En linux con gtk-theme-switch2 pueden ver cuales temas existen
        #gtk.rc_parse_string(rc_string)
        #Si no se puede crear/descargar/modificar un tema
        #Y se lo activamos con
        gtk.rc_parse('WoW-Dark/gtk-2.0/gtkrc')
        gtk.Window.__init__(self)

        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title('Algo')
        hbox = gtk.HBox() #http://www.pygtk.org/docs/pygtk/class-gtkhbox.html
        vbox = gtk.VBox() #http://www.pygtk.org/docs/pygtk/class-gtkvbox.html
        #Menus
        menu_bar = gtk.MenuBar()
        file_menu = gtk.Menu()
        #file_menu.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
        close_item = gtk.MenuItem('Cerrar')
        close_item.connect('activate', lambda widget: gtk.main_quit())
        file_menu.append(close_item)
        file_item = gtk.MenuItem('Archivo')
        style = file_item.get_style().copy()
        file_item.set_style(style)
        file_item.set_submenu(file_menu)

        menu_bar.append(file_item)
        #menu_bar.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))

        #Barra de Herramientas (Vertical)
        #http://www.pygtk.org/docs/pygtk/class-gtktoolbar.html
        ToolBar = gtk.Toolbar()
        ToolBar.set_orientation(gtk.ORIENTATION_VERTICAL)
        # gtk.STOCK : http://www.pygtk.org/docs/pygtk/gtk-stock-items.html
        ToolBar.append_element(gtk.TOOLBAR_CHILD_BUTTON, None,
                               "Obtener Lista","Obtiene la lista de proxys",None,
                               gtk.image_new_from_stock(gtk.STOCK_NETWORK,1),
                               self.get_proxy_list,None)
        ToolBar.append_element(gtk.TOOLBAR_CHILD_BUTTON, None,
                               "Verificar","Verifica cuales proxys esta activos",
                               None,gtk.image_new_from_stock(gtk.STOCK_APPLY,1),
                               self.check_proxys_alive,None)
        ToolBar.append_element(gtk.TOOLBAR_CHILD_BUTTON, None,
                               "Recargar","Vuelve a descargar la lista",None,
                               gtk.image_new_from_stock(gtk.STOCK_REFRESH,1),
                               self.get_proxy_list,None)
        ToolBar.append_element(gtk.TOOLBAR_CHILD_BUTTON, None,
                               "Guardar","Guarda la lista",None,
                               gtk.image_new_from_stock(gtk.STOCK_SAVE,1),
                               self.save_proxy_list,None)
        ToolBar.append_element(gtk.TOOLBAR_CHILD_BUTTON, None,
                               "Salir","Sale de la aplicacion",
                               None,gtk.image_new_from_stock(gtk.STOCK_QUIT,1),
                               lambda widget: gtk.main_quit(),None)

        hbox.pack_start(ToolBar)
        #ToolBar.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
        #TextView http://www.pygtk.org/docs/pygtk/class-gtktextview.html
        #TextBuffer http://www.pygtk.org/docs/pygtk/class-gtktextbuffer.html
        #Para colocar la lista de proxys encontrados
        self.TextView = gtk.TextView()
        self.TextView.set_editable(False)
        self.TextView.set_cursor_visible(False)
        self.TextView.set_sensitive(False)
        #Le agregamos la barra de desplazamiento al TextView
        ScrolledWindow = gtk.ScrolledWindow()
        ScrolledWindow.set_size_request(300,400)
        ScrolledWindow.set_policy(gtk.POLICY_NEVER, gtk.POLICY_ALWAYS)
        ScrolledWindow.add(self.TextView)
        hbox.pack_start(ScrolledWindow)
        vbox.pack_start(menu_bar)
        vbox.pack_start(hbox)
        self.add(vbox)

        self.show_all()

    def get_proxy_list(self,widget):
        #plugins = Plugins.find_plugins()
        #print(plugins)
        #proxy_list = []
        #for plugin in plugins:
        #    px = Plugins.load_plugin(plugin)()
        #    proxy_list.extend(px.run())
        #TextBuffer = self.TextView.get_buffer()
        #textbuffer=''
        #for proxy in proxy_list:
        #    textbuffer += proxy+'\n'
        #TextBuffer.insert_at_cursor(textbuffer)
        #self.TextView.set_buffer(TextBuffer)
        pass

    def check_proxys_alive(self,widget):
        pass

    def save_proxy_list(self, widget):
        pass

    def run(self):
        gtk.main()
