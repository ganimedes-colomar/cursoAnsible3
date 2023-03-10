# Custom facts

Son archivos que creamos en la carpeta /etc/ansible/facts.d del remoto.

El nombre del archivo será el nombre del fact(variable) que vamos a usar posteriormente en ansible.
De hecho, para usar ese dato, tendremos que escribir: -
- `ansible_local.NOMBRE_FACT`
- `ansible_facts.ansible_local.NOMBRE_FACT`

# CUSTOM FACT ESTÁTICO

El fichero que vamos a crear para un fact debe ser un json... y le ponemos extensión ".json"
La extensión no se tiene en cuenta en el nombre del fact:
`monitorizada.json` -> { "deployed": true, ... }
Para recuperar el dato: `ansible_local.monitorizada.deployed`

# CUSTOM FACT DINAMICO

Puedo crear un fichero ahí dentro de esa carpeta con mi lenguaje de programación de scripting favorito:
- bash
- ps1
- py
- perl

Que hace Ansible, ejecuta ese fichero 
(motivo por el cuál, el fichero necesita permisos de ejecución... eso es lo que mira Ansible)
De hecho Ansible no sabe en que lenguaje está escrito aquello... Para eso esta el SHEBANG !

Pasa igual que con los estáticos. El resultado del programa (stdout) se toma como valor del fact. Y al fact accedo
a través del nombre del archivo... sin extensión.


# Ansible Tower:

La característica más exclusiva de tower es:
- Capacidad para orquestar playbooks

El hecho de que me permita ejecuatr playbooks? No necesito Ansible Tower para nada.
El hecho de que me permite tener un inventario centralizado... Mentira...
    Ansible Tower lo lee de GIT... es en git donde tengo el inventario centralizado.
    Lo puedo leer de git desde cualquier sitio
El hecho de poder hacer programaciones de playbooks: Ejecuta este playbook los jueves a las 10
    Eso lo hace una herramienta como JENKINS 100 veces mejor...
    con más opciones de programación / planificación

Lo único que realmente nos ofrece TOWER que no ofrece nadie más es la 
capacidad de orquestar playbooks => Y ESTO ES MUY VALIOSO

---
Me llega un servidor (físico o virtual) nuevo.
Y quiero ponerle un nginx... a funcionar!

Lo quiero gestionar con Ansible?

- Darlo de alta en el known_hosts desde donde vaya a ejecutar ansible
- Lo que hicimos en el playbook que instalaba el nginx y un app.
- Quiero monitorizar esa máquina? Le quiero montar un agente de monitorización? Pues claro
- La quiero registrar en el CMDB? SIP
- Con que usuario voya. instalar el nginx? usuario: TOWER
- Usuario TOWER que se contectará a la máquina mediante una clave ssh.... que habrá que dejar allí
- Y le voy a configruar la red?
- En la máquina pondré una determinada policita de actualización de paquetes... y haré actualziaciones con una periodicidad
- Si la máquina es RHEL ->SELinux


TODO ESO LO METO EN UN PLAYBOOK UNICO? Ni de broma.

----

No tengo un PC, tengo un servidor. Físico.
El servidor tendré cuantas NIC (tarjetas de red) De 2 a 30... quiero redundancia 
Esas tarjetas de red las haré un bonding... a nivel de SO las monto como un único interfaz de red
A lo mejor creo 2/3 interfaces de red

NIC 1   ----- App.     (eth)
NIC 2   ----/
NIC 3   ----/
NIC 4   ----> Servicio (servicio)
NIC 5   ----- Comunicaciones internas de la app
NIC 6   ----/

    
---

En un playbook, una tarea puede fallar.
Si falla, tengo opción de?
- Rescue y rescatarla... y entonces aunque haya ido mal, mi playbook sigue y hará otras tareas

Subir de nivel
    
En una orquestación de playbooks (workflow), una playbook puede fallar.
Si falla, tengo opción de?
- Rescue y rescatarlo... y entonces aunque haya ido mal, mi workflow sigue y hará otras tareas


    
    
    
    
    
