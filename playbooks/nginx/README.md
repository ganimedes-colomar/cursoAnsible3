# Vamos a montar nuestro primer playbook de verdad !

1º Acabar teniendo nginx instalado (en una versión muy concreta) y corriendo en un servidor
2º Quiero una web desplegada dentro del nginx. La web la vamos a sacar de un repo de git
3º Queremos que nginx funcione en un puerto muy concreto y leyendo la web de un directorio muy concreto


Eso debe ejecutarse suponiendo que tengo una maquina UBUNTU !
Ni lo voy a comprobar. Lo doy por supuesto.

ESE ES EL PLAYBOOK... o mejor dicho, lo que espero del playbook.

Estimación de número de tareas que nos van a hacer falta?
6 I
5 I I
4 I
3 I I

si lo hacemos en menos de 20 nos damos damos con un canto en los dientes !  WTF !!!!!!!

Que nos va a joder aquí? sin complicarlo! 
EL PUÑETERO CONCEPTO DE IDEMPOTENCIA

Que significa que el playbook debe funcionar si?
- No existe una instalacion de nginx
- Si existe la que necesitamos
- Si existe otra
- Si existe una instalación , pero usa otros puertos o directorio
- Si tengo ya una versión vieja de la app
- Si aun no hay aplciacion
- ....
- 



ESCENARIO TIPICO:
Maquina limpia: 
    
    instalar git si no lo está
    instalar curl si no lo esta
    
    mkdir web
    cd web
    git clone https://github.com/IvanciniGT/webEjemploAnsible .
    
    sudo apt install nginx -y
    sudo vi /etc/nginx/sites-available/default
        METIDO EL PUERTO Y LA CARPETA 
    sudo systemctl restart nginx
    curl localhost:81

OTRO ESCENARIO:
Maquina en produccion, sirviendo la version antigua de la 
aplciacion en el mismo nginx que necesito ahora
    instalar git si no lo está
    instalar curl si no lo esta
    git pull
    Necesito instalar nginx? NO
    Y cambiarle la configruación? NO
    sudo systemctl restart nginx

OTRO ESCENARIO:             Monitorizar
Maquina en produccion, 
sirviendo la misma version de la aplciacion 
en el mismo nginx que necesito ahora

OTRO ESCENARIO:
Se ha caido el nginx... pero todo está instalado dpm

OTRO ESCENARIO:
Nginx está instalado en su versión y la app también
Pero a un gracioso se le ha ocurrido cambiar los puertos
    Necesito nuevo fichero de configuracion
    Reinicio del servicio
    

    
Para ejecutarlo cada media hora o 5 minutos:
    - PRUEBAS -> SI PRUEBAS FALLA -> EJECUTAR TODO -> SI FALLA -> QUE ME NOTIFIQUE
        ^^^^^^
      Cuantas veces estoy ejecutando el playbook? 1 o 2 ->
        ORQUESTACION DE PLAYBOOKS < Ansible tower
        
    
Si cambiamos el nginx corporativamente:
    - INSTALACION -> SI FALLA? -> EJECUTA TODO? -> SI FALLA -> QUE ME NOTIFIQUE

Si cambiamos la versión de la app
    - DESPLIEGUE
    
Si cambioamos puertos
    - CONFIGURACION
    
Si estas cosas las estoy lanzando a mano desde tower
    (SKIP) NOTIFICACION