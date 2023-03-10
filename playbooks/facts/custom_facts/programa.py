#!/usr/bin/python3

import json

nginx_corrindo = True 
# Aqui hacemos una llamada a ver si nginx está orriendo o no
# En otro escenario, conectar con una BBDD
# Aqui puedo meter mucha logica para sacar el dato que me interesa

resultado= {
    "nginx_corrindo": nginx_corrindo
}

print(json.dumps(resultado))