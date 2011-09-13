#coding: utf-8

from plugin_base import BasePlugin # Clase base
import urllib2 # Librería para peticiones a web

class ProxylistsNetPlugin(BasePlugin):
     plugin_type = BasePlugin.LIST_PLUGIN
     plugin_author = "overload"
     plugin_version = 0.1

     def proxycapter(self, url, tipo):
         listaproxy = []
         pagina = urllib2.urlopen(url)
         s = pagina.read() # s = "111.111.111.111:111\n222.222.222.222:222"
         r = s.split("\n") # r = ["111.111.111.111:111", "222.222.222.222:222"]
         for p in r:
           if len(p) > 0: # Evita las lineas vacias
             # p = "111.111.111.111:111\r"
             # p = "222.222.222.222:222\r"
             p = p.strip() # Se elimina el \r del final
             valores = p.split(":") # Los valores estan separados por :
             # valores = ["111.111.111.111", "111"]
             proxy = [tipo] + valores # proxy ['SOCKS4', "111.111.111.111", "111"]
             listaproxy.append(proxy) 
         # listaproxy = [('SOCKS4',"111.111.111.111:111"), ('SOCKS4',"222.222.222.222:222")]
         return listaproxy

     def get_list(self):
         lista_socks4 = self.proxycapter("http://www.proxylists.net/socks4.txt", "SOCKS4")
         lista_socks5 = self.proxycapter("http://www.proxylists.net/socks5.txt", "SOCKS5") 
         return lista_socks4 + lista_socks5

# Devuelve el plugin o None si es una clase de plantilla
def get_plugin():
    return ProxylistsNetPlugin()

# Si se ejecuta directamente, mostrar la lista de proxies
if __name__ == "__main__":
    plugin = get_plugin()
    lista  = plugin.get_list()
    for proxy in lista:
        print proxy
