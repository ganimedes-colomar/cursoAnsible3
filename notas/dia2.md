Al conectarnos con un entorno remoto, lo hacemos a través de unas credenciales:
- usuario
- mecanismo de autenticación: password, ssh key...

El usuario tendrá localmente privilegios para realizar unas determinadas tareas.

sudo 

----

# HANDLERS:

tarea 1:
ejecutar el procedimiento de despliegue de una app en un weblogic
¿Quién define la tarea 1? El tio que sepa de weblogic que lo haga en el yaml


Cuando despliego una nueva aplicación (cuando la tarea 1 provoca un cambio)
qué quiero hacer? Comenzar a monitorizar la aplciación.

handler 1: 
iniciar un proceso de monitorización para esa aplicación recien desplegada
¿quien define el handler? El tio que sepa de monitorización..

Quién escribe la tarea 1?



Programacion patron orientado a eventos 


tarea 1:
ejecutar el procedimiento de despliegue de una app en un weblogic
¿Quién define la tarea 1? El tio que sepa de weblogic que lo haga en el yaml
Si la tarea provoca cambio NOTIFICO: NUEVA_APLICACION !!!!! A quien interese

        VVV
        NUEVA_APLICACION
        ^^^
        
handler 1: 
iniciar un proceso de monitorización para esa aplicación recien desplegada
¿quien define el handler? El tio que sepa de monitorización..
Escucharan si hay una NUEVA_APLICACION... y entonces harán sus cositas

---

# VARIABLES: 

En ansible podemos hacer uso de variables.... con varias finalidades:
- Acceder a información que se genera de forma dinámica:                        ansible_facts

En el bloque vars del PLAY:
    - A veces, me interesa definir una variable porque hay un dato que voy a usar vacias veces en el playbooks
        Va a crear un usuario "felipe" y le va a asignar un home "/home/felipe"
        Y en ese home, coy a copiarle unos archivos
        Y de paso le voy a generar otros
      ¿Cuantas veces uso el dato "HOME DEL USUARIO FELIPE"?                           montonones
      En este caso, me puede interesar definir el dato en una variable, de forma que si mañana decido cambiarlo, solo lo tenga que cambiar en un único sitio
    - Tener todos los DATOS en un UNICO SITIO
      Quizas el nombre de usuario FELIPE lo uso solo una vez... pero ya lo pongo deonde defina el home
      Simplemente por dejar los datos juntos.... en un unico sitio y que si en el futuro lo he de cambiar, me sea sencillo
      
- Quizas por me interese PARAMETRIZAR un fichero playbook. Es decir que el playbook se ejecute con distintos valores de la variable
  Tengo un playbook que abre puertos en un servidor
    Podemos suministrar el valor de una variable en tiempo de ejecución, al llamar al playbook:
    --extra-vars VARIABLE=VALOR
    --extra-vars @ficheroDeVariables
- ...
- set_fact


En Ansible puedo definir variables en más de 20 sitios distintos.... ES UNA LOCURA !

A nivel de una tarea podemos definir vars... ya os diré para que sirve eso. SU CASO DE USO.



sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y
