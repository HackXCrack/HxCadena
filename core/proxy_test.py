#coding: utf-8

import socket

# Función contribuída por overload
# timeout añadido por kenkeiras
def filtrar(lista, tiempo_de_espera = 10.):
    nueva_lista = []
    for proxy in lista:
        s = socket.socket()
        s.settimeout(tiempo_de_espera)
        try:
            s.connect((proxy[1],int(proxy[2])))
        except:
            pass
        else:
            nueva_lista.append(proxy)
            s.close()
    return nueva_lista
