# Role

$ ansible-galaxy init ROLENAME
    
    .
    └── knownhosts
        ├── README.md
        ├── defaults                Meteremos las variables del role que la gente vaya a modificar
        │   └── main.yml
        ├── files                   Ficheros que nuestro role (tareas) puedan usar
        ├── handlers                Handlers que puedan ser lanzados desde esas tareas
        │   └── main.yml
        ├── meta                    Donde hay metadatos (nombre del rol, licencia, sitio web) que se compartirán si publicamos el role
        │   └── main.yml
        ├── tasks
        │   └── main.yml            Tareas reutilizables
        ├── templates               Plantillas que usen nuestras taras
        ├── tests                   Pruebas del rol, para ver si funciona
        │   ├── inventory               Inventario de prueba
        │   └── test.yml                Playbook de prueba
        └── vars                    Meteremos nuestras propias variables que no quiero que me toquen
            └── main.yml
            
# Facts

Que es un fact? DATO al que accedo a través de un NOMBRE (variable)

`ansible_facts` < - variable que generaba ansible cuando ejecuto un gather_facts

# Variables

Hemos creado/usado nosotros variables en los playbooks?
- Usado si, mucho
- Creado ..... bueno:
    - [x] Hemos definido variables, a las que hemos asignado un valor.
    - [x] Hemos definido variables, a las que al ejecutar un playbook se les asignaba un valor (--extra-vars)
    - [ ] Hemos definido variables, a las que dinamicamente (durante la ejecución del playbook) les dieramos un valor

Si reordais, tenemos una tarea que se llama: gather_facts.... que también podemo ejecutar con un módulo: setup

# Qué datos me trae?

Información del servidor.. qué infromación? la que pidamos (o todo)... de entre? la que Ansible es capaz de recoger

Y si me interesa tener mis propios datos? asociados a cada máquina?

Por ejemplo:

# CMDB

Base de datos que contiene todos los entornos/nodos que tenemos en la empresa...
Y cada entorno/nodo en el CMDB tiene un IDENTIFICADOR.

Quizás ese ID me hace falta en algún playbook.

Donde podría guardarlo?
- Como una variable en el inventario.                                                                                       REPOSITORIO CENTRALIZADO DE IDs
- Dentro de cada entorno. Como un CUSTOM FACT, de forma que cuando a Ansible le pida un GATHER_FACTS, me traiga ese dato.   REPOSITORIO DESCENTRALIZADO DE INFO
    Un custom fact es un dato, con un nombre que puedo dejar en un entorno remoto, para que ansible pueda recuperarlo con un gather_facts o setup

Quiero saber si en un máquina está corriendo nginx
- Los ansible_facts me dan esa información? NO

Quiero saber si en una máquina hemos instalado ya el agente de monitorización
- Los ansible_facts me dan esa información? NO

Me puede interesar generar un CUSTOM FACT dentro del entorno con esa información.

El CMDB_ID es un dato que podría dejar de forma ESTATICA.
Si he montado o no el AGENTE de monitorización es un dato que puedo dejar de forma ESTATICA.
    Cuando instalo el agente dejo creado un ficherito, indicando que YA HE INSTALDO EL AGENTE. 

En cambio, para saber si nginx está corriendo o no... me vale algo estático? NO
    Aquí entre el concepto de CUSTOM FACTS ESTÁTICOS y CUSTOM FACTS DINAMICOS

