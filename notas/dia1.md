# Ansible

Ansible es una familia de productos de software que nos ayudan con AUTOMATIZACIONES.

Quién está detrás de Ansible? Redhat

### Alternativas a Ansible

Puppet
Chef
Salt

## Redhat

Es la empresa que nos demostro que el mundo OpenSource es/puede ser rentable.
Vende sus productos, son gratis? 

De cada producto ofrece 2 "distribuciones", una gratuita, otra de pago, 
mediante un sistema de licenciamiento basado en subscripciones: Basicamente pagamos por un soporte!

| PAGO                                | Proyecto upstream                       |
| ----------------------------------- | --------------------------------------- |
| RHEL                                | Fedora                                  |
| Redhat Openshift Container Platform | OKD                                     |
| Ansible Tower                       | AWX                                     |
| Ansible engine                      | Ansible project                         |

Ansible galaxy: Esto es un servicio (gratuito y de pago... depende del tipo de cuenta)

## Ansible engine / Ansible project

Herramienta de software que nos ofrece:
- Un lenguaje (schema de YAML) para crear scripts de automatización     ->      Playbooks
- Varias sintaxis (3) para definir                                              Inventarios
  Inventario? Catalogo de entornos remotos que pueden ser administrados
              mediante playbooks
- Una serie de comandos, con los que poder aplicar operaciones sobre esos inventarios/playbooks

### Para qué se usa esto en la práctica?

AUTOMATIZACIONES del lado de SISTEMAS:
- Despliegues masivos
- Configurar entornos
- Monitorización 
- Solventar alertas en entornos
- ...

Y esas cosas... no las teníamos ya resueltas de antes?
Si... mediante scripts de la bash, sh... python, ps1

Y entonces, por qué ansible?
La cuestión es que todas esas herramientas de las que hablábamos antes usan una sintaxis IMPERATIVA !
Y ansible usa una sintaxis DECLARATIVA !
Y eso lo cambia TODO !

Mucha gente piensa en Ansible como un reemplazo de los scripts de la bash.
En parte es cierto... pero hay más... mucho más.

Adoptar Ansible implica un CAMBIO DE MENTALIDAD (GRANDE) en el trabajo. Y este tema es el poca gente tiene en cuenta!

La sintaxis declarativa va de la mano de otro concepto: IDEMPOTENCIA ! (aquí esta la magia)
No obstante ese concepto de IDEMPOTENCIA NO ES SENCILLO DE OBTENER... ni gratuito!
Aquí es donde Ansible AMRCA LA DIFERENCIA. Si bien Ansible NO ME REGALA LA IDEMPOTENCIA !

Todas las herramientas que a día de hoy están "triunfando" lo hacen por usar una sintaxis DECLARATIVA:
- Kubernetes/Openshift
- Terraform
- Ansible

# Sintaxis IMPERATIVA

> Felipe! pon una silla debajo de la ventana!                                   IMPERATIVO (doy una orden)
                                                                                Tiempo verbal: Imperativo

Imaginad que ya hay una silla debajo de la ventana.... qué ocurriría en esta situación?
Felipe devolvería ERROR ! Y esto obliga a replantearme el guión (script) de Felipe.

> Felipe, SI NO HAY UNA SILLA debajo de la ventana                              SI = if
>    Felipe! pon una silla debajo de la ventana!                                IMPERATIVO (doy una orden)

Y si hay un mueble debajo de la ventana?

> Felipe, SI HAY ALGO QUE NO SEA UNA SILLA debajo de la ventana                 SI = if
>    Felipe! quitalo!                                                           IMPERATIVO (doy una orden)
> Felipe, SI NO HAY UNA SILLA debajo de la ventana                              SI = if
>    Felipe! pon una silla debajo de la ventana!                                IMPERATIVO (doy una orden)

Y si no hay silla?

> Felipe, SI HAY ALGO QUE NO SEA UNA SILLA debajo de la ventana                 SI = if
>    Felipe! quitalo!                                                           IMPERATIVO (doy una orden)
> Felipe, SI NO HAY UNA SILLA debajo de la ventana                              SI = if
>   Felipe, Si no hay sillas,
>           Felipe, vete al ikea a por una silla !    
>   Felipe! pon una silla debajo de la ventana!                                 IMPERATIVO (doy una orden)

El problema es que al expresarme mediante un lenguaje imperativo, el cerebro lo pongo YO !
Es mia la responsabilidad de definir el procedimiento de actuación.

El lenguaje imperativo, a pesar de parecer muy natural y muy sencillo, da lugar a muchos problemas

Nota: En inglés como se monta un imperativo?
            PRESENTE        IMPERATIVO
- To eat:   you eat         eat more !!!!
- To run:   you run         run more !!!!

make a directory !      Imperativo                                              mkdir
change owner     !      Imperativo                                              chown
change mode                                                                     chmod
list files                                                                      ls

# Sintaxis DECLARATIVA

> Felipe, asegurate de que: debajo de la ventana haya una silla                  orden? SI
          ^^^^^^^^^         De conseguir un determinado ESTADO

Pero... le estoy explicando a Felipe cómo conseguir ese estado?                 NO
Delego en Felipe la responsabilidad de establecer el procedimieto para conseguir ese estado deseado

Y si ya hay una silla? que dirá Felipe?                                         Asegurado !
Y si no la hay?                         La pone                                 Asegurado !
Y si hay un mueble?                     Lo quitará, pondrá la silla             Asegurado !
Y si no hay silla...            Felipe, que no es mi problema... resuelvelo TU !
                                        Felipe, se pira al Ikea                 Asegurado !

En este sentido, Ansible, lo pone más fácil.
La cuestión... es que ahora que dispongo de un lenguaje DECLARATIVO, me planteo cosas que antes no me podía plantear:
IDEMPOTENCIA ! => Esto es algo que antes no me planteaba... por su complejidad.... 
                  Hoy en día si que me lo planteo... gracias a Ansible. 
                  Pero esto es duro, e implica un cambio de chip... GRANDE
                  ESTE ES EL CAMINO !

# Idempotencia

Da igual el estado inicial del que parta, siempre voy a obtener el mismo estado final !

No importa si no hay silla... si ya hay silla... si hay un mueble... da igual.
Una vez que le doy la instrucción a Felipe, tengo garantías de que el sistema quedará como yo quiero!

Claro... antes, usando lenguaje imperativo, me planteaba por ejemplo montar un:
- Script para poner una silla debajo de la ventana
- Quizás me planteaba otro script para monitorizar que la silla sigue debajo de la ventana

- Script de instalación de Oracle Database en un servidor nuevito!              Este ya es tremendamente complicado
- Script de monitorización de un servicio
- Script de intentar que el Oracle vuelva a la vida!                            A manita 
- Y si quiero instalar una versión nueva, en un entorno ue ya tenga Oracle Database.. otro script !

Ansible me da la oportunidad de tener UN UNICO SCRIPT para todo ese trabajo:
- Asegurate de que tenga Oracle versión 17 instalado en tal máquina y funcionando !

Me da igual el estado inicial ... siempre quiero conseguir el mismo estado final = IDEMPOTENCIA !

Y con un UNICO SCRIPT resuelvo todo el problema = UALA !!!!! que jodido va ser esto !

El mundo de hoy... especialmente en el sector IT, no es el mundo de hace 15 años.
Hace 15 años, los scripts de la bash, ps1, me iban guay!
Pero es que estábamos en entornos poco cambiantes (muy estáticos)

## DEV--->OPS 

Devops no es un perfil... no es una persona... es una CULTURA en pro de la AUTOMATIZACION !

Hay muchas herramienats que nos ayudan a automatizar tareas:
- Scripts de la bash, ps1, python...
- Terraform: Creación de entornos en clouds
- Kubernetes: Operación de un entornos de PRODUCCION

Pero esas herramientas hay que orquestarlas entre si. Y además hay que determinar CUANDO deben ejecutarse.
Y ahí salen toda una nueva generación de herramientas de software (que antes no existían) que nos ayudan 
a automatizar esos trabajos: Servidores de automatización:
- Jenkins
- AzureDevops
- Travis CI
- Gitlab CI/CD
- Github actions

# Ansible Tower / AWX

Una herramienta que nos ofrece:
- Una interfaz web, desde la que poder ejecutar playbooks sobre inventarios
- Un repositorio centralizado de credenciales
- API REST para solicitar remotamente la ejecución de tareas / playbooks
- **Un mecanismo para orquestar playbooks**

# Palabros importantes en el ecosistema ANSIBLE / Arquitectura de Ansible

Vamos a tener Ansible instalado en una máquina: NODO CONTROLADOR

Requisitos de esta máquina:
Máquina LINUX !
Python... una versión modernita!
Ya lo tengo todo. Instalo Ansible desde mi repositorio favorito. Trivial. Docu de Ansible


# Nodos gestionados

Ansible, desde el nodo controlador ejecutará scripts con tareas dentro de entornos remotos: NODO GESTIONADO

En estos entornos necesitamos tener instalado:
- Python..  una versión modernita
- Necesito un protocolo y un servicio de conexión con el remoto: ssh, winrm,... 

# Inventario

Catalogo de nodos gestionados. Dentro de él, y asociado a cada nodo, podremos dar algunas características adicionales:
- Usuario que necesito para conectar con un entorno
- Su IP
- Protocolo
- Puerto
- Credenciales
- ...

Fichero o una carpeta con el catalogo (inventario)

# Playbooks

Un playbook es un script de automatización. En él definimos tareas que vamos a ejecutar sobre unos entornos.
Esto a su vez va a ser también un fichero o una carpeta.

Tanto los playbooks como los inventarios van a terminar almacenados en un sistema de control de versiones: GITLAB

Teneis que tener en cuenta que estamos creando PROGRAMAS / SOFTWARE!
Y vamos a adherirnos a las mismas practicas que usan los desarrolladores de software.
Entre las cuales, la principal es : MI SOFTWARE tiene que tener versiones y estar
bajo control en un sistema de control de código fuente: GIT

# Modulos de Ansible

Un módulo de Ansible es un programa que se encarga de realizar un tipo de tarea muy concreto.
A saber:
- Quiero crear en una máquina remota un usuario: NECESITO UN MODULO PARA ELLO
- Quiero abrir un puerto en una máquina ubuntu:  NECESITO UN MODULO PARA ELLO
- Quiero abrir un puerto en una máquina redhat:  NECESITO OTRO MODULO PARA ELLO
- Crear un archivo:  NECESITO OTRO MODULO PARA ELLO
- Levantar un servicio: NECESITO OTRO MODULO MAS

Quien ejecuta una tarea dentro de ANSIBLE es un MODULO
Ansible simplemente me da una sintaxis con la que poder comunicarme con MODULOS.

Al final, un MODULO es un script, programado habitualmente en PYTHON (de ahí que necesitemos python por todos lados)
Es un script muy trabajado... en lenguaje imperativo.

Por ejemplo, podría tener el MODULO: Asegurar que hay una silla debajo de la ventana.
Ansible viene precargado con MILES DE MODULOS!

Cuando se monta un MODULO, se intenta, con mucho mucho mucho esfuerzo que sea IDEMPOTENTE (no siempre es posible)
El 99.9% de los modulos de Ansible respetan el principio de IDEMPOTENCIA.

Ansible "garantiza" la idempotencia a nivel de MODULO: OJO !!!!!
NO DE PLAYBOOK. Ese trabajo es mio (y esto nos dará dolores de cabeza)

# Vamos a hacer uso intensivo de YAML.

YAML es un lenguaje
lenguaje de marcas? Lenguaje de estructuración de información: JSON, XML, HTML
HTML es un lenguaje de estructuración de información de dominio específico (para páginas web)
XML, JSON o YAML son de proposito general (sirven para multitud de tipos de información)

YAML:   YAML ain't markup language
HTML    \
 XML    / Markup language: <tag atrr="valor"></tag>

Es el lenguaje de estructuración de ionformación que más fuerza está cogiendo. Se ha comido literalmente a JSON.
Hoy en día cualquier documento JSON es un documento YAML válido. Esto es desde la versión 1.2 de YAML 

YAML nos permite definir estructuras JERARQUICAS: ARBOLES

Hay muchas formas en programación de representar datos:
ARRAY, lista
ARARY Asociativo (diccionario, mapa, tabla clave-valor)
STACK: PILA
MATRIZ
COLA
ARBOL

Cada programa que decide usar documentos YAML, DEBE DEFINIR SU PROPIO ESQUEMA YAML.

Un esquema (SCHEMA) YAML refleja la estructura de tipos de datos que debe tener un documento, para ser considerado VALIDO para ese programa concreto.

UNO DE LOS OBJETIVOS DEL CURSO es aprender el esquema que define ANSIBLE para los playbooks y para los inventarios.

# Ejecución de playbooks

La realizamos con el comando: `ansible-playbook <playbook>`

Este comando me informa de las tareas que se van ejecutando en cada playbook
Y además, me ofrece un resumen con el número de tareas:
- TOTALES que han acabado BIEN
- TOTALES que han provocado cambios en el entorno
- TOTALES QUE HAN FALLADO


Una tarea puede acabar en estado:
- OK:       Que la tarea tenemos asegurado que se ha realizado correctamente.
            Que tenemos asegurado que nuestro sistema está en el estado deseado (según se haya definido en esa tarea)
- CHANGED:  Que la tarea tenemos asegurado que se ha realizado correctamente.
            Que tenemos asegurado que nuestro sistema está en el estado deseado (según se haya definido en esa tarea)
            Pero... para llegar a ese estado, ha sido necesario hacer cambios en el sistema
- FAILED:   Que una tarea ha fallado

En principio, la segunda vez que ejecute un playbook, cuantas tareas deberían estar en estado CHANGED? NINGUNA 
Para nosotros va a ser MUY IMPORTANTE discernir cuando al ejecutar una tarea ESTA PROVOCA O NO CAMBIOS.

# JINJA2

Libreria de PLANTILLA (Templating) disponible en PYTHON.

Me permite definir plantillas, que den lugar a textos, listas, .... a datos.

Esas plantillas tienen su propia sintaxis a la hora de escribirse.

---

# SELinux

Security Enhanced for Linux.... De serie en las máquinas REDHAT